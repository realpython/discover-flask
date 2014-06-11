python, flask, web development, python tutorial, jinga

Introduction to Flask, Part 4 - Template Inheritence

http://www.realpython.com/blog/python/primer-on-jinja-templating

Okay. Here we are - video number four. I know I said last time tha we'd be adding a database in this video, but I got a request to simplify the HTML templates via inheritence, which I was going to save for video number ten or so when we go over macros and filtering within templates. However, I agree: it's a good idea to setup our template directory correctly.

Before we start, I highly recommend reading a blog post I wrote called, A Primer on Jinja Templating. As always, you can find a link directly to it in this video's description.

Oh - and if you've been following along with the other videos, you probably noticed that my Sublime text environment looks a bit different. I went through and added some settings and packages to customize it for Python, full-stack development. I may detail my setup in a future video. If interested, request it in the comments.

Alright. Let's get started.

**

Although you can use any templating system you want, Flask uses the Jinja2 templating engine right out of the box. Unless you have a good reason not to use Jinja, then you should stick with it - because it's just as powerful as say the Django templating engine, but it loads much faster. I often use Jinja2 with DJango.

Anyhow, your templates should take advantage of inheritence, which inclues a parent template that defines the basic structure for all subsequent child templates.

This helps keep common, boilerplate code not only in sync but it's also stored in one place.

If we look at our templates now you can see that there is a lot of code reuse; the goal with templating is to move that recurring code to the parent template. So, we can move the every before the body tag as well as everything starting with the error message to the parent template.

**

Create a new file called base.html to house our parent template. I'll grab the HTML for this from the repo.

The block tags define a block (or area) that our child templates will fill in. In other words, when we request a URL, the block tags will be replaced with the HTML from that template.

**

Now we need to update each of our child templates.

Here's the boilerplate to do that.

```
{% extends "base.html" %}
{% block content %}

PLACE HTML HERE

{% endblock}
```

The {% extends %} tag informs the templating engine that this template "extends" another template, base.html. This establishes the link between the parent and child templates.

**

That's it. Let's test this out to make sure nothing broke. Login. Logout. Test for errors. Cool.

**

We literally just scratched the surface on the power behind Jinja2. Like I said, I will show you much more around the 10th or 11th video in this series. If you do want to jump ahead, I encourage you to check out the blog post on Jinj2, which again you can find a link to in this videos description.

With our templates now in working order, we will move on to adding a database in the next video. Comment below if you have questions. Thanks for watching!
