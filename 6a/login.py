#!/bin/python

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_auth.db'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), index=True, unique=True)
	password_hash = db.Column(db.String(64))
	
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(password)

	@staticmethod
	def register(username, password):
		user = User(username=username)
		user.set_password(password)
		db.session.add(user)
		db.session.commit()
		return user

	def __repr__(self):
		return '<User {0}>'.format(self.username)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	new = False
	form = NameForm()

	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		if User.query.filter_by(name=name).first() is None:
			db.session.add(User(name=name))
			db.session.commit()
			new = True
	return render_template('index.html', form=form, name=name, new=new)

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)