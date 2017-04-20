''' DESCRIPTION: Contains the content of your application 

	             The following sample (main.py) is a basic Flask-based application 
                 that also makes use of a simple error handler.
'''

import logging

from flask import Flask, render_template, request

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
app = Flask(__name__)


@app.route('/') # decorator to map the root URL ('/') to a simple request handler
def hello():
    '''Return a friendly HTTP greeting.'''
    return 'Hello World 2!'

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template('submitted_form.html', name=name, email=email, site=site, comments=comments)

@app.errorhandler(404)
def page_not_found(e):
    '''Return a custom 404 error.'''
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    # Log the error and stacktrace.
    # logging.exception('An error occurred during a request.')
    return 'Sorry, unexpected error: {}'.format(e), 500