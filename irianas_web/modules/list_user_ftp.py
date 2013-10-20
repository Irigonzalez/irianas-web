from flask import Blueprint, render_template

irianas_module = Blueprint('list_user_ftp', __name__,
                           template_folder='templates')


@irianas_module.route('/list_user_ftp/', methods=['GET', 'POST'])
def list_user_ftp():
    return render_template('list_user_ftp.html')
