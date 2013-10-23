from flask import Blueprint, render_template

irianas_module = Blueprint('crear_virtual', __name__,
                           template_folder='templates')


@irianas_module.route('/crear_virtual/', methods=['GET', 'POST'])
def crear_virtual():
    return render_template('crear_virtual.html')
