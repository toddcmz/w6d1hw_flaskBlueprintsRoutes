from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    first_name = StringField('first_name', validators =[DataRequired()])
    last_name = StringField('last_name', validators =[DataRequired()])
    fav_book = StringField('fav_book')
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')