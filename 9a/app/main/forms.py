from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length


class LoginForm(FlaskForm):
	username = StringField('Username', validators=[Required(), Length(1, 16)])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Remember me')
	submit = SubmitField('Submit')