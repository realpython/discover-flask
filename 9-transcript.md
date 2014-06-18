
In Part 9 of this series, we'll add the popular extension Flask-SQLAlchemy to better manage our database.

Intro to Flask, Part 9 - SQLAlchemy

The time has come to move away from interacting with our database with raw SQL and instead use SQLAlchemy, which is a powerful abstraction layer and Object Relatonal Mappers.

Most ORM increase your productivity, because you don't have to switch languages (to SQL, in other words) as you develop and interact with your database. There's also the added benefit of portability. Since SQLAlchemy is a high-level ORM, it can abstract the database engine, making it easy to switch from SQLite to Postgres, for example. Sounds too good to be true? It can be. There is a slight decrease in performance that is inherent with all ORMs due to the overhead from converting objects to much simplier data formats found in most databases - and vice versa. In most cases the productivity gain outweights the decrease in performance, though. Be mindful of the benefits of learning SQL that I outlined in the 5th video as well.

http://pythonhosted.org/Flask-SQLAlchemy/

The Flask SQLAlchemy extension further simplifies database interaction, by providing a number of pre-configured defaults right out of the box. Be sure to check out the documenation for further details.

**

Start by installing the extension with pip, which will also install the full SQLAlchemy package:

pip install Flask-SQLAlchemy

**

Now let's recreate our database schema using SQLAlchemy. Take note of how we accomplish this vs how we did it before with raw SQL.

First, add a file called models.py. With our SQL.py file open side by side, we can easily translate the SQL commands over to objects.

```
from app import db


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, descriptio):
        self.title = title
        self.descriptio = descriptio

    def __repr__(self):
        return '<title {}'.format(self.title)
```

1. So, we defined a new class called BlogPost (which inherets from db.Model) that has three fields, each defined as class variables or attributes.
1. We also specified the actual table name we want to use within the database.
1. Next, we defined the constructor, the under init method, for each individual instance attribute.
1. Finally, method is used for specifying how we want the object to be represented when printed. This will make more sense in a second.

Save this file.

**

Next we need to update our app's configuration. Open app.py.

Update the config setting to initialize SQL ALchemy.

```
# create the application object
app = Flask(__name__)

# config
app.secret_key = 'my precious'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' # setup the db engine

# create the sqlalchemy object
db = SQLAlchemy(app)
```

Update the imports:

```
from flask.ext.sqlalchemy import SQLAlchemy
# import sqlite3
```

Then comment out this function:

```
# # connect to database
# def connect_db():
#     return sqlite3.connect(app.database)
```

That's it. The config should now be updated so that we can use SQLAlchemy to manage our database.

Just make a mental note that we will need to refactor the home() function since it's still utilzing the sqlite3 python package to interact with the db.

***

Now we are ready to actually create our new db.

Create a new file called db_create.py:

```
from app import db
from models import BlogPost

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "I\'m okay."))

# commit the changes
db.session.commit()
```

Import ...

With just one command, db.create_all(), we can initialize the database, based on the schema defined in our models.py file. That's the power you get with SQLAlchemy.

***

Run. Since we didn't get an error, we can assume it worked. Let's double check that though.

**

Enter the Shell:

Let's query the database.

```
In [5]: from models import BlogPost

In [6]: posts = BlogPost.query.all()

In [7]: posts
Out[7]: [<title Good, <title Well, <title Excellent, <title Okay]
```

This is the same as the select command, select all from posts.

Take a look at the ouput. Do you see how each object is represented. Remember that method we used to do that?

https://docs.python.org/2/reference/datamodel.html#object.__repr__

This just allows us to represent the object with a string. Let's update it:

return '<{} - {}'.format(self.title, self.description)

Test in the shell.

Make sense?

Change it back.

Let's add some data:

```
from app import db
>>> db.session.add(BlogPost("Test", "Shell Test"))
>>> db.session.commit()
```

Be sure to check out the full Flask SQLAlchemy docs for all the basic SQL commands - http://pythonhosted.org/Flask-SQLAlchemy/queries.html

There's a link to the docs in this vide's description

query again:

```
posts = BlogPost.query.all()
```

There's are new post. Boom. Exit the shell. Check the SQLite Browser to visually see the data.

**

Did you remember that we need to refactor the home function(). Good. Let's do that now.


First, if we really wanted to, we could still use SQLite to query the db.

Uncomment import sqlite3

Update:

```
# # connect to database
# def connect_db():
#     return sqlite3.connect('posts.db')
```

Run the server. There's our posts.

However, this doesn't make much sense now that we are using SQLAlchemy, since SQLAlchemy lets us query with objects or even raw SQL if we want.

Comment out again.

Update the function

```
# use decorators to link the function to a url
@app.route('/')
@login_required
def home():
    # return "Hello, World!"  # return a string
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)  # render a template
```

Test it out. python tests.py

And all is well.

**

I think we'll go ahead and stop here. What I hope you've gotten out of these videos thus far is that Flask stays out of your way as you develop, unlike some of the heavier frameworks - like Django. It gives us freedom. That said, as we start adding pre-built extensions, like FLask-SQLAlchemy, we limit that freedom to some degree. Granted, tou could build or roll your own solutions, but these extensions are battle tested and are continually being updated. Weigh the pros and cons of each route - building vs. extending, for your app.

Next time, we are going to do some refactoring.

1. We'll add a config.py file to better organize our app
2. Then we'll update that failing test
3. And there's probably a few more things that need refactoring that are escaping me right now.

Oh - and we'll get our app fully working on Heroku as well.

Thanks for watching. Have a great day!





