from flask import Blueprint, render_template

irianas_module = Blueprint('mysql', __name__, template_folder='templates')


@irianas_module.route('/mysql/', methods=['GET', 'POST'])
def mysql():
    return render_template('mysql.html')
