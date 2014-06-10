---
layout: post
title: "Introduction to Flask (part 3) - Sessions, login_required decorator, debugging"
date: 2013-01-30 13:51
comments: true
categories: tutorials
---
{% raw %}
Continuing on from our last tutorial, we want to protect the hello page because it can be accessed without first logging in. Go ahead and try: Launch the server and navigate your browser to [http://localhost:5000/hello](http://localhost:5000/hello). See - we're not logged in right now but we can still access the hello page.

## **Contents** ##

**Intro to Flask:**

1. Part 1 - Setting Up a Static Site: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-setting-up-a-static-site/) / 
[Video](http://www.youtube.com/watch?v=VsuArvWwuDI)
2. Part 2 - Creating a Login Page: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-creating-a-login-page/) /
[Video](http://www.youtube.com/watch?v=Z7fyAxdL7Uc)
3. => Part 3 - Sessions, Login_required Decorator, Debugging: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/30/introduction-to-flask-sessions-login-required-decorator-debugging/) /
[Video](http://www.youtube.com/watch?v=WCpNvteLCDI)
4. Part 4 - Databases: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-databases/) /
[Video](http://www.youtube.com/watch?v=BkdVq9ag7aw)
5. Part 5 - Deploying to PythonAnywhere [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-deploying/) /
[Video](http://www.youtube.com/watch?v=M4sxSoRZLtI)
6. Part 6 - Task Management Application (FlaskTaskr): [Tutorial](http://www.realpythonfortheweb.com/blog/2013/02/06/introduction-to-flask-web-app/) /
[Video](http://youtu.be/Z86QxnU9BMM)

GitHub Repo: [https://github.com/mjhea0/flask-intro](https://github.com/mjhea0/flask-intro)

## **Goals** ##

To prevent unauthorized access to the hello page, we need to set up sessions as well as a login_required decorator. Sessions store user information client side. I believe it's possible for users to view the information within a session but not modify it without an application key. 

The login_required decorator, meanwhile, checks to make sure that a user is authorized (logged in) before allowing them to view a certain page.

Thus, sessions and login_required decorators work in tandem to protect specific views from unauthorized users.

## **Sessions** ##

Let's start by adding sessions. Add the following code to the `log` function, just below the else statement:

	session['logged_in'] = True

Next create a new view called logout:

	@app.route('/logout')
	def logout():
		session.pop('logged_in', None)
		return redirect(url_for('home'))

When a user is logged in the session key is set to True and the user is still redirected back to the hello page. Then when the user logs out, we use the pop(method) to reset the key to the default value. Pretty cool. 

The updated code for the routes.py file looks like this:

	from flask import *
	
	app = Flask(__name__)
	
	@app.route('/')
	def home():
		return render_template('home.html')
		
	@app.route('/welcome')
	def welcome():
		return render_template('welcome.html')
	
	@app.route('/logout')
	def logout():
		session.pop('logged_in', None)
		return redirect(url_for('show_entries'))
	
	@app.route('/hello')
	def hello():
		return render_template('hello.html')
	
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
		app.run()

Now let's test this out to make sure it works. Fire up that server.

Well, I don't know about you - but I got an "Internal Server Error". This is actually good. Now I can show you how to debug your code. 

Shut down the server, and add `debug=True` to the run function:

	if __name__ == '__main__':
		app.run(debug=True)

Run the server again, and again try to login in. Now you should see the debugger in action. This makes life a lot easier. Oh - but never run this on a production server as it is a security risk.

You should see this error:

	RuntimeError: the session is unavailable because no secret key was set. Set the secret_key on the application to something unique and secret.

Yes, I forgot to set the secret_key. This has to be set for sessions to work properly. Go ahead and add it to the routes.py file:

	app.secret_key = 'my precious'

Just a note: You do not want to make the secret key easy to guess like in this example. There are key generators you can use to completely randomize the key. Let's test it again. Save the routes.py file. If you look at your command-line, you will see that it detected the change in the file and automatically restarted the server:

	* Detected change in 'routes.py', reloading
	* Restarting with reloader

Hit the back button, log in again, and it should work. Then if you go to this url - [http://localhost:5000/logout](http://localhost:5000/logout) - this should log you out and redirect you back to home.html.

Let's actually change this a bit to make it a little more interesting. 

Change the logout() function in the routes.py file:

	@app.route('/logout')
	def logout():
		session.pop('logged_in', None)
		flash('You were logged out')
		return redirect(url_for('log'))

We're going to add message flashing, which is a simple way to give user feedback. I also updated the redirect back to the log.html page. Let's add the flashing response to that page:

	{% extends "template.html" %}
	{% block content %}
	  <h1>Login</h1>
	  {% if error %}
	    <p class=error><strong>Error:</strong> {{ error }}
	  {% endif %}
	  <form action="" method=post>
	    <dl>
	      <dt>Username:
	      <dd><input type=text name=username value="{{
	          request.form.username }}">
	      <dt>Password:
	      <dd><input type=password name=password>
	    </dl>
	    <p><input type=submit value=Login>
	  </form>
	{% for message in get_flashed_messages() %}
		<div class=flash>
			{{ message }}
		</div>
	{% endfor %}
	{% endblock %}

Now when you login and then log back out. You should have been redirected back to the login screen and the following message should have populated: "You were logged out".

Let's add a logout link to the hello page. 

	{% extends "template.html" %}
	{% block content %}
		<h2>Welcome! You are now logged in.</h2>
		<br />
		<br />
		<a href="/logout">Logout</a>
	{% endblock %}

Test it one last time. Perfect.

Now, let's move on to the second half of this tutorial ...

## **Login_required Decorator** ##

Now we still need to prevent unauthorized users from accessing the hello page. To do that we are going to use a decorator to control access to the hello view. 

Start by importing functools within your routes.py file:
	
	from functools import wraps

Now let's setup the actual function:

	def login_required(test):
		@wraps(test)
		def wrap(*args, **kwargs):
			if 'logged_in' in session:
				return test(*args, **kwargs)
			else:
				flash('You need to login first.')
				return redirect(url_for('log'))
		return wrap	

So, this tests to see if `logged_in` is in the session. If it is then we call the method, and if not, the user is redirected back to the login screen with a message stating that a login is required. 

Add the decorator to the hello function:

	@app.route('/hello')
	@login_required
	def hello():
		return render_template('hello.html')

When a GET request is sent to access the hello function it hits the `@login_required` function and the entire function is momentarily replaced (or wrapped) by the wrap function. Then when the user is logged in, the hello() function is invoked, and the user is allowed to access hello.html. If the user is not logged in ... well, you get the idea. 

Make sure to test everything out.

The final routes.py code looks like this:

	from flask import *
	from functools import wraps
	
	app = Flask(__name__)
	
	app.secret_key = 'my precious'
	
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
		return redirect(url_for('log'))
		
	@app.route('/hello')
	@login_required
	def hello():
		return render_template('hello.html')
	
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

## **Conclusion** ##

In this tutorial we did a little bit of housekeeping to keep unauthorized users from accessing the hello.html page. Next time let's add a database to control the users who have access to the hello page. 
{% endraw %}

***

{% youtube WCpNvteLCDI %}