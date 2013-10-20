from flask import Blueprint, render_template

irianas_module = Blueprint('client', __name__, template_folder='templates')


@irianas_module.route('/client/', methods=['GET', 'POST'])
def client():
    return render_template('client.html')
