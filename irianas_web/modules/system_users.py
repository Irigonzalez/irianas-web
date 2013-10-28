import requests
import datetime
from flask import \
    Blueprint, render_template, redirect, request, session, abort, jsonify
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('system_users', __name__,
                           template_folder='templates')


def get_list_users():
    data = dict(token=session['token'])
    try:
        r = requests.get(url_server + 'user',
                         data=data, verify=False)
    except requests.ConnectionError:
        return None

    if r.status_code == 200:
        result = r.json()
        if not result.get('status'):
            return result['users']
    return None


@irianas_module.route('/users/')
@require_login
def list_users():
    users = get_list_users()
    if users:
        return render_template('users.html', users=users)
    else:
        return render_template(
            'users.html', msg='No hay usuarios para mostrar.')


@irianas_module.route('/users/password/<user>', methods=['GET', 'POST'])
@require_login
def change_password_user(user):
    if request.method == 'POST':
        if request.form['user_password'] == \
           request.form['user_password_repeat'] and \
           request.form['user_password'] and \
           request.form['user_password_repeat']:
            data = dict(user_system=user,
                        password=request.form['user_password'],
                        token=session['token'])
            try:
                r = requests.put(url_server + 'user/update',
                                 data=data, verify=False)
            except requests.ConnectionError:
                return abort(404)
            if r.status_code == 200:
                result = r.json()
                if result.get('action'):
                    return render_template(
                        'users_password.html', user=user,
                        msg_success="Contrase&ntilde;a Modificada.")
            return render_template(
                'users_password.html', user=user,
                msg="Error en la transacci&oacute;n. Por favor revise \
                    el usuario o la contrase&ntilde;a. <strong>NOTA: \
                    </strong> Es importante que coincidan las \
                    contrase&ntilde;as.")
        return render_template('users_password.html', user=user)
    else:
        return render_template('users_password.html', user=user)


@irianas_module.route('/users/delete/<user>', methods=['GET', 'POST'])
@require_login
def delete_user(user):
    if request.method == 'POST':
        data = dict(user_system=user,
                    token=session['token'])
        try:
            r = requests.put(url_server + 'user/delete',
                             data=data, verify=False)
        except requests.ConnectionError:
            return abort(404)

        users = get_list_users()

        if r.status_code == 200:
            result = r.json()

            if result['action']:
                msg_success = 'Usuario eliminado con &eacute;xito.'
                return render_template('users.html',
                                       msg_success=msg_success,
                                       users=users)

        return render_template('users.html',
                               msg='No se pudo procesar la solicitud.',
                               users=users)

    else:
        msg = 'Desea eliminar el usuario {user}?'.format(user=user)
        link = '/users/delete/{user}'.format(user=user)
        link_back = '/users/'
        return render_template(
            'question.html', msg=msg, link=link, link_back=link_back)


@irianas_module.route('/time/', methods=['GET', 'POST'])
@require_login
def time_user():
    data = dict(username=session['username'],
                token=session['token'])
    if request.method == 'POST':
        try:
            r = requests.get(url_server + 'user/expand',
                             data=data, verify=False)
        except requests.ConnectionError:
            return abort(404)

        if r.status_code == 200:
            return jsonify(**r.json())

    else:
        try:
            r = requests.get(url_server + 'user/time',
                             data=data, verify=False)
        except requests.ConnectionError:
            return abort(404)

        if r.status_code == 200:
            return jsonify(**r.json())
    return abort(404)


@irianas_module.route('/users/add/', methods=['GET', 'POST'])
@require_login
def add_user():
    if request.method == 'POST':
        if request.form['user_password'] == \
           request.form['user_password_repeat'] and \
           request.form['user_password'] and \
           request.form['user_password_repeat']:

            data = dict(user_system=request.form['user_system'],
                        password=request.form['user_password'],
                        token=session['token'])
            try:
                r = requests.post(url_server + 'user',
                                  data=data, verify=False)
            except requests.ConnectionError:
                return abort(404)
            users = get_list_users()

            if r.status_code == 200:
                result = r.json()

                if result['action']:
                    msg_success = 'Usuario agregado con &eacute;xito.'
                    return render_template('users.html',
                                           msg_success=msg_success,
                                           users=users)

            return render_template('users.html',
                                   msg='No se pudo procesar la solicitud.',
                                   users=users)
        return render_template('users_create.html')
    else:
        return render_template('users_create.html')
