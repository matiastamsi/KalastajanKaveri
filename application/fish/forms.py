from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, BooleanField, validators

class FishForm(FlaskForm):

    name = StringField('Species', [validators.InputRequired()])
    minimum_catch_size = DecimalField('Minimum size to keep',
                                      [validators.NumberRange(min=0.0, max=150.0)])
    closed_season_starts_day = IntegerField('Closed season starts: Day',
                                            [validators.NumberRange(min=1, max=31)])
    closed_season_starts_month = IntegerField("Month",
                                              [validators.NumberRange(min=1, max=12)])
    closed_season_ends_day = IntegerField("Closed season ends: Day",
                                          [validators.NumberRange(min=1, max=31)])
    closed_season_ends_month = IntegerField("Month",
                                            [validators.NumberRange(min=1, max=12)])
    #Boolean value to message whether
    #the fish species is going to be deleted.
    delete = BooleanField("I agree deleting this species permanently.")

    class Meta:
        csrf = False
