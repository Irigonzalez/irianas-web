#!/usr/bin/env python
""":mod:`irianas_web.main` -- Program entry point
"""
from flask import Flask
from modules.login import irianas_module as login
from modules.home import irianas_module as home
from modules.clients import irianas_module as clients
from modules.http import irianas_module as http
from modules.ftp import irianas_module as ftp
from modules.dns import irianas_module as dns
from modules.mysql import irianas_module as mysql
from modules.servers import irianas_module as servers
from modules.client import irianas_module as client
from modules.list_user_ftp import irianas_module as list_user_ftp
from modules.user_ftp import irianas_module as user_ftp
from modules.cambio_password_ftp import irianas_module as cambio_password_ftp
from modules.crear_virtual import irianas_module as crear_virtual
from modules.list_domain import irianas_module as list_domain
from modules.crear_cliente import irianas_module as crear_cliente
from modules.crear_user import irianas_module as crear_user

app = Flask(__name__)
app.register_blueprint(login)
app.register_blueprint(home)
app.register_blueprint(clients)
app.register_blueprint(http)
app.register_blueprint(ftp)
app.register_blueprint(dns)
app.register_blueprint(mysql)
app.register_blueprint(servers)
app.register_blueprint(client)
app.register_blueprint(list_user_ftp)
app.register_blueprint(user_ftp)
app.register_blueprint(cambio_password_ftp)
app.register_blueprint(crear_virtual)
app.register_blueprint(list_domain)
app.register_blueprint(crear_cliente)
app.register_blueprint(crear_user)

if __name__ == '__main__':
    app.run(debug=True)
