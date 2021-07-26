# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
from flask import render_template, flash, redirect, request
from app import app
from app.forms import SearchForm


@app.route('/',  methods=['GET', 'POST'])
#@app.route('/index')
#@app.route('/search', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template('search.html', form=form)

    #if form.validate_on_submit():
     #   flash('Login requested for user {}, remember_me={}'.format(
      #      form.username.data, form.remember_me.data))
        #return redirect('/index')
#@app.route('/index')
"""def index()
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
"""