# Introduction to Flask, Part 2 - Creating a login page 

Last [time](http://www.realpython.com/blog/python/introduction-to-flask-part-1-setting-up-a-static-site/#.U5Chm5RdUZ0) we went over how to set up a basic Flask structure and then developed a static site, styled with Bootstrap. In this second part of the series, we'll be adding a login page for end users to, well, login to.

Building on the code from the previous tutorial, we need to-

- Add a route to handle requests to the login URL, and
- Add a template for the login page

## Add a route to handle requests to the login URL

Make sure your virtualenv is activated. Open *app.py* in your code editor and add the following route:

```python
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
```

Make sure you also update the imports:

```python
from flask import Flask, render_template, redirect, url_for, request
```

### So, what's going on?

1. First, notice that we specified the applicable HTTP methods for the route, GET and POST, as an argument in the decorator.
1. GET is the default method. So, if no methods are explicitly defined, Flask assumes that the only available [method](http://flask.pocoo.org/docs/quickstart/#http-methods) is GET, as is the case for the previous two routes, `/` and `/welcome`.
2. For the new `/login` route we need to specifiy the POST method as well as GET so that end users can send a POST request with their login credentials to that `/login` endpoint.
3. The logic within the `login()` function tests to see if the credentials are correct. If they are correct, then the user is redirected to the main route, `/`, and if the credentials are incorrect, an error populates. Where do these credentials come from? The POST request, which you'll see in just a minute.
4. In the case of a GET request, the login page is rendered.

> **NOTE**: The [`url_for()`](http://flask.pocoo.org/docs/api/#flask.url_for) function generates an endpoint for the provided method.

## Add a template for the login page

1. Create a new file called *login.html*, adding it to the "templates" directory:

  ```html
  <html>
    <head>
      <title>Flask Intro - login page</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="static/bootstrap.min.css" rel="stylesheet" media="screen">
    </head>
    <body>
      <div class="container">
        <h1>Please login</h1>
        <br>
        <form action="" method="post">
          <input type="text" placeholder="Username" name="username" value="{{
            request.form.username }}">
           <input type="password" placeholder="Password" name="password" value="{{
            request.form.password }}">
          <input class="btn btn-default" type="submit" value="Login">
        </form>
        {% if error %}
          <p class="error"><strong>Error:</strong> {{ error }}
        {% endif %}
      </div>
    </body>
  </html>
  ```

  Time for a quick test.

1. Fire up the server. Navigate to [http://localhost:5000/login](http://localhost:5000/login). 

2. Enter the incorrect credentials, then press login. You should get this response: "Error: Invalid Credentials. Please try again."

3. Now use "admin" for both the username and password and you should be redirected to the `/` URL.

4. Can you tell what's happening here? When the form is submitted, a POST request is sent along with the form data, `value="{{request.form.username }}` and `value="{{request.form.password }}"`, to the conroller, `app.py` - which then handles the request and either responds with an error message or redirects the user to the `/` URL. **Be sure to check out the accompanying video to dig deeper into this with Chrom Developer Tools!**

5. Finally, we have some logic in our templates. Originally, we passed in None for the error. Well, if the error is not None, then we display the actual error message, which gets passed to the template from the views: `<p class="error"><strong>Error:</strong> {{ error }}`. For info on how this works, check out [this](http://www.realpython.com/blog/python/primer-on-jinja-templating/#.U5CtZJRdUZ0) blog post on the Jinja2 templating engine.

## Conclusion

What do you think? Simple, right? Don't get too excited, as we still have more to do with reguard to user/session management ...

Now that users have the ability to login, we need to protect that URL `/` from unauthorized access. In other words, when an end user hits that endpoint, unless they are already logged in, then they should be immediately sent to the login page. Next time. Until then, go [practice](http://www.realpython.com/learn/jquery-practice/) some jQuery.
