from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    email = EmailField('email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
