from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class SignUpForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2)])
    username = StringField('Username', [validators.Length(min=8)])
    password = PasswordField('New Password', [validators.Length(min=10), validators.EqualTo('confirm')])
    confirm  = PasswordField('Repeat Password')

    class Meta:
        csrf = False

