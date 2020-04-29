from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField
  
class SearchForm(FlaskForm):
    species = SelectField()
    spot = SelectField()
    orderBySize = BooleanField()
    
    class Meta:
        csrf = False
