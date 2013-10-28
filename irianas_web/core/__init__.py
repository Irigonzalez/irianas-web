import requests
from functools import wraps
from flask import session, redirect

url_server = 'https://127.0.0.1:9001/'


def require_login(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if session.get('username') and session.get('token'):
            try:
                r = requests.get(url_server + 'login',
                                 data=dict(token=session['token']),
                                 verify=False)
            except requests.ConnectionError:
                return redirect('/error/connection')
            if r.status_code == 200:
                return f(*args, **kwargs)
        return redirect('/login')
    return inner
