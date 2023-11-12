from app import app
from flask import render_template
from scraper import scrape_cf
@app.route('/')
def base():
    return render_template('index.html')

@app.route('/home')
def home():
    return 'This is the homepage'

@app.route('/learn')
def learn():
    return "this is the learn page"

@app.route('/compete')
def compete():
    return 'compete'

@app.route('/compete/cfs')
def cfs():
    return 'Codeforces data is to be displayed here (we are gonna display the upcoming contests and some of the upcoming contests)'
