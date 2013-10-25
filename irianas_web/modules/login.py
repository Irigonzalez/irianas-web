# -*- coding: utf-8 -*-
import requests
from flask import Blueprint, render_template, request, session, redirect
from irianas_web.core import url_server
from irianas_web.core import require_login

irianas_module = Blueprint('login', __name__, template_folder='templates')


@irianas_module.route('/login/', methods=['GET', 'POST'])
def login():
    if request.form.get('user') and request.form.get('password'):
        data = {"user": request.form.get('user'),
                "pass": request.form.get('password')}
        r = requests.post(url_server + 'login', data=data, verify=False)
        if r.status_code == 200:
            result = r.json()
            if result.get('token'):
                session['token'] = result.get('token')
                session['username'] = result.get('user')
                return redirect('home')
            else:
                msg = 'Error de autenticaci&oacute;n.'
        else:
            msg = 'Error en el servidor.'
    else:
        msg = ''
    return render_template('login.html', msg=msg)


@irianas_module.route('/logout/', methods=['GET'])
@require_login
def logout():
    data = dict(token=session.get('token'))
    r = requests.put(url_server + 'login/' + session.get('username'),
                     data=data, verify=False)
    if r.status_code == 200:
        result = r.json()
        if result.get("action"):
            session['username'] = None
            session['token'] = None
            return redirect('/login')
        else:
            return redirect('/home')
    elif r.status_code == 401:
        return redirect('/login')
