from flask import Flask,request,abort,jsonify
import functools
import os

app = Flask(__name__)

def login_required(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        header = request.headers.get('Authorization')

        if header is None:
            abort(401)

        auth_type, token = header.split()

        if auth_type != 'Bearer':
            abort(401)
        if token != os.getenv('SAMPLE_API_TOKEN'):
            abort(401)

        return method(*args, **kwargs)
    return wrapper

@app.errorhandler(401)
def error_handler(error):
    response = jsonify({})
    response.headers['WWW-Authenticate'] = 'Bearer realm="example"'
    return response, error.code

@app.route('/')
def index():
    response = jsonify({'message' : 'Hello World!'})
    return response, 200

@app.route('/token_auth')
@login_required
def tokenAuthApi():
    response = jsonify({'message' : 'Token Authorization Sample.'})
    response.headers['WWW-Authenticate'] = 'Bearer realm=""'
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)