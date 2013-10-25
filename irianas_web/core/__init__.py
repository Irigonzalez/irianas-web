from flask import session, redirect

url_server = 'https://127.0.0.1:9001/'


def require_login(f):

    def inner(*args, **kwargs):
        if session.get('username') and session.get('token'):
            return f(*args, **kwargs)
        else:
            return redirect('/login')
    return inner
