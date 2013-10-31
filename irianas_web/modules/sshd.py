from flask import Blueprint, request
from irianas_web.core import require_login, services_config

irianas_module = Blueprint('ssh', __name__, template_folder='templates')


@irianas_module.route('/client/services/config/ssh/<ip>',
                      methods=['GET', 'POST'])
@require_login
def ssh(ip):
    return services_config(request.method, 'ssh', request.form, ip,
                           'ssh.html')
