#!/bin/python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
	'August', 'September', 'October', 'November', 'December']

	weather = {
	'January':{'min': 38, 'max': 47, 'rain': 6.14},
	'February':{'min': 38, 'max': 51, 'rain': 4.14},
	'March':{'min': 41, 'max': 56, 'rain': 4.5},
	'April':{'min': 38, 'max': 70, 'rain': 6.14},
	'May':{'min': 39, 'max': 80, 'rain': 6.14},
	'June':{'min': 67, 'max': 90, 'rain': 6.14},
	'July':{'min': 38, 'max': 47, 'rain': 6.14},
	'August':{'min': 38, 'max': 47, 'rain': 6.14},
	'September':{'min': 38, 'max': 47, 'rain': 6.14},
	'October':{'min': 38, 'max': 47, 'rain': 6.14},
	'November':{'min': 38, 'max': 47, 'rain': 6.14},
	'December':{'min': 38, 'max': 47, 'rain': 6.14}
	}
	highlight = {'min': 35, 'max':80, 'rain':5}
	return render_template('index.html', city='Fort Worth, TX', months=months, weather=weather, highlight=highlight)

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)