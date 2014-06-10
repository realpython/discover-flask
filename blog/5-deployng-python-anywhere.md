---
layout: post
title: "Introduction to Flask (part 5) - deploying to PythonAnywhere"
date: 2013-01-31 16:16
comments: true
categories: tutorials
---

{% raw %}
Well, we've reached the point where we're ready to deploy our new application to the web. My current favorite Python hosting environment is [PythonAnywhere](http://www.pythonanywhere.com/). The PaaS actually doubles as an IDE, which is really cool. Just a few of the many features include Dropbox connectivity for syncing files, scheduled tasks, and even pair programming. Let's get started. 

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
5. => Part 5 - Deploying to PythonAnywhere [Tutorial](http://www.realpythonfortheweb.com/blog/2013/01/31/introduction-to-flask-deploying/) /
[Video](http://www.youtube.com/watch?v=M4sxSoRZLtI)
6. Part 6 - Task Management Application (FlaskTaskr): [Tutorial](http://www.realpythonfortheweb.com/blog/2013/02/06/introduction-to-flask-web-app/) /
[Video](http://youtu.be/Z86QxnU9BMM)

GitHub Repo: [https://github.com/mjhea0/flask-intro](https://github.com/mjhea0/flask-intro)

## **Goals** ##

Our goal is simple: Get our app on the web so the world can enjoy it.

## **PythonAnywhere** ##

You'll first want to sign up for PythonAnywhere. They have a free account where you can deploy two apps. Once signed up, go ahead and login, navigate to your Dashboard, click "Web", and then finally click "Add a new web app".

Don't change the app's domain - just click Next. Select Flask, leave the Path just the way it is, and click Next again to create your Flask project.

Click the link for "Files", select your project, and you'll see a sample app called flask_app.py. It's just a basic Hello, World type app. If you want to see the results from the client-side, navigate your browser to [your_user_name].pythonanywhere.com.

Back to the admin page, go ahead and delete the sample app so we can set up our project. 

In essence, set up your project just like it is on your computer:

1. Create the static directory and then add the three subdirectories
1. Create the templates directory
1. Add the .css file to the CSS directory
1. Add all of your templates to the templates directory
1. Add routes.py and sales.db to your project's root directory

There's one change that needs to be made to the routes.py file. Go ahead and click the file to open the editor. Now we need to change the path to our database.

	/home/[your_user_name]/[project_directory]/sales.db

In my case:

	/home/realpython/mysite/sales.db

 Save the file. Click the link for the Dashboard, then click "Web". We need to make one change to the WSGI file. Open it up and update the code to import your app to:

	from routes import app as application

We should be good to go. Click Save => Dashboard => Web => Reload web app. Your app should now be live.

Pull it up in your browser. Play around. Make sure everything works. 


## **Conclusion** ##

Alright. Now that you know all the fundamentals, let's build something practical. In the next tutorial, we'll be building a micro task manager. 

Feel free to leave comments below with any questions. 

Best!
{% endraw %}

***

{% youtube M4sxSoRZLtI %}
