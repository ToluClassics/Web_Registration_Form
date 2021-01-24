from app import app
from app.form import RegistrationForm
from flask import render_template

@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def index():
    form = RegistrationForm()
    return render_template('index.html',form=form)


