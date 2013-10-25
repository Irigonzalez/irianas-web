from flask import Blueprint, render_template

irianas_module = Blueprint('create_client', __name__,
                           template_folder='templates')


@irianas_module.route('/client/add', methods=['GET', 'POST'])
def create_client():
    return render_template('crear_client.html')
