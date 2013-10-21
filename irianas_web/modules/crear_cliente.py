from flask import Blueprint, render_template

irianas_module = Blueprint('crear_client', __name__,
                           template_folder='templates')


@irianas_module.route('/crear_client/', methods=['GET', 'POST'])
def crear_client():
    return render_template('crear_client.html')
