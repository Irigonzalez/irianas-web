import requests
import datetime
from flask import Blueprint, render_template, redirect, jsonify, session, abort
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('user', __name__, template_folder='templates')


@irianas_module.route('/user/record/', methods=['GET'])
@require_login
def record_user():
    data = dict(token=session['token'])
    try:
        r = requests.get(url_server + 'user/record',
                         data=data, verify=False)
    except requests.ConnectionError:
        return abort(404)
    if r.status_code == 200:
        result = r.json()
        print result
        record_dict = dict()

        return result
