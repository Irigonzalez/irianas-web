from flask import (Blueprint, render_template)
from irianas_web.core import require_login

irianas_module = Blueprint('home', __name__, template_folder='templates')

values = dict(host_name='node.master',
              ip_address='192.167.10.2',
              opera_system='CentOS6',
              arch='64bits',
              processor='Intel i5',
              memory_ram='4 Gb')


@require_login
@irianas_module.route('/home/')
@irianas_module.route('/')
@irianas_module.route('/index/')
def home():
    return render_template('home.html', values=values)
