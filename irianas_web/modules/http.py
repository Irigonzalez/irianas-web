import requests
import simplejson as json
from flask import Blueprint, render_template, request, abort, session, redirect
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('http', __name__, template_folder='templates')


@irianas_module.route('/client/services/config/httpd/<ip>',
                      methods=['GET', 'POST'])
@require_login
def http(ip):
    data = dict(ip=ip,
                token=session['token'],
                service='apache')
    if request.method == 'POST':
        for key, value in request.form.iteritems():
            if not value:
                return redirect('/client/services/config/httpd/' + ip)
        else:
            data = dict(data.items() + request.form.items())
            try:
                r = requests.post(url_server + 'client/services',
                                  data=data, verify=False)
            except requests.ConnectionError:
                return abort(404)

            if r.status_code == 200:
                items = dict(request.form.items())
                msg_success = 'Configuraci&oacute;n guardada con &eacute;xito.'
                return render_template('http.html', msg_success=msg_success,
                                       ip_client=ip, **items)
        msg = 'Error al guardar la configuraci&oacute;n.'
        return render_template('http.html', msg=msg,
                               ip_client=ip, **request.form)

    else:
        try:
            r = requests.get(url_server + 'client/services',
                             data=data, verify=False)
        except requests.ConnectionError:
            return abort(404)

        if r.status_code == 200:
            result = r.json()
            return render_template('http.html', ip_client=ip, **json.loads(result))
