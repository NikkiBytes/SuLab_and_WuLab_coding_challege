# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
from flask import render_template, flash, redirect, request
from app import app
from app.forms import SearchForm
from elasticsearch import Elasticsearch

es = Elasticsearch()

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    
    
    return render_template('search.html', form=form)
