#!/bin/python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[Required(), Length(1, 16)])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name)

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)