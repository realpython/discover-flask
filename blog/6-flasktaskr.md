---
layout: post
title: "Introduction to Flask (Part 6) - Task Management Application (FlaskTaskr)"
date: 2013-02-06 08:36
comments: true
categories: tutorials
---

{% raw %}
Well, I just couldn't help myself. I couldn't leave the app in disarray. Let's create something useful. Something that actually works. 

How about a task manager. We could call it FlaskTaskr.

This application has the following functionality:

1. Users sign in and out from the landing page, which us managed by sessions. For now, only one user is supported.
2. Once signed in, users can add new tasks. Each task consists of a name, due date, priority, status, and an auto-incremented ID. 
3. Users can view all uncompleted tasks from the same screen.
4. Users can also delete tasks and mark tasks as completed. If a user deletes a task, it will also be deleted from the database.

## **Contents** ##


**Intro to Flask:**

1. Part 1 - Setting Up a Static Site: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-setting-up-a-static-site/) / 
[Video](http://www.youtube.com/watch?v=VsuArvWwuDI)
2. Part 2 - Creating a Login Page: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/29/flask-tutorial-creating-a-login-page/) /
[Video](http://www.youtube.com/watch?v=Z7fyAxdL7Uc)
3. Part 3 - Sessions, Login_required Decorator, Debugging: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/30/introduction-to-flask-sessions-login-required-decorator-debugging/) /
[Video](http://www.youtube.com/watch?v=WCpNvteLCDI)
4. Part 4 - Databases: [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-databases/) /
[Video](http://www.youtube.com/watch?v=BkdVq9ag7aw)
5. Part 5 - Deploying to PythonAnywhere [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-deploying/) /
[Video](http://www.youtube.com/watch?v=M4sxSoRZLtI)
6. => Part 6 - Task Management Application (FlaskTaskr): [Tutorial](http://www.realpythonfortheweb.com/blog/2013/02/06/introduction-to-flask-web-app/) /
[Video](http://youtu.be/Z86QxnU9BMM)

GitHub Repo: [https://github.com/mjhea0/flask-intro](https://github.com/mjhea0/flask-intro)


## **Database** ##

First, we need to create a new database. Based on the info above, we need one table, consisting of these fields - task_id, name, due_date, priority, status. Status will either be 1 or 0; 1 of the task is still open and 0 if closed. 

So, let's code the file to create the table and populate it with some dummy data:

    import sqlite3

	con = sqlite3.connect("flasktask.db")

	with con:
    	cur = con.cursor()
    	cur.execute("DROP TABLE IF EXISTS ftasks")
    	cur.execute("CREATE TABLE ftasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)")
    	cur.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish this tutorial", "02/03/2013", 10, 1)')
    	cur.execute('INSERT INTO ftasks (name, due_date, priority, status) VALUES("Finish my book", "02/03/2013", 10, 1)')

	con.close()

Save the file as database.py and run. 

## **Routes** ##

Now let's make some quick changes in routes.py.

Update the name of the database:

    flasktask.db

Remove both the home() and welcome() functions and change the routing url for the log() function to the main directory - `('/')` - and update the return url to `tasks` when the user logs in correctly.

Change the hello() function to match the following code:

    @app.route('/tasks')
    @login_required
    def tasks():
	    g.db  = connect_db()
	    g.db.close()
	    return render_template('tasks.html')

This is the updated code for routes.py for now:

    from flask import *
    from functools import wraps
    import sqlite3

    DATABASE = 'flasktask.db'

    app = Flask(__name__)
    app.config.from_object(__name__)

    app.secret_key = 'my precious'

    def connect_db():
	    return sqlite3.connect(app.config['DATABASE'])

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

    @app.route('/tasks')
    @login_required
    def tasks():
	    g.db  = connect_db()
	    g.db.close()
	    return render_template('tasks.html')

    @app.route('/', methods=['GET', 'POST'])
    def log():
    error = None
        if request.method == 'POST':
            if request.form['username'] != 'admin' or request.form['password'] != 'admin':
                error = 'Invalid Credentials. Please try again.'
            else:
			    session['logged_in'] = True
			    return redirect(url_for('tasks'))
        return render_template('log.html', error=error)
    
    @app.before_request
    def before_request():
        g.db = connect_db()
		
    if __name__ == '__main__':
	    app.run(debug=True)

## **Views and Templates** ##

Save a new copy of the hello.html page as tasks.html.

Create a style.css sheet, consisting of the code below, and save it to the CSS folder:

    body            { font-family: sans-serif; background: #eee; }
	a, h1, h2       { color: #377BA8; }
	h1, h2          { font-family: 'Georgia', serif; margin: 0; }
	h1              { border-bottom: 2px solid #eee; }
	h2              { font-size: 1.5em; }

	.page           { margin: 2em auto; width: 50em; border: 5px solid #ccc;
                  padding: 0.8em; background: white; }
	.entries        { list-style: none; margin: 0; padding: 0; }
	.entries li     { margin: 0.8em 1.2em; }
	.entries li h2  { margin-left: -1em; }
	.add-task     	{ font-size: 0.9em; border-bottom: 1px solid #ccc; }
	.add-task dl   	{ font-weight: bold; }
	.metanav        { text-align: right; font-size: 0.8em; padding: 0.3em;
                  margin-bottom: 1em; background: #fafafa; }
	.flash          { background: #CEE5F5; padding: 0.5em;
                  border: 1px solid #AACBE2; }
	.error          { background: #F0D6D6; padding: 0.5em; }

	.datagrid table { border-collapse: collapse; text-align: left; width: 100%; } 
	.datagrid {background: #fff; overflow: hidden; border: 1px solid #000000; -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; }
	.datagrid table td, .datagrid table th { padding: 3px 10px; }
	.datagrid table thead th {background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #000000), color-stop(1, #000000) );background:-moz-linear-gradient( center top, #000000 5%, #000000 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#000000', endColorstr='#000000');background-color:#000000; color:#FFFFFF; font-size: 15px; font-weight: bold; } 
	.datagrid table thead th:first-child { border: none; }.datagrid table tbody td { color: #000000; border-left: 1px solid #E1EEF4;font-size: 12px;font-weight: normal; }
	.datagrid table tbody .alt td { background: #E1EEF4; color: #000000; }
	.datagrid table tbody td:first-child { border-left: none; }
	.datagrid table tbody tr:last-child td { border-bottom: none; }

	.button {
		background-color:#000;
		display:inline-block;
		color:#ffffff;
		font-size:13px;
		padding:3px 12px;
		margin: 0;
		text-decoration:none;
		position:relative;
	}
    
Now go ahead and change the template.html file as follows:

	<!DOCTYPE html>
	<html>
	  <head>
	    <title>FlaskTaskr</title>
	    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap.css') }}">
	    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
	  </head>
	  <body>
	  	<br/>
	    <div class="container">
	   	  {% for message in get_flashed_messages() %}
    	  <div class=flash>{{ message }}</div>
  		  {% endfor %}
	      {% block content %}
	      {% endblock %}
	    </div>
	  </body>
	</html>

Then you can drop the flashed messages from the log.html file. 

## **Routes** ##

Update the tasks() function again within the routes.py file:

    @app.route('/tasks')
	@login_required
	def tasks():
    	g.db  = connect_db()
    	cur = g.db.execute('select name, due_date, priority, task_id from ftasks where status=1')
    	open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    	cur = g.db.execute('select name, due_date, priority, task_id from ftasks where status=0')
    	closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    	g.db.close()
    	return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks)

As you can tell, we are querying the database for open and closed tasks, saving the results, and then passing the two variables `open_tasks` and `closed tasks` to the tasks.html page. This is used to populate the completed and uncompleted task lists.

Next, we need to add the ability to add new tasks, complete tasks, and delete tasks.

Beginning with adding new tasks:

    @app.route('/add', methods=['POST'])
	@login_required
	def new_task():
    	name = request.form['name']
    	date = request.form['due_date']
    	priority = request.form['priority']
    	if not name and not date and not priority:
        	flash("You forgot the task name, date, and priority! Try again.")
        	return redirect(url_for('tasks'))
    	elif not name and not date:
        	flash("You forgot the task name and date! Try again.")
        	return redirect(url_for('tasks'))
    	elif not date and not priority:
        	flash("You forgot the task date and priority! Try again.")
        	return redirect(url_for('tasks'))
    	elif not name and not priority:
        	flash("You forgot the task name and priority! Try again.")
        	return redirect(url_for('tasks'))   
    	elif not name:
        	flash("You forgot the task name! Try again.")
        	return redirect(url_for('tasks'))
    	elif not date:
        	flash("You forgot the task date! Try again.")
        	return redirect(url_for('tasks'))
    	elif not priority:
        	flash("You forgot the task priority! Try again.")
        	return redirect(url_for('tasks'))    
    	else:
        	g.db.execute('insert into ftasks (name, due_date, priority, status) values (?, ?, ?, 1)',
                 [request.form['name'], request.form['due_date'], request.form['priority']])                 
        	g.db.commit()
        	flash('New entry was successfully posted')
        	return redirect(url_for('tasks'))
            
First we have to go through a series of error checking to make sure all required information is populated, then we add the new data to the database. There is a simpler means of going through the error checking which I'll show you in an upcoming video.

Add the ability to delete tasks:

    @app.route('/delete/<int:task_id>',)
	@login_required
	def delete_entry(task_id):
    	g.db  = connect_db()
    	cur = g.db.execute('delete from ftasks where task_id='+str(task_id))
    	g.db.commit()
    	g.db.close()
    	flash('The task was deleted')
    	return redirect(url_for('tasks'))

And to mark tasks as complete:

    @app.route('/complete/<int:task_id>',)
	@login_required
		def complete(task_id):
    	g.db  = connect_db()
    	cur = g.db.execute('update ftasks set status = 0 where task_id='+str(task_id))
    	g.db.commit()
    	g.db.close()
    	flash('The task was marked as complete.')
    	return redirect(url_for('tasks'))

These last two functions pass in a variable, `task_id` from the tasks.html page. This variable  is equal to the *task_id* filed in the database. A query is then performed and the appropriate action takes place. 

## **Tasks** ##

Finally, we need to significantly alter the tasks.html file to take into account this new functionality, which, again, used to be hello.html:

    {% extends "template.html" %}
	{% block content %}
		<div class="page">
    	<h1>Welcome to FlaskTaskR</h1>
    	<a href="/logout">Logout</a>
    	<div class="add-task">
    		<h3>Add a new task:</h3>
    		<table>
    		<tr>
    		<form action="{{ url_for('new_task') }}" method=post class=new-task>
    			<td>
				<label>Task Name:</label>
				<input name="name" type="text">
				</td>
				<td>
				<label>Due Date (mm/dd/yyyy):</label>
				<input name="due_date" type="text" width="120px">
				</td>
			</tr>
			<tr> 
				<td>
				<label>Priority:</label>
				<select name="priority" width="100px">
				<option value="1">1</option>
				<option value="2">2</option>
				<option value="3">3</option>
				<option value="4">4</option>
				<option value="5">5</option>
				<option value="6">6</option>
				<option value="7">7</option>
				<option value="8">8</option>
				<option value="9">9</option>
				<option value="10">10</option>
				</select>
				</td>
				<td>
				&nbsp; 
				&nbsp; 
				<input class="button" type="submit" value="Save">
				</td>
			</form>
			</tr>
			</table>
		</div>
		<div class="entries">
		<h2>Open tasks:</h2>
		<div class="datagrid">
    	<table>
    		<thread>
    		<tr>
          	<th width="300px"><strong>Task Name</strong></th>
          	<th width="100px"><strong>Due Date</strong></th>
          	<th width="50px"><strong>Priority</strong></th>
          	<th><b>Actions</b></th>
        	</tr>
    		</thread>
			{% for o in open_tasks %}
        	<tr> 
          	<td width="300px">{{ o.name }}</td>
          	<td width="100px">{{ o.due_date }}</td>
          	<td width="50px">{{ o.priority }}</td>
          	<td>
            	<a href="{{ url_for('delete_entry', task_id = o.task_id) }}">Delete</a>  - 
            	<a href="{{ url_for('complete', task_id = o.task_id) }}">Mark as Complete</a>
      	    </td>
			</tr> 
          	{% endfor %} 
    	</table>
		</div>
    	<br/>
    	<br/>
    	<div class="entries">
    	<h2>Closed tasks:</h2>
    	<div class="datagrid">
		<table>
    		<thread>
    		<tr>
          	<th width="300px"><strong>Task Name</strong></th>
          	<th width="100px"><strong>Due Date</strong></th>
          	<th width="50px"><strong>Priority</strong></th>
          	<th><b>Actions</b></th>
        	</tr>
    		</thread>
			{% for c in closed_tasks %}
        	<tr> 
          	<td width="300px">{{ c.name }}</td>
          	<td width="100px">{{ c.due_date }}</td>
          	<td width="50px">{{ c.priority }}</td>
          	<td>
            	<a href="{{ url_for('delete_entry', task_id = c.task_id) }}">Delete</a>
      	  	</td>
			</tr> 
          	{% endfor %} 
    	</table>
		</div>
		</div>
	{% endblock %}

Essentially, we're using for loops to output the data from the open and closed tasks. Make sure you understand how the links for *delete* and *mark as complete* work. Look back at the routes.py file. Check out the video for further detail.

## **Conclusion** ##

Finally, test out the functionality locally before deploying. In reality, we didn't make too many changes. In fact, the only new thing that you haven't seen thus far is the URLs for *delete* and *mark as complete*. 

Well, I am going to leave this app alone for a while - but there still is much I want to add and more I want to show you, such as advanced debugging, data/form validation, making edits to tasks, and much more. Something to look forward too. 

Thanks for reading. 
{% endraw %}

***

{% youtube Z86QxnU9BMM %}
