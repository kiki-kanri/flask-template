from flask import Blueprint


api = Blueprint('example', __name__, url_prefix = '/example')


@api.get('')
def hello_world():
    return 'Hello, World!'
