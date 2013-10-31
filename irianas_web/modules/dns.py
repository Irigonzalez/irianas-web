from flask import Blueprint, request
from irianas_web.core import require_login, services_config

irianas_module = Blueprint('dns', __name__, template_folder='templates')


@irianas_module.route('/client/services/config/bind/<ip>',
                      methods=['GET', 'POST'])
@require_login
def bind(ip):
    return services_config(request.method, 'bind', request.form, ip,
                           'dns.html')
