from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searchquery=StringField('query: ')#, validators=[DataRequired()])
    submit = SubmitField('search')
