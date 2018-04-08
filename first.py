from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route('/', methods = ['GET', 'POST'])
def login_form_main():

	error = None
	if request.method == "POST":
		if request.form['username'] != 'admin' or request.form['password'] != 'admin' :
			error = "Invalid Credentials. Please Try Again"
		else:
			return redirect(url_for('login_status'))


	return render_template("index.html", error = error)

@app.route('/status')
def login_status():
	return render_template('home.html')

@app.route('/test', methods = ['GET', 'POST'])
def login_form_test():

	error = None

	if request.method == 'POST': 
		name_info = request.form['username']
		return redirect(url_for('print_info', uname = name_info))
		#return redirect(url_for('print_info', uname_alter = name_info))

	return render_template('index.html', error = error)

@app.route('/test/info/', methods = ['GET', 'POST'])
def print_info():
	u_name = request.args.get('uname')
	return render_template('print.html', u__name = u_name)

@app.route('test/info/alternative/<uname_alter>', methods = ['GET', 'POST'])
def print_info_alter(uname_alter):
	u_name_alter = uname_alter
	return render_template('print.html', u__name = u_name_alter)

if __name__ == __main__:
	app.run(debug = True,  port = 5000)

