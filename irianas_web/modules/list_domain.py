from flask import Blueprint, render_template

irianas_module = Blueprint('list_domain', __name__,
                           template_folder='templates')


@irianas_module.route('/list_domain/', methods=['GET', 'POST'])
def list_domain():
    return render_template('list_domain.html')
