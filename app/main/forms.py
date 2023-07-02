from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What\'s your name', validators=[DataRequired()])
    submit = SubmitField('Submit')