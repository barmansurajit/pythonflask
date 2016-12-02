#!/bin/python

from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)


@app.route('/')
def index():
	if 'count' not in session:
		session['count'] = 1
	else:
		session['count'] += 1
	return render_template('index.html', count=session['count'])

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)