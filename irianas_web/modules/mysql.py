from flask import Blueprint, request
from irianas_web.core import require_login, services_config

irianas_module = Blueprint('mysql', __name__, template_folder='templates')


@irianas_module.route('/client/services/config/mysql/<ip>',
                      methods=['GET', 'POST'])
@require_login
def mysql(ip):
    return services_config(request.method, 'mysql', request.form, ip,
                           'mysql.html')
