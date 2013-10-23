from flask import Blueprint, render_template

irianas_module = Blueprint('crear_user', __name__,
                           template_folder='templates')


@irianas_module.route('/crear_user/', methods=['GET', 'POST'])
def crear_user():
    return render_template('crear_user.html')
