from flask import Blueprint, render_template

irianas_module = Blueprint('servers', __name__, template_folder='templates')


@irianas_module.route('/servers/', methods=['GET', 'POST'])
def servers():
    return render_template('servers.html')
