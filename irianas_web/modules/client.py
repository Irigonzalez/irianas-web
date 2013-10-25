from flask import Blueprint, render_template
from irianas_web.core import require_login

irianas_module = Blueprint('client', __name__, template_folder='templates')


@irianas_module.route('/client/', methods=['GET'])
@require_login
def client():
    return render_template('client.html')
