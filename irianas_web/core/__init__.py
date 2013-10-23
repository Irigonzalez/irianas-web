from flask import session, redirect


def require_login(f):

    def inner(*args, **kwargs):
        if session.get('username') and session.get('token'):
            return f(*args, **kwargs)
        else:
            return redirect('/login')
        return inner
