#!/bin/python

import os, imghdr
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
bootstrap = Bootstrap(app)

class UploadForm(FlaskForm):
	image_file = FileField('Image file')
	submit = SubmitField('Submit')

	"""docstring for UploadForm"""
	def validate_image_file(self, field):
		if field.data.filename[-4:].lower() != '.jpg':
			raise ValidationError('Invalid file extension, only jpeg allowed')
		if imghdr.what(field.data) != 'jpeg':
			raise ValidationError('Invalid image format')

@app.route('/', methods=['GET', 'POST'])
def index():
	image = None
	form = UploadForm()
	if form.validate_on_submit():
		image = 'uploads/' + form.image_file.data.filename
		form.image_file.data.save(os.path.join(app.static_folder, image))
	return render_template('index.html', form=form, image=image)

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)