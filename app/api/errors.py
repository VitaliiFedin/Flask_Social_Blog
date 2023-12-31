from flask import jsonify


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401


def bad_request(message):
    response = jsonify({'error': 'bad request', 'message': message})
