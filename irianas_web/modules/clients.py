import requests
from flask import Blueprint, render_template, session
from irianas_web.core import require_login, url_server

irianas_module = Blueprint('clients', __name__, template_folder='templates')


@irianas_module.route('/clients/', methods=['GET'])
@require_login
def clients():
    data = dict(token=session.get('token'))
    r = requests.get(url_server + 'client/List', data=data, verify=False)
    if r.status_code == 200:
        result = r.json()

    else:
        msg = 'No hay clientes para administrar.'
        return render_template('clients.html', msg=msg)
