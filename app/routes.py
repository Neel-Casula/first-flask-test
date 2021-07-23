from app import app
from flask import Flask,render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Neel'} 
    return render_template('test.html', user=user) 
@app.route('/test') 
def test(): 
    user = {'username': 'Neel'} 
    return render_template('test.html', user=user) 
@app.route('/test2') 
def test2(): 
    user = {'username': 'Neel'} 
    sample_data = [ 
        { 
            'author': {'username': 'Neel'}, 
            'body': 'Hello!' 
        }, { 
            'author': {'username': 'Neel'}, 
            'body': 'Welcome to Flask!' 
        } 
    ] 
    return render_template('test2.html', user=user, sample_data=sample_data) 



