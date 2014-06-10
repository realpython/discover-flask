# Introduction to Flask, Part 1 - Setting up a static site

> **Note**: This article was original posted on 01/29/2013. Due to the vast overall of it, it was decided to "retire" the old article and create a new article. If you are interested in viewing the code and video for the old tutorial, please visit this [repo](https://github.com/mjhea0/flask-intro).

[Flask](http://flask.pocoo.org/) is a micro web framework powered by Python. It's API is fairly small, making it easy to learn and simple to use. But don't let this fool you, as it's powerful enough to support enterprise-level applications handling large amounts of traffic. You can start small with an app contained entirely in one file, then slowly scale up to multiple files and folders in a well-structured manner as your site becomes more and more complex. 

It's an excellent framework to start with, which you'll be learning in true "Real Python-style": with hands-on, practical examples that are interesting and fun. Let's begin.

**Check out the accompanying [video](https://www.youtube.com/watch?v=Gix_zeTrT7E).**

## Requirements

This tutorial assumes you have [Python 2.7.x](https://www.python.org/download/releases/2.7), [pip](http://pip.readthedocs.org/en/latest/installing.html), and [virtualenv](http://virtualenv.readthedocs.org/en/latest/) installed. 

Ideally, you should have basic knowledge of the command line or terminal and Python general. If not, you will learn enough to get by, then as you continue working with Flask, your development skills will advanced as well. If you do want additional help, check out the [Real Python](http://www.realpython.com) series to learn Python and web development from the ground up.

You also need a code editor or IDE such as [Sublime Text](http://www.sublimetext.com/), [gedit](https://wiki.gnome.org/Apps/Gedit), [Notepad++](http://notepad-plus-plus.org/), or [VIM](http://vimdoc.sourceforge.net/), etc. If you're ensure what to use, check out Sublime Text, which is a lightweight, yet powerful cross-platform code editor. 

## Conventions

1. All examples in this tutorial utilize a Unix-style prompt:

    ```
    $ python hello-world.py
    ```
    
    Remember that the dollar sign is not part of the command, and the equivalent command in Windows is:

    ```
    C:\Sites> python hello-world.py
    ```

2. All examples are coded in Sublime Text 3. 

3. All examples utilize Python 2.7.7. You can use any version of 2.7.x.

4. Additional requirements and dependency versions are listed in the *requirements.txt* file found within the Github [repo](https://github.com/realpython/flask-intro).
    
## Setup

1. Navigate to a convenient directory, such as the "Desktop" or "Documents" folder
2. Create a new directory called "flask-intro" to house your project
3. Activate a virtualenv:

    ```
    $ cd flask-intro
    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate
    ```

4. Install Flask:

    ```
    $ pip install Flask
    ```
 
## Structure

If you're familiar with [Django](https://www.djangoproject.com/), [web2py](http://www.web2py.com/), or any other high-level (or [full-stack](https://wiki.python.org/moin/WebFrameworks)) framework, then you know that each impose a specific structure. Due to it's minimalist nature, however, Flask does not provide a set structure, which can be difficult for beginners. Fortunately, it's fairly easy to figure out, especially if you use a single file for the Flask components.

Create the following project structure within the "flask-intro" folder:

    ```
    .
    ├── app.py
    ├── static
    └── templates
    ```

Here, we simply have a single file for our Flask app called *app.py* and then have two folders, "static" and "templates". The former houses our stylesheets, Javascript files, and images, while the latter is for HTML files. This is a good base to start with. We're already thinking in terms of front vs. back-end. The *app.py* will utilize the Model-View-Controller (MVC) design pattern in the back-end to handle requests and dish out responses to the end user. 

Put simply, when a request comes in, the controller, which handles our app's business logic, decides how to handle it. 

For example, the controller could communicate directly with a database (like MySQL, SQLite, PostgreSQL, MongoDB, etc.) to obtain the requested data and return a response, via the views, with the appropriate data in the appropriate format (like HTML or JSON). Or perhaps the end user's request is for a resource that does not exist - in which case the controller will respond with a 404 error. 

Starting with this structure will help with scaling your app out into separate files and folders, since there is already a logical separation between the front and back-end. If you're unfamiliar with the MVC pattern, read more about it [here](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). Get used to it as almost every web framework utilizes some form of MVC.

## Routes

Open your favorite editor and add the following code to your *app.py* file:

```python
# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
```

The code is fairly straightforward. 

After importing the `Flask` class, we create (or instantiate) the application object, define the views to respond to requests, then start the server. 

The `route` [decorators](http://flask.pocoo.org/docs/patterns/viewdecorators/) are used to associate (or map) a URL to a function. The URL `/` is associated with the `home()` function, so when the end user requests that URL, the view will respond with a string. Similarly, when the `/welcome` URL is requested, the view will render the *welcome.html* template. 

**In short, the main application object is instantiated which is then used to map URLs to functions.**

For a more detailed explanation, read Flask’s quick-start [tutorial](http://flask.pocoo.org/docs/quickstart/).

## Test

Time for a sanity check. Fire up your development server:

```
$ python app.py
```

Navigate to [http://localhost:5000/](http://localhost:5000/). You should see "Hello, World!" staring back at you. Then request the next URL, [http://localhost:5000/welcome](http://localhost:5000/welcome). You should see, a "TemplateNotFound" error. Why? Because we have not set up our template. Flask is looking for it, but it's not there. Let's do that. First, kill the server by pressing CTRL+C from your terminal.

> For more on the actual response, check out the [video](https://www.youtube.com/watch?v=Gix_zeTrT7E") accompanying this post.

## Templates

Create a new file in your templates directory called *welcome.html*. Open this file in your code editor, then add the following HTML:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Flask Intro</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <div class="container">
      <h1>Welcome to Flask!</h2>
      <br>
      <p>Click <a href="/">here</a> to go home.</p>
    </div>
  </body>
</html>
```
    
Save. Run your server again. What do you see now when you request [http://localhost:5000/welcome](http://localhost:5000/welcome)? Test the link. It works but it's not very pretty. Let's change that. This time leave the server running as we make the changes.

## Bootstrap 

Okay. Let's utilize those static folders by adding a stylesheet. Have you heard of bootstrap? If your answer is no, then check out [this](http://www.realpython.com/blog/design/getting-started-with-bootstrap-3/) blog post for details.

Download [Bootstrap](http://getbootstrap.com/), then add the *bootstrap.min.css* and *bootstrap.min.js* files to your "static" folder. 

Update the template:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Flask Intro</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <h1>Welcome to Flask!</h2>
      <br>
      <p>Click <a href="/">here</a> to go home.</p>
    </div>
  </body>
</html>
```

We just added included the CSS stylesheets. We'll add in a bit of Javascript in a latter tutorial. 

Return to your browser. 

Remember that we left the server running? Well, when Flask is in [debug mode](http://flask.pocoo.org/docs/quickstart/#debug-mode), `app.run(debug=True)`, there's an auto-reload mechanism that kicks in on code changes. Thus, we can just press refresh in our browser and we should see the new template staring right back at us. 

Nice.

## Conclusion

What are your initial thoughts? Comment below. Grab the [code](https://github.com/realpython/flask-intro). Watch the [video](https://www.youtube.com/watch?v=Gix_zeTrT7E).

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Gix_zeTrT7E
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

In under thirty minutes, you learned the Flask basics and set the ground work for a larger app. If you've worked with Django before, you probably noticed immediately that Flask stays out of your way as you develop, leaving you free to structure and design your app how you see fit. Because of the lack of structure, true beginners may struggle a bit, however it's an invaluable learning experience that will benefit you in the long run, regardless of whether you continue working with Flask or move on to a higher-level framework. 

In the next tutorial we'll look at adding some dynamic content. 

Cheers!