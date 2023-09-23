#!/usr/bin/env python3

import os

from flask import Flask, request, current_app, g, make_response, redirect, abort

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

@app.route('/reginald-kenneth-dwight')
def redirect_example():
    # Redirect to the specified URL
    return redirect('https://www.names.com/elton-john')

@app.route('/<stage_name>')
def get_name(stage_name):
    # In this example, we simulate a database query
    # If the stage name exists, return a response; otherwise, abort with a 404 status code
    if stage_name == 'elton-john':
        return make_response(f'<h1>{stage_name} is an existing stage name!</h1>')
    else:
        abort(404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
