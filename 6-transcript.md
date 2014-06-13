python, flask, web development, python tutorial, list comps, list comprehensions

Introduction to Flask, Part 6 - List Comprehensions

In the last video I touched on some code that was a litle too advanced for beginners and did not provide a good explanation for how it worked. So, I want to take a step back from Flask and touch on some Python data structures.

**

The code I am referring to is here -

```
posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
```

Here we cast the data fetched from the SQL query to a dictionary. And there's also a list comprehension in work here, which is just a concise way of creating a list. Let's break this down and then refactor it into something a bit more legible for beginners.

Let's start by seeing what the data structure looks like. Add a print statement to the function.

Fire up the server. Login. Now open your terminal. So, we have a list of dictionaries, where each dictionary contains information about each individual post.

Now, let's update the code to create the exact same data structure, just in a more readable way.

**

Where do we start? Well, what does fetchall() return? We could check the Python documenation but let's just test it ourselves. We can assume that it does something with all the data returned based on the name of the method. But what type of data structure is utilized?

Let's find out.

Add two more print statements:

```
print cur()
print cur.fetchall()
```

Refresh the page. Open Terminal.

Okay so the cur() is just an object, while fetchall() returns a list of tuples contaning the data from each row in the database. Keep in mind that we could pass that directly to the template as we can loop through the list and grab each piece of data from the tuples.

Let's focus on the task at hand, though, by refactoring the code to create the exact same data structure - a list of dictionaries.

Start with the creation of the dictionaries:

```
# define an empty dict
post_dict = {}
# then look through each row, adding a new key/value pair to that dict
for row in cur.fetchall():
    post_dict["title"] = row[0]
    post_dict["description"] = row[1]
    print post_dict
```

Refersh the page. Open Terminal. There's all dictionaries.

Now we can just create a list and append each dictionary to it.

```
# define an empty list
posts = []
for row in cur.fetchall():
    post_dict["title"] = row[0]
    post_dict["description"] = row[1]
    # append the data the list
    posts.append(post_dict)
    # print the list
    print posts
```

Refresh the page again and check out the results in your terminal. That looks like exactly what we want.

Finally, let's update the function.

```
posts = []
for row in cur.fetchall():
    posts.append(dict(title=row[0], description=row[1]))

# posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
```

Notice that I refactored the function to cast the results from the query to a dictionary rather than assigning each key/value pair manually. This code is not a bit cleaner.

Refresh your page. And it works. Cool.

**

I hope that all makes sense now. If you want more info on list comps, check out the Real Python course. Next time we will move back to Flask and add unit testing into the mix. Cheers!
