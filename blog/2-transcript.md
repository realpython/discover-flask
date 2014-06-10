python, flask, web development, python tutorial

In the last tutroial we set up a basic Flask static app that included two endpoints. Just the main URL and welcome. 

In this video we'll be adding a basic login page for end users to login to. Now since this code builds on the previous code, be sure to build the app by watching the previous video, or download the code from the blog post. You'll find links to both in this video's description.

*

Navigate to the directory housing your app. Activate your virtualenv. Then open the project in sublime. 

Open the *app.py file. And let's add the new route for the login page.

First update your imports:

```python
from flask import Flask, render_template, redirect, url_for, request
```

Next add in the route decorator, specifying the URL. 

```python
@app.route('/login', 
```


We also need to add an argument for the HTTP methods.

```python
methods=['GET', 'POST'])
```

Notice how the other decorators don't need this argument. That's because by default, Flask assumes that the method is a GET request. If you need to apply other methods to a route, then you need to explicitly add them in. 

In this case, we need the GET method as usual as well as POST so that end users can send a POST request with their login credentials to that `/login` endpoint.

Next, we add the function that the URL is mapped to. We'll call this login:

```python
def login():
    error = None  # set variable error equal to None
    return render_template('login.html', error=error)
```

Based on the logic within this route, right now, there's no way to handle a POST request. All this is doing is rendering an HTML template and passing an error message to that template. 

In order to handle the post request we need to expand this function:

```python
if request.method == 'POST':
```

If the end user's request is POST, then ..

```python
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        error = 'Invalid Credentials. Please try again.'
    else:
        return redirect(url_for('home'))
```

Let's test the data sent along with that requst.

If the username and password do not equal `admin`, we send and error. If they are equal to admin, then we redirect them to the main url.

Simple as that.

*

Next, we just need to add our login.html template, which I am going to grab from the repo. Again, you can find a link to the Github repository in the video's description.

Now, before we break down this template, let's test out our app. 

Fire up the server.

Navigate to the login page. 

Open up chrome developer tools. Click the network tab. 

First, let's send incorrect data. Type in anything but admin and admin for the username and password. 

You can see the response, but let's dig a little deeper. Click on login. On the Headers tab you can see what was sent with the POST request. And there's the actual data sent.

Now, let's try that again. This time use both admin for the username and password. 

First, you can see the 302 status code which indicates a redirect occured, which redirect us to the `/` endpoint. You can also see this in the terminal. If we check the headers again, we can see that both admin and admin were sent. 

Going back to the code ...

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
        <p class="error"><strong>Error:</strong> {{ error }}</p>
      {% endif %}
    </div>
  </body>
</html>
```

First, in the templates you can see that we have some strange syntax, which is not HTML.

The `{%` tag is used for Python-like expressions such as conditionals and loops, while `{{` tags are for variables or the results from an expression. In this case we pass in the error variable from the view and if it evaluates to not None, then that `<p></p>` tag is displayed along with the content within it which include the actual error message. 

Other than that, we have a basic HTML form that sends a POST request along with the values from the input boxes as we have already seen. 

But let's check it out again. This time let's send the incorrect credentials. 

Within developer tools again, click the login link. Now click preview. The `{{` variables wew replaced with the actual values. Error message. You can even see the username and password values that were submitted.

For more on this, check out the blog post.

*

Alright, well we quickly added a login page that users can login to. There's still much to be done with regard to user management. But this is a good stopping point for today. Be sure to check out the blog post for the full tutorial. Comment if you have questions. Thanks for watching.