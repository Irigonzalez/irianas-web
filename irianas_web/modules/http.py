from flask import Blueprint, render_template

irianas_module = Blueprint('http', __name__, template_folder='templates')


@irianas_module.route('/http/', methods=['GET', 'POST'])
def http():
    return render_template('http.html')
