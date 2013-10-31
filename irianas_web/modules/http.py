from flask import Blueprint, request
from irianas_web.core import require_login, services_config

irianas_module = Blueprint('http', __name__, template_folder='templates')


@irianas_module.route('/client/services/config/httpd/<ip>',
                      methods=['GET', 'POST'])
@require_login
def http(ip):
    return services_config(request.method, 'apache', request.form, ip,
                           'http.html')
