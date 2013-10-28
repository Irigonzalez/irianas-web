import requests
from flask import (Blueprint, render_template, session, redirect)
from irianas_web.core import require_login
from irianas_web.core import url_server

irianas_module = Blueprint('home', __name__, template_folder='templates')


@irianas_module.route('/home/')
@irianas_module.route('/')
@irianas_module.route('/index/')
@require_login
def home():
    data = dict(token=session.get('token'))
    try:
        r = requests.get(url_server + 'info', data=data, verify=False)
    except requests.ConnectionError:
        return redirect('/error/connection')

    if r.status_code == 200:
        result = r.json()
        return render_template('home.html', values=result)
    else:
        return redirect('/login')
