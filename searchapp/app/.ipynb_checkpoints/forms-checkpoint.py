from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searchID=StringField('query id: ')#, validators=[DataRequired()])
    submitID = SubmitField('search')
    searchText=StringField('query text: ')#, validators=[DataRequired()])
    submitText = SubmitField('search')