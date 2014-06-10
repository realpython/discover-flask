---
layout: post
title: "Introduction to Flask (part 4) - databases"
date: 2013-01-31 10:20
comments: true
categories: tutorials
---
{% raw %}
Last time we implemented a number of security features to prevent users from accessing the restricted page hello.html. In this final tutorial before deployment I'll show you the basics of working with SQLite from Flask.

## **Goals** ##

The first time you work with a database in Flask it can be somewhat confusing, especially if you're working from the Flaskr tutorial. So, I want to show you one of the simplest approaches for implementing a database. We will simply query a database from the hello() function and then display the results on the hello.html page.

## **Contents** ##

**Intro to Flask:**

1. Part 1 - Setting Up a Static Site: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-setting-up-a-static-site/) / 
[Video](http://www.youtube.com/watch?v=VsuArvWwuDI)
2. Part 2 - Creating a Login Page: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-creating-a-login-page/) /
[Video](http://www.youtube.com/watch?v=Z7fyAxdL7Uc)
3. Part 3 - Sessions, Login_required Decorator, Debugging: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/30/introduction-to-flask-sessions-login-required-decorator-debugging/) /
[Video](http://www.youtube.com/watch?v=WCpNvteLCDI)
4. => Part 4 - Databases: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-databases/) /
[Video](http://www.youtube.com/watch?v=BkdVq9ag7aw)
5. Part 5 - Deploying to PythonAnywhere [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-deploying/) /
[Video](http://www.youtube.com/watch?v=M4sxSoRZLtI)
6. Part 6 - Task Management Application (FlaskTaskr): [Tutorial](http://www.realpythonfortheweb.com/blog/2013/02/06/introduction-to-flask-web-app/) /
[Video](http://youtu.be/Z86QxnU9BMM)

GitHub Repo: [https://github.com/mjhea0/flask-intro](https://github.com/mjhea0/flask-intro)

## **Requirements** ##

I assume you already have some SQLite knowledge so go ahead and create a database called "sales". Within that database create a table called "reps" with the fields "rep_name" (TEXT) and "amount" (INT).

Put in ten rows of data. 

If you need help please see the video below.

## **Routes** ##

Let's make some changes to the routes.py file so that we can access the database and then query the database. 

	import sqlite3

Import the sqlite3 library. 

	DATABASE = 'sales.db'

Define the database.

	app.config.from_object(__name__)

The `from_object` looks at the config information (e.g., DATABASE) and imports the variables. It's a good idea to use a separate file to store your configuration information.

	def connect_db():
    	return sqlite3.connect(app.config['DATABASE'])

This method allows us to easily connect to the database when ready.

	@app.route('/hello')
	@login_required
	def hello():
		g.db  = connect_db()
		cur = g.db.execute('select rep_name, amount from reps')
		sales = [dict(rep_name=row[0], amount=row[1]) for row in cur.fetchall()]
		g.db.close()
		return render_template('hello.html', sales=sales)
	
The hello() function connects to the database, executes the SELECT statement to query the database, returns the data in a dictionary assigned to a variable name, closes the database, renders the template and passes the variable to the template. Much of this can be broken up into separate functions to make your code a bit more readable.

The final code looks like this:

	from flask import *
	from functools import wraps
	import sqlite3
	
	DATABASE = 'sales.db'
	
	app = Flask(__name__)
	app.config.from_object(__name__)
	
	app.secret_key = 'my precious'
	
	def connect_db():
		return sqlite3.connect(app.config['DATABASE'])
	
	@app.route('/')
	def home():
		return render_template('home.html')
		
	@app.route('/welcome')
	def welcome():
		return render_template('welcome.html')
	
	def login_required(test):
		@wraps(test)
		def wrap(*args, **kwargs):
			if 'logged_in' in session:
				return test(*args, **kwargs)
			else:
				flash('You need to login first.')
				return redirect(url_for('log'))
		return wrap	
	
	@app.route('/logout')
	def logout():
		session.pop('logged_in', None)
		flash('You were logged out')
		return redirect (url_for('log'))
	
	@app.route('/hello')
	@login_required
	def hello():
		g.db  = connect_db()
		cur = g.db.execute('select rep_name, amount from reps')
		sales = [dict(rep_name=row[0], amount=row[1]) for row in cur.fetchall()]
		g.db.close()
		return render_template('hello.html', sales=sales)
	
	@app.route('/log', methods=['GET', 'POST'])
	def log():
	    error = None
	    if request.method == 'POST':
	        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
	            error = 'Invalid Credentials. Please try again.'
	        else:
				session['logged_in'] = True
				return redirect(url_for('hello'))
	    return render_template('log.html', error=error)
			
	if __name__ == '__main__':
		app.run(debug=True)

## **Hello** ##

Update the hello.html view:

	{% extends "template.html" %}
	{% block content %}
	    <h2>Welcome! You are now logged in.</h2>
	    <a href="/logout">Logout</a>
	    <br />
	    <br />
	    <h3>Sales Data - Region 1:</h3>
	    {% for item in sales %}
	    {{ item.rep_name }} | {{ item.amount }} <br \>
	{% endfor %}
	{% endblock %}

The new code works similar to a for loop in Python to iterate through each item in the dictionary. 

Test this out. 

You should now see the following output on the hello.html page:

	John | 22000 
	Derek | 25000 
	Lily | 28000 
	Josh | 20000 
	Kevin | 29000 
	Kim | 18000 
	Ryan | 25000 
	Henry | 25000 
	Brian | 19000 
	Kelly | 29000

## **Conclusion** ##

That's it. All done. Can you believe it? So we used Flask to create a basic website, housing static pages. Then we added dynamic content for logging users in and out and displaying data extracted from SQLite. Along the way, I hope that you grasped the basics of how to build a simple Flask application. If you haven't already, I would highly recommend building the demo Flask app on the Flask site, called Flaskr. 

As far as our app goes, it may not look pretty, but in the end, you gained the fundamentals - and that's what matters. If you want you could easily add additional functionally, clean the site up a bit and develop the basis for a bigger application. Perhaps a mini sales database that can be queried, for example. Add some additional components. Think about your goals. Build. Hit hurdles. And then build some more. 

Oh - and next time we'll be deploying this application to a production server. Get excited. 
{% endraw %}

***

{% youtube BkdVq9ag7aw %}





