''' DESCRIPTION: Contains the content of your application 

	The following sample (main.py) is a basic Flask-based "Hello World!" 
	application that also makes use of a simple error handler
'''

import logging

from flask import Flask, render_template, request


app = Flask(__name__)


# @app.route('/') # decorator to map the root URL ('/') to a simple request handler
# def hello():
#     return 'Hello World!'

@app.route('/')
def form():
	return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template('submitted_form.html', name=name, email=email, site=site, comments=comments)

@app.errorhandler(500)  # simple error handler
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500