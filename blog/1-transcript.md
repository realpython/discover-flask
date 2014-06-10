python, flask, web development, python tutorial

In this series of tutorials we'll be looking at the Flask framework powered by Python. 

It's an excellent framework to start with because you can start small, literally building an app in a single file, then as your site becomes more and more complex, you can scale your application up to multiple files and folders.

*

Before we begin, you should have a version of Python 2.7 installed. I'm using version 2.7.6. You also need pip for installing Python packages as well as virtualenv.

Check the video description for info on all the tools that I'm using as well as links on installing Python, pip, and virtualenv There's also a link to the blog post associated with this video. 

*

So, in this first video we'll be going over setting up a basic Flask structure and developing a static site, styled with Bootstrap.

Navigate to a convenient directory, such as the desktop or documents folders. Create a new folder to house your project called flask-intro. 

Create then activate a virtualenv.

Install Flask. This will take just a minute.

*

While that's installing, let's talk the project structure. If you're familar with a high-level web framework such as Django, then you're accustomed to the fact that it does a lot for you, including defining a project structure that you should adhere to. 

Flask does not force any structure on you, which can make it difficult for beginners to get started. 

With that in mind, it's generally a good idea to start just with a single file for the Flask components to make things simple before you start scaling to multiple files and folder.

So, within that flask-intro folder, add a new file called app.py to house the Python code for the Flask app, then a folder called static for your static files and another follder called templates for your HTML files. 

Check out the blog post, which again you can find a link to within this video's description, to learn more about this project structure and how the app.py file ties each component together.

*

Next, open up a code editor. I'll be using Sublime Text. Let's create our basic app.

Start by importing the Flask class from the flask module.

```python
from flask import Flask
```

Now create the application object.

```python
app = Flask(__name__)
```

Next we need to setup our first route. To do that we use a decorator to join a URL to a function. In this case, our URL is just the main URL and the function is called home. Finally, for the response, we just return hello world string.

```python
@app.route('/')
def home():
    return "Hello, World!"  # return a string
```

Finally, we need to start the server with the run() method.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

The debug mode will give us debugger we can use in the browser as well auto reload for when code changes are made. You'll see what I mean in a second.

That's it. 

*

Time to test. Fire up the server. Alright, so we can see that it's running. That URL 127.0.0.1 is also known as local host. 

Open your browser, then navigate to local host port 500. There's our hello world text rendered in HTML. You can see the entire response in chrome developer tools within the network tab. Aside for the output, we have the status code of 200 and the content type of HTML/Text. 

Notice how we did not have to define either of these. Flask defined these for us. 

*

Let's add one more route. 

Back to your editor, let's add a /welcome url, which is linked to a function also called welcome.

This time instead of just responding with a string, let's render a full HTML template. We'll call it welcome.html. Make sure you aslo add the render_template method to the imports.

If we test it out now, we will receive an error. Notice that we are not seeing just a 500 error; Flask is giving us more to work with which can be quite handly. This is part of the debugger. If you remove the debug mode, then you'll just see a plain 500 error.

This error just means that Flask is trying to find the welcome template but can't find it. Let's add it.

Also, because the debugger was enabled we didn't have to restart the server after code changes were made. Instead, it's watching for changes, and when it sees them, it automatically refreshes. 

*

Create a welcome.html file. I'll just go ahead and copy and paste this code in. This is just a straightforward HTML page.

* 

In the browser, navigate to the /welcome url. There you go. Nothing too special. Let's add in some quick bootsrap styles. Navigate to getbootstrap.com. Click download. Download the full download. Extract the contents of the file. Now grab the CSS file and drop it in the static folder. Then do the same with the javascript file.

*

Back in your editor, add in the stylesheet. Refresh the page. Still nothing too special, but I'll show you how to add some basic Bootstrap styles in the latter video.

*

Alright, be sure to check out the blog post for the full tutorial. Comment if you have questions. Thanks for watching.





