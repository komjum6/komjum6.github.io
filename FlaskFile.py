from flask import Flask, render_template
from flask_frozen import Freezer
from wtforms import Form, BooleanField, StringField, PasswordField, validators
app = Flask(__name__, static_url_path='',static_folder="static")

freezer = Freezer(app)

#De Root Map
@app.route('/')
def index():
    return render_template('index.html')
    
#De plaats waar alles gevisualiseerd word
@app.route('/accomplishments')
def accomplishments():
    return render_template('accomplishments.html')

#De plaats voor contact info
@app.route('/work')
def work():
    return render_template('work.html')

#Een plaats voor een introductie etc
@app.route('/notes')
def notes():
    return render_template('notes.html')
	
#
@app.route('/littleblog')
def littleblog():
    return render_template('littleblog.html')
	
#
@app.route('/gameknowledge')
def gameknowledge():
    return render_template('gameknowledge.html')

#error 500 handling
@app.errorhandler(500)
def internal_error(error):

    return str(error)

#error 404 handling
@app.errorhandler(404)
def page_not_found(error):
    return str(error)

if __name__ == '__main__':
    freezer.freeze()