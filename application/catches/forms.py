from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, validators

class CatchForm(FlaskForm):
    species = StringField("Species") #Lisätään myöhemmin validointi joka viittaa kalalajitauluun
    lure_or_fly = SelectField("Lure or Fly", choices=[('lure', 'Lure'), ('fly', 'Fly')])
    length = DecimalField("Length", [validators.NumberRange(min=0.1, max=500.0)], places=2)
    weight = DecimalField("Weight", [validators.NumberRange(min=0.1, max=50.0)], places=2)
    spot = StringField("Spot") #Lisätään myöhemmin validointi joka viittaa kalapaikkatauluun
    description = StringField("Description", [validators.Length(min=3, max=100)])
    private_or_public = SelectField("Private or public", choices=[('private', 'Private'),('public', 'Public')])

    class Meta:
        csrf = False
