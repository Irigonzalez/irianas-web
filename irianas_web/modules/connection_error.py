from flask import Blueprint, render_template

irianas_module = Blueprint('connection_error', __name__,
                           template_folder='templates')


@irianas_module.route('/error/connection', methods=['GET', 'POST'])
def connection_error():
    return render_template('connection_error.html',
                           msg='Error con la conexi&oacute;n al servidor.')
