from flask_wtf import FlaskForm
from wtforms import StringField

class ContactForm(FlaskForm):

    submit = SubmitField('Do this')
    submit2 = SubmitField('Do that')