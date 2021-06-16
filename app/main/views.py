from flask import render_template
from . import main


#views

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    header = "PIZZA"
    return render_template('index.html', header=header)

