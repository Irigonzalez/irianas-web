import requests
import grequests
from flask import Blueprint, render_template, redirect, jsonify, session, abort
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('client', __name__, template_folder='templates')


@irianas_module.route('/client/<ip>', methods=['GET'])
@require_login
def client(ip):
    return render_template('client.html', ip_client=ip)


@irianas_module.route('/client/', methods=['GET'])
@require_login
def redirect_to_clients():
    return redirect('/clients/')


@irianas_module.route('/client/<task>/<ip>', methods=['GET'])
@require_login
def task_client(task, ip):
    data = dict(ip=ip, token=session['token'])
    try:
        r = requests.get(url_server + 'client/task/' + task,
                         data=data, verify=False)
    except requests.ConnectionError:
        return abort(404)

    if r.status_code == 200:
        return jsonify(**r.json())
    return abort(404)


@irianas_module.route('/client/services/<ip>', methods=['GET'])
@require_login
def services_client(ip):
    data = dict(ip=ip, token=session['token'])

    list_services = ['apache', 'vsftpd', 'mysql', 'bind', 'ssh']
    list_cmd = ['status', 'installed']

    dict_services = dict()

    for service in list_services:
        dict_services[service] = dict()
        for cmd in list_cmd:
            dict_services[service][cmd] = None
            try:
                r = requests.get(
                    url_server + 'client/services/' + service + '/' + cmd,
                    data=data, verify=False)
            except requests.ConnectionError:
                return abort(404)

            if r.status_code == 200:
                result = r.json()
                if cmd is 'installed':
                    cmd = 'status_service'
                dict_services[service][cmd] = result[cmd]
            else:
                return abort(404)
    return jsonify(**dict_services)


@irianas_module.route('/client/services/<service>/<cmd>/<ip>', methods=['GET'])
@require_login
def services_task_client(service, cmd, ip):
    data = dict(ip=ip, token=session['token'])

    list_services = ['apache', 'vsftpd', 'mysql', 'bind', 'ssh']

    if service in list_services:
        r = grequests.request(
            'GET', url_server + 'client/services/' + service + '/' + cmd,
            data=data, verify=False)
        r.send()
        return jsonify(status=1)
    return abort(404)


@irianas_module.route('/client/events/<ip>', methods=['GET'])
@require_login
def events_client(ip):
    data = dict(ip=ip, token=session['token'])

    try:
        r = requests.get(
            url_server + 'client/events', data=data, verify=False)
    except requests.ConnectionError:
        return abort(404)

    if r.status_code == 200:
        return jsonify(**r.json())

    return abort(404)
