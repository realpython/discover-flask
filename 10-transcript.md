python, flask, web development, python tutorial, config.py, config, configuration

In Part 10 of this series, we'll update our configuration settings.

Intro to Flask, Part 10 - Configuration

Okay. So, in part 10 of this series, we'll look at some conventions regarding your app's configration settings.

In general, all appplications require some sort of settings specific to your setup.

For example, if you look at our app.py file, we defined the secret key and the location of the database and turned debug mode on. These settings are specific to our app, in our current environment - which is our local development environment. When we deployed our app to Heroku, some of our settings didn't translate over correctly.

In fact, all of our currently defined settings need to be configured differently for Heroku.

Thus, your settings change depending on your application's environment.

We've also hard-coded our configuration settings directly in the code within app.py. You can get away with this for small applications, but the complexity of your app's config increases with the size and scale of your app and the more environment's that your app operates in. For example, each environment requires a different database connection, and you'll often need to utilize different API keys - one for your live environment and another for a testing environment - depending on the service.

Because of this it's common practice to utilize a different config file for each environment.

That said, since our app is still relatively small, we can just use one file for now. We'll set up a parent class for our default config settings, then have a seperate child classes for each of our environments to override the default settings when necessary.

Let's get to it.

**

Start by adding a config.py file to your app's root directory.

Then add the following config:

```
# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my precious'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
```

This is our default config. So let's add a class and call it BaseConfig, which will inheret from object. Now we can use class variables to define our config settings.


Update app.py:

```
app.config.from_object('config.BaseConfig')
```


Remove `debug = True`

Here, we are importing our config file into our app using `app.config' along with the 'from_object()` method. We are then referencing the `BaseConfig()` class. So, when our app is initalized, it's configured with all the class variables from the BaseConfig class.

Test it out. Open the shell.

```
In [1]: from app import app

In [2]: print app.config
```

Here we can see the settings we defined. Debug. Database URI. and SECRET KEY.

So, we set up our parent config settings with some default settings. Now, we can define different settings for each of the environments that our app will operate in. These classes will inherent the default settings from the parent class.

Let's set up a config specific to our local development environment.

**

Return to config.py

Add the following class:

```
class DevelopmentConfig(BaseConfig):
    DEBUG = True
```

So, here we are overriding the DEBUG class variable from the parent class.

***

Let's test this out. Open app.py and update our config settings:

```
app.config.from_object('config.DevelopmentConfig')
```

Now let's check our actual settings from the shell. So you can see that DEBUG is now TRUE, while our DATABASE URI and SESSION KEYS are still the same. This is exactly what we want.

**

Next, let's setup settings for our production environment, which is our live app on Heroku.

config.py:

```
class ProductionConfig(BaseConfig):
    DEBUG = False
```

So, even though our default config sets DEBUG to false, I added it to our ProductConfig for two reasons. First, I want to be absolutely certain that DEBUG will be false in production. If we screw up somehow with inheritence and accidently set it to true, we are exposing our server to the outside world - which is obviously not good. And the other reason is just for educational purposes: I just want to be explicit with everything. Yes, our code is not perfectly DRY, since we are repeating code, but I want to err on the side of being less DRY if it allows you to understand what's happening better.

**

If you're following along really well - you may have noticed that we have a problem. Since I am hard-coding our environment class in app.py, how do we set this up so that Flask "knows" which environment it's in?

And the answer is that we can use environment variables. If you're not familiar with env variables, I suggest doing a quick Google search - but, put simply, they are simple key/value pairs that reside in the operating environment which make it easy to pass information to programs.

In order for Flask to recognize these variables, we need to update how we import the config settings into our app:

```
app.config.from_object(os.environ['APP_SETTINGS'])
```

Don't forget to import os.

Now, we need to actually add our local settings to the environment to create the environment variables. To do that, run the following command from your root Flask directory:

```
export APP_SETTINGS="config.DevelopmentConfig"
```

Now if we confirm the settings from the shell, we should see that debug is True, which indicates that we are importing the right class for this environment.

**

Okay. Stop for a minute and take a breath or two. This can be a bit confusing the first time you do this, so if that's the case, I highly recommend stopping the video right now and then watching it up to this point as many times as necessary. So, when ready, let's move on.

**

We need to do one last thing before we update Heroku - setup an env variable for our database. Why? Because our local database is different from our production database on Heroku.

This is an easy update. Simply update the BaseConfig so that the DATABASE URI imports the actual path and name of our database from the environment. Then we need to set that path and name as an environment variable. Want to try that on your own?

Pause the video.

How'd it go? Did you update your config.py to search the environment for that variable, DATABASE_URL:

```
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
```

Then did you add the DATABASE_URL environment variable like so -

```
export DATABASE_URL="sqlite:///posts.db"
```

Again if you test this in the shell, you should see that the environment variable is now updated ...

Cool.

**

Make sure you app still runs fine and then take some quick notes on what we did here since in the next video we'll be updating our config settings for our production env on Heroku. Also, there are a number of ways to set up your config settings. This just so happens to be the method that I like, which is a solid choice for the relative size of our app.

Another popular method is to create seperate config files for each environment.

Whatever the method you employ, the thing to keep in mind is that in a lot of cases, you do not want your config settings in your version control since -

(a) if you have a public repo (which I do), you can see the settings. If there is sensitive information in there, which more often than not there is, then the whole world can see it. We will fix this in a future video.

and (b) if you do just have one config file that has different settings for each env and you are not using classes like I am, then each time you PUSH to a different env, you will override the config.py file and establish the wrong settings for that environment. In other words, if you have a two environments - development and production - and you have one config file for developmen and one for production, but you are naming the files the same  - config.py. Then if you do not keep that file out of version control, your development settings will override your production settings each time you PUSH new code to heroku. If that's how you want to manage your config files, then make sure to add the filename to your .gitgnore.

Hopefully that didn't confuse you, but if it did - just use the method that I am using and you won't have to worry about it - for now at least.

Anyhow, next time we'll get our config settings setup for Heroku. Thanks again for watching.
