from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def me():

	error = None
	if request.method == "POST":
		if request.form['username'] != 'admin' or request.form['password'] != 'admin' :
			error = "Invalid Credentials. Please Try Again"
		else:
			return redirect(url_for('hom'))


	return render_template("index.html", error = error)

@app.route('/home')
def hom():
	return render_template('home.html')