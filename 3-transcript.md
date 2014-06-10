
python, flask, web development, python tutorial

Welcome to video number three. Last time, we added a basic login page for end users to login to. Now as you may have already seen, this is by no means a secure login. First, we are only handling one user. Second, we are not protecting the route in which we need to login to, which in this case is the home route.

In other words, we can access this route without being logged in - which defeats the purpose of having a login. 

We need to (a) protect that route so that it cannot be accessed by an unathorized user using the login_required decorator and (b) indicate to Flask that a user is logged in through a session key.

Before we begin, I highly recommend using a popular Flask Extensnion called Flask-Login for managing sessions; it's a small yet powerful utility. We will be creating our own means of managing sessions and users for educational purposes, but as this app grows, I will eventually migrate over to using this extension.

Anyway, let's start by adding sessions.

**

Activate your virtualenv. Get your text editor up. And then open up *app.py* and the following line of code to the login function:

```
session['logged_in'] = True
```

Eseentially, if the user's credentials are correct, then the key associated to the `logged_in` value is set to True.

Users also need to logout so let's add a new route:

```
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('welcome'))
```

Here, when a GET request is sent to that route, we "pop" the value of True out of the session object, replacing it with None which will actually delete the key. Then the user is redirected to the welcome page.

Just as a sanity check, let me show you this in the REPL:

```
>>> test = {}
>>> test["key"] = "value"
>>> test
{'key': 'value'}
>>> test.pop("key", None)
'value'
>>> test
{}
>>>
```

Make sure to add session to the imports.

Fire up the server. Oops. There's a runtime error. We need to set a secret key. 

***

So, sessions use cookies to store information about a user, which in this case is whether they are logged in or not. The difference between a session and cookie, though, is that sessions store the actual data about a user on the server side while on the client side, there's just a session id. In order to access the actual data, you need to use an encyrption key which comes from the secret key variable.

We can add this key to the app.py file like so:

```
app.secret_key = 'my precious'
```

This will work. But there's two extremely dangerous security flaws. First - the value associated to the variable should be completely random - so that it's nearly impossible to guess. Use a random key generator for this. Next - this key should be placed in a seperate config file, which would then be added to the imports. We'll address both of these issues in another video. For now, just know that you need a secret key for sessions to work properly. The session key protects the session from being accessed client side. And the means in which we are adding the key to our app is less than ideal but will still work. 

Refresh the page. Login again. It works! 

Now if you open Developer Tools. Go to the resources tab. Click cookies. We can see our session as well as the key. You can also see that it is part of the response object in the network tab.

Now logout. We're redirected and the session is now gone, which we can confirm on the resources tab again.

**

Let's add flask messaging to provide the user with some feedback. These are generally coupled with templates and work along side requests.

First, add the following messages to the login and logout functions: 

```
flash('You were logged in.')

flash('You were logged out.')
```

Add flash to the imports as well.

Next, update the home function to render a template called index.html instead of returning a string:

```
return render_template('index.html')  # render a template
```

Add in the template, which we'll grab from the repo (there's a link in the video description):

```
<!DOCTYPE html>
<html>
  <head>
    <title>Flask Intro</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <div class="container">
      <h1>Welcome to Flask!</h1>
      <br>
      {% for message in get_flashed_messages() %}
      	{{ message }}
      {% endfor %}
    </div>
  </body>
</html>
```

Notice the for loop used for retriving then displaying each flash message.

Add this for loop to the welcome and login pages as well. 

Finally, add a logout link to the index template:

```
<p>Click <a href="/logout">here</a> to logout.</p>
```

Time to test. All is well.

**

That's it for sessions. Now we need to still nned protect that home route so that only logged in, authorized users can access it. We do this using the login required decorator.

First, add the following import:

```
from functools import wraps
```

Now we need to add the actual function, which I'll grab from the repo to save some time:

```
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
```

Now let's just add the decorator to the home and logout routes:

```
@login_required
```

Now if the user sends a GET requets to the index page, and they are not logged in (meaning there's not a key called "logged_in" in the session object), then the login_required function will catch it and redirect the user back to the login page.

Test this out. While logged out, see what happends if you try to access the index URL. Let's check the logout url as well.

Alright. Everything works. 

**

So, if you're curious to know more about how this decorator works, check out the Real Python course at realpython.com. 

Next time we'll add in a database to house some actual content. Thanks again for watching. See you next time. Cheers!