import requests
import simplejson as json
from functools import wraps
from flask import session, redirect, abort, render_template

url_server = 'https://127.0.0.1:9001/'


def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        print session.get('username')
        print session.get('token')
        if session.get('username') and session.get('token'):
            try:
                r = requests.get(url_server + 'login',
                                 data=dict(token=session.get('token')),
                                 verify=False)
            except requests.ConnectionError:
                return redirect('/error/connection')
            if r.status_code == 200:
                return f(*args, **kwargs)
        return redirect('/login')
    return inner


def services_config(method, service, form, ip, template):
    data = dict(ip=ip,
                token=session['token'],
                service=service)
    if method == 'POST':
        for key, value in form.iteritems():
            if not value:
                return redirect(
                    '/client/services/config/' + service + '/' + ip)
        else:
            data = dict(data.items() + form.items())
            try:
                r = requests.post(url_server + 'client/services',
                                  data=data, verify=False)
            except requests.ConnectionError:
                return abort(404)

            if r.status_code == 200:
                items = dict(data.items())
                msg_success = 'Configuraci&oacute;n guardada con &eacute;xito.'
                return render_template(template, msg_success=msg_success,
                                       ip_client=ip, **items)
        msg = 'Error al guardar la configuraci&oacute;n.'
        return render_template(template, msg=msg,
                               ip_client=ip, **form)

    else:
        try:
            r = requests.get(url_server + 'client/services',
                             data=data, verify=False)
        except requests.ConnectionError:
            return abort(404)

        if r.status_code == 200:
            result = r.json()
            return render_template(template, ip_client=ip,
                                   **json.loads(result))
