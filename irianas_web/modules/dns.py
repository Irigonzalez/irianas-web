from flask import Blueprint, render_template

irianas_module = Blueprint('dns', __name__, template_folder='templates')


@irianas_module.route('/dns/', methods=['GET', 'POST'])
def dns():
    return render_template('dns.html')
