import requests
from flask import Blueprint, render_template, session, redirect, request
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('clients', __name__, template_folder='templates')


@irianas_module.route('/clients/', methods=['GET'])
@require_login
def clients():
    data = dict(token=session.get('token'))

    try:
        r = requests.get(url_server + 'client/List', data=data, verify=False)
    except requests.ConnectionError:
        return redirect('/error/connection')

    if r.status_code == 200:
        result = r.json()
        print result
        return render_template('clients.html', clients=result['result'])
    else:
        msg = 'No hay clientes para administrar.'
        return render_template('clients.html', msg=msg)


@irianas_module.route('/clients/delete/<ip>', methods=['GET', 'POST'])
@require_login
def delete_client(ip):
    if request.method == 'POST':
        data = dict(token=session.get('token'), ip=ip)
        try:
            r = requests.put(url_server + 'client', data=data, verify=False)
        except requests.ConnectionError:
            return redirect('/error/connection')

        var = dict(link='/clients/')
        if r.status_code == 200:
            var['msg_success'] = 'Cliente eliminado con &eacute;xito.'
            return render_template('msg.html', **var)
        else:
            var['msg'] = 'Error al eliminar el client'
            return render_template('msg.html', **var)
    else:
        var = dict(link='/clients/delete/' + ip,
                   link_back='/clients/',
                   msg='Desea eliminar el cliente ' + ip + '?')
        return render_template('question.html', **var)


@irianas_module.route('/client/add/', methods=['GET', 'POST'])
@require_login
def create_client():
    if request.method == 'POST':
        msg = dict()
        if request.form.get('ip'):
            data = dict(ip=request.form.get('ip'), token=session['token'],
                        username=session['username'])
            try:
                r = requests.post(url_server + 'client', data=data,
                                  verify=False)
            except requests.ConnectionError:
                return redirect('/error/connection')

            if r.status_code == 200:
                result = r.json()
                if result['status'] == -1:
                    msg = dict(msg="El Cliente existe o ha sido agregado a \
                        otro servidor.")
                elif result['status'] == 0:
                    msg = dict(msg="Cliente no agregado.")
                else:
                    msg = dict(msg_success="Cliente agregado.")
            elif r.status_code == 404:
                msg = dict(msg="Cliente no v&aacute;lido.")
            else:
                msg = dict(msg="Error con el servidor.")
        return render_template('create_client.html', **msg)
    else:
        return render_template('create_client.html')
