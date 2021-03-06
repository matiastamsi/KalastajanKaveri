from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, BooleanField

class SignUpForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=20)])
    username = StringField('Username', [validators.Length(min=8, max=20)])
    password = PasswordField('New Password', [validators.Length(min=10), validators.EqualTo('confirm')])
    confirm  = PasswordField('Repeat Password')
    #Boolean value to message whether
    #the account is going to be deleted.
    delete = BooleanField()

    class Meta:
        csrf = False

