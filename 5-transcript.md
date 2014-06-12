python, flask, web development, python tutorial, sql, sqlite, databases

Introduction to Flask, Part 5 - Databases

Dynamic applications must interact with data at some point. This data could come from a number of sources such as a flat JSON file or a web API, but the post common source is from a database engine. So, in this video I'll show the basics of working with SQLite, which is light-weight relational database. It's great for your development environment because it requires no setup or configuration. Just plug it and go.

Now, before we look at the popular SQl abstraction tool called SQLAlchemy, we're going to work with straight SQL. On that note, it's important for developers to learn SQL. Why? The same reason why you are probably learning Flask - so you know what's actually happening. Sure, you could skip Flask and jump right to Django - but you'd have a hard time understanding what's happening beneath the hood. The same goes for SQL. If you jump right to SQLAlchemy, working with Python objects rather than vanialla SQL, then you'll miss out on how the SQL queries are actually structured. I can almost 100% guarantee you that at some point you will have to write a SQL query. As the queries get more advanced, the easier becomes to write them in actual SQL. Plus, it's hard to structure your queries in an efficent manner using Python objects without fully understanding SQL.

I'll stop now, but if you'd like to know more, check out my popular blog post on the matter called. Learn SQL, Dammit. You can find the link below.

Moving on ...

Keep in mind that Flask can handle both SQL and NoSQL databases, so everything from Postgres to MySQL to MongoDB to rethinkDB. When we launch our app in production, we'll be utilize a Postgres database. But I do plan on showing you how to work with straight JSON objects from MongoDB as well. If you're curious, there's a simple flask todo app tutorial on the RP blog that details how to connect to a NoSQL database. Check it out.

**

Now, I am going to assume you have zero SQL knowledge and show you how to create and add data to a basic database. However, this is not a video on learning SQL. If you do want to learn SQL (which, again, I highly encourage you to do so), you will learn it from the ground up in the Real Python course. Check it out.

Be sure to download SQLite before beginning. I also recommend the SQLite Database Browser, so that you can interact with your database without using SQL. I use this as a quick sanity check to make sure my queries work.

You can download it here: http://sqlitebrowser.org/

Let's start by creating our database's tables and then add some data. Activate your virtualenv. Open the project in your text editor.

Create a new file called sql.py within your main directory. Then withing that file ...

```
import sqlite3
```

import sqlite, then let's create a connection.

```
with sqlite3.connect("sample.db") as connection:
```

And this will create the database if it does not exist. Now we need to define a cursor, which allows us to interact with the database itself.

```
    c = connection.cursor()
```

Create a new table. We'll call it posts and then add in the columns title and description, which both have a text datatype:

```
    c.execute("""CREATE TABLE posts(title TEXT, description TEXT)""")
```

Finally, let's add some data:

```
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
```

Save the file. Then run it. We can interact directly with that new database using the SQLite shell.

```
$ sqlite3 sample.db
```

Now, let's look at all the data:

```
select * from posts;
```

And there are the posts that we added.

Let's add a new post:

```
insert into posts values('Hello', 'Hello from the shell')
```

Now query for all posts, and there we go - our new post.

So you can pause the video now if you'd like and add in more data. I also suggest checking out the SQLite documentation to see examples of some of the other commands. Try deleting a post, for example. Or maybe update a posts description. Take all the time you need. I'll wait.

***

Okay. I hope you had some fun and learned a few things. Exit the SQLite shell. Let's look at our data real quick in the SQLite browser. Open the folder in your Finder, then open the database. Click browse. There's our data.

Next open up your app.py file. We need to add in some basic configuration, indicating the existance of the database to Flask.

Add the sqlite3 import as well as the following variable:

```
app.database = 'sample.db'
```

Finally, let's add a function to connect to the database:

```
def connect_db():
    return sqlite3.connect(app.database)
```

Let's test this out real quick. Open a Python Shell. I'm using ipython; if you don't have it installed, I suggest you install it otherwise just enter the regular shell.

```
In [6]: from app import *

In [7]: c = connect_db()

In [8]: c
Out[8]: <sqlite3.Connection at 0x1026735a0>

In [9]: c.close()

```

And you can see our connection object assigned to the c variable. Cool.

**

Close the connection. Exit the Shell. Return to app.py and let's use that function to establish a connection so that we can query the database. Add the following code to the home() function.

```
g.db  = connect_db()
cur = g.db.execute('select * from posts')
posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
g.db.close()
return render_template('hello.html', sales=sales)
```

First, establish the connection. G is an object specific to Flask that's used to store a tempory object during a request - like a database connection or the currently logged in user. The value is reset after each request.

Then fetch the data from the "posts" table then caste it to a dictionary that's assigned to the variable posts. Close the connection. Finally pass in the posts variable to our template.

Next, let's update the template. Open index.html. Grab the updated HTML from the repo.

This is a relatively straightforward: We use a simple for loop to iterate through the dictionary, calling each key on each pass through, to display the results.

Let's test it out. Fire up the server. Login. There's our posts. Open up Developer Tools. Click the Network tab. Refresh the page. Click the link here. Scroll down to see the response info.

**

Alright. That's it. All done. And you know what, we have a full application here. Can you believe it?

Well, to be clear, we have a web 1.0 application allowing a user to login and view info. We still need to add in some sort of user interaction, possibly by allowing them to add new posts. That's for another video.

Next time we'll add in some unit tests. Until then, think about where you'd like this video series to go. What kind of app would you like me to create. The stack will be Postgres, Flask, Angular. There will be a RESTful API that Angular consumes data from and creates nicely formatted charts and graphs.

As far as the data is concerned, what would you like to see? I like the idea of developing an app to create quizes that provide instant feedback with Angular. If you'd like to see something different let me know. Comment. Email. Etc.

Thanks for watching. Cheers!







