from flask import Blueprint, render_template

irianas_module = Blueprint('clients', __name__, template_folder='templates')


@irianas_module.route('/clients/', methods=['GET', 'POST'])
def clients():
    return render_template('clients.html')
