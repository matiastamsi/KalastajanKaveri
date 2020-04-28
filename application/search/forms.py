from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField
  
class SearchForm(FlaskForm):
    species = SelectField()
    lure_or_fly = SelectField()
    spot = SelectField()
    day = SelectField()
    month = SelectField()
    year = SelectField()
    weight = BooleanField()
    length = BooleanField()
    
    class Meta:
        csrf = False
