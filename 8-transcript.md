
Intro to Flask, Part 8 - Unit Tests

Well, we've reached the point where we're ready to deploy our new little application to the web. There are a number of different hosting options available, but by far the easiest are services like Heroku that operate in the cloud. These are known as platforms as a service, which provide everything we need to host an application - such as the servers, operating system, and database. In other words, we just need to provide the Flask application, and they provide the rest.

There are a number of these services, but we'll utilize Heroku since they have a free service level.

Now, there are a few things we need to do first, before we can just hand over our app. Let's turn to the Heroku guide for help.

**

https://devcenter.heroku.com/articles/getting-started-with-python

First, let's take a look at the prerequisites.

1. Yes, we have back Python knowledge.
2. We also have Python istalled. Make sure your virtualenv is activated.
3. We also have pip.
4. If you don't have a Heroku account be sure to sign up.

Next go ahead and install the Heroku toolbelt for your specific OS. This is a command line tool used to create and manage applications on heroku.

Now, let's loging to Heroku from the command line:

```
heroku login
```

The first time you run this command you will be prompted for your Heroku login credentials. Once authenticated, an SSH key will be created and sent to Heroku, which will automaticaly authenticate you whenever you communitate with Heroku. Thus, you will only need to enter your login credentials once.

**

We aleady have our Flask app setup, so we can skip this. We do need to install gunicorn, though. Gunicorn is a web sever that works well with Flask.

After that's installed, let's test it locally.

```
gunicorn -b 127.0.0.1:4000 app:app
```

-b is for binding the app to an address. In this case, localhost with port 500. Then we specify the project and app name, which are both the same in this case.

**

Next, we need to setup a Procfile. Heroku uses this file for determining how to execute your application. Create the file (no extension) and place it in your root directory. The syntax for the procfile is simple, each line contains a different command starting with the name, then a colon, then the actual command.

Add the following code:

```
web: gunicorn app:app
```

In this case, the name of the command is web. When Heroku sees this it expects that the command will launch the web server, which it does.

**

You can validate your Procfile format using the with foreman, which was installed with the Heroku toolbelt.

$ foreman check

You can also test the gunicorn server again:

$ foreman start

All is well. I'm confident our app will work just fine on Heroku.

**

Next, we need to provide a requirements.txt file so that Heroku know which dependencies to install.

pip provides a command for this:

```
pip freeze > requirements.txt
```

You can also run just pip freeze to see the dependencies.

**

Next we need to add our project to a local Git repository. Git was installed with the Heroku toolbelt if you didn't already have it installed.

If you're unfamiliar with Git and how version control works, check out the official Git site here - http://git-scm.com/

Before we create our local repo, we need to add a .gitignore file, which is used to ignore files from being added to our repo.

For now, just add the venv folder as well as any compiled Python and database files:

```
venv
*.pyc
*.db
```

Next, initialize or create a repo:

```
$ git init
$ git add .
$ git commit -m "init"
```

Add all files and folders (except those listed in your .gitignore file) to staging, then to add use git commit to place those files and folders into your repo.

***

Next, let's create a space on Heroku to house our app, using the Heroku create command.

```
heroku create
```

You can specify an optional site name as well, which I recommend you to do so. Otherwise, your URL will include the name of the Heroku server housing the application, plus a randomly asisgned #, which is hard to remember.

```
heroku create flask-intro
```

I am going to use flask-intro. You will have to pick a different, unique name. Get creative.

***

Now we can check our live app, but typing in heroku open in the terminal, which will open a new window in Chrome and navigate to the URL. Or you can just type in the URL -> http://flask-intro.herokuapp.com/

Obviously our app is not working yet, so we are getting the default Heroku error page.

We need to first deploy, which is also known as PUSHing because we are using Git for this, our app to Heroku. Use the following command:

```
git push heroku master
```

The first time you push will take much longer since it has to install all the dependencies from the requirements file.

Now, let's add one dyno to our app:

```
heroku ps:scale web=1
```

Dynos are specific to Heroku, but they basically allow us to run processes. In the above command, we are telling Heroku to run the web command (remember from our Procfile) and then using 1 dyno. For more on Dynos, check the Heroku documentation.

Now run Heroku ps to check the currently running processes:

```
heroku ps
```

All is well, let's check the app. Try logging in. Oh no.

Well, let's troubleshoot. Open developer tools. Is there a session? Yes, well we know that the user was logged in correctly.

What else is happening on that page? We're querying the database.

Let's try to recreate the error locally. Open app.py. Change the name of the database. Now run the app. 500 error. Let's set up an Exception Handler for this side effect.

```
    # return "Hello, World!"  # return a string
    posts = []
    try:
        g.db = connect_db()
        cur = g.db.execute('select * from posts')

        for row in cur.fetchall():
            posts.append(dict(title=row[0], description=row[1]))

        # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]

        g.db.close()
    except sqlite3.OperationalError:
        flash('Missing the DB!')
```

So, we'll try to connect to the database and if that works, then we'll grab the posts like always, but if it doesn't find a connection then we'll flash a message. This is not the best way of handling it. Can you imagine going to Google and trying to search but you get a message saying that the DB is missing. That would be a bit scary.

But are not Google and we just want to get our Heroku app working. We'll deal with the bigger issue later.

Test it locally. Now commit the new code. Push to Heroku.

Now our app is at least displaying. No ugly Internal Server Error message.

**

We stil have the bigger issue of setting up our database on Heroku. We'll address this in the next video when we upgrade to SQLAlchemy.

Finally, let's run our tests:

```
heroku run python tests.py -v
```

We can use the heroku run + the command we want to run one-off scripts. As expected, the -

test_posts_show_up_on_main_page (__main__.FlaskTestCase) ... FAIL

fails, since we are not displaying that post from the db. That's alright. We need to refactor this test anyway, which we will do next time as well.

To summarize, in this video we set up all the requirements for Heroku and then deplyed our app. We found a bug and troubleshooted it, then slapped on a temporary band aide just to get the app up. Next time we'll -

1. Migrate to SQLAlchemy for better database management
2. Add our database to Heroku
3. Refactor the failing unit test

Alright. Leave comments, questions, feedback, and/or rants below.

Best!





