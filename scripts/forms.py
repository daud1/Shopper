from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms import PasswordField
from wtforms.validators import InputRequired, AnyOf

class LoginForm(FlaskForm):
    username = TextField('Username', validators=[InputRequired(), AnyOf(['admin'], message='Enter a valid username')])
    password = PasswordField('Password', validators=[InputRequired(), AnyOf(['password'], message='Enter a valid password')])