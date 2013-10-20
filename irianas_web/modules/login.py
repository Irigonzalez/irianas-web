from flask import Blueprint, render_template

irianas_module = Blueprint('login', __name__, template_folder='templates')


@irianas_module.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
