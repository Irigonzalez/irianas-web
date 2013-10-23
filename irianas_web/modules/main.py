from flask import (Flask, Blueprint)

blue = Blueprint('blue', _name_)


@blue.route('/Home/')
def main():
    return Home


app.register_blueprint(blue)
app.run(debug=True)
