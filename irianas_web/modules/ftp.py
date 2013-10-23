from flask import Blueprint, render_template

irianas_module = Blueprint('ftp', __name__, template_folder='templates')


@irianas_module.route('/ftp/', methods=['GET', 'POST'])
def ftp():
    return render_template('ftp.html')
