from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    species = StringField(label='Species', validators=[DataRequired()])
    breed = StringField(label='Breed', validators=[DataRequired()])
    submit = SubmitField(label='Save')
