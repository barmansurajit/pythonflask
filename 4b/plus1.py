#!/bin/python

from datetime import datetime
from flask import Flask, render_template, session, g
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)


@app.before_request
def before_request():
	if not 'count' in session:
		session['count'] = 1
	else:
		session['count'] += 1
	g.when = datetime.now().strftime('%H:%M:%S')

@app.route('/')
def index():
	return render_template('index.html', count=session['count'], when=g.when)

@app.route('/other')
def other():
	return render_template('other.html', count=session['count'], when=g.when)

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)