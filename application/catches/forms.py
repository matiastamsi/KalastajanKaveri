from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, BooleanField, validators

class CatchForm(FlaskForm):
    species = StringField("Species")
    lure_or_fly = SelectField("Lure or Fly", choices=[('lure', 'Lure'), ('fly', 'Fly')], default='lure')
    length = DecimalField("Length", [validators.NumberRange(min=0.1, max=500.0)], places=2)
    weight = DecimalField("Weight", [validators.NumberRange(min=0.1, max=50.0)], places=2)
    spot = StringField("Spot")
    description = StringField("Description", [validators.Length(min=3, max=100)])
    private_or_public = SelectField("Private or public", choices=[('private', 'Private'),('public', 'Public')], default='private')

    delete = BooleanField("I agree deleting this catch permanently.")

    def change_choice(self, newChoice):
        self.lure_or_fly.default = newChoice
        self.process()

    def change_privacy(self, newValue):
        self.private_or_public.default = newValue
        self.process()

    class Meta:
        csrf = False
