from flask import Blueprint, render_template

irianas_module = Blueprint('user_ftp', __name__, template_folder='templates')


@irianas_module.route('/user_ftp/', methods=['GET', 'POST'])
def user_ftp():
    return render_template('user_ftp.html')
