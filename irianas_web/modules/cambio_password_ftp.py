from flask import Blueprint, render_template

irianas_module = Blueprint('cambio_password_ftp', __name__,
                           template_folder='templates')


@irianas_module.route('/cambio_password_ftp/', methods=['GET', 'POST'])
def cambio_password_ftp():
    return render_template('cambio_password_ftp.html')
