from flask import Flask, render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators
app = Flask(__name__, static_url_path='',static_folder="WiWebSite")

webcode = open('index.html').read()
registerfile = open('register.html').read()

@app.route('/')
def webprint():
    return webcode

#Hier is een experimentele aanpak


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return registerfile

#Hier eindigt de experimentele aanpak

if __name__ == "__FlaskFile__":
    app.run(debug=False)

"""    
set FLASK_APP=FlaskFile.py
py -m flask run

url_for('static', filename='style.css')

name=None
render_template("WiWebSite.html", name=name)



return render_template('register.html', form=form)
"""