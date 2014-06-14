python, flask, web development, python tutorial, unit tests, flask-testing

Introduction to Flask, Part 7 - Unit Tests

It's important to write tests for all code you write, especially when you're learning. Why? Tests reduce bugs in new features and reduce regressions in your existing code base as you add new features.

Flask comes equiped with a test client, which allows our tests to mimic actual client requests. So requests hit our routes which are handled by the views as they normally would, then the response is sent back to the actual test. In general, you write tests to check the response for correctness.

**

Activate your virtualenv. Open your code editor. Let's get to it.

Create a new file called tests.py.

Grab the boilerplate from the repo.

```
from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
```

Again, the test client is what we use to create a test app, mocking out the functionality of our current app. Think of it as an isolated app that we can use to send requests to and then test the responses, all outside the scope of our main app. We're using the unit test library to call the /login route, then checking that the response status code is 200.

Run the test:

```
python tests.py -v
```

***

And it passed.

We need to write tests to cover our entire app, and each test should test only one piece of functionality. Stop for a minute and, from an end user perspective, think about what our app does. The best way to do that is to actually go through our app as an end user, then determining each individual feature and then writing a test for it.

Fire up the server. Navigate to the login route.

Like I said, the best way to do this it to just go through your app, manually testing it, and think about how you can test each piece of functionality. In most cases, we'll either test the response status code or that the actual data returned contains text from the page. For example, in the case of the login route, we could test to ensure that the text "Please login" is part of the response. Let's add that test.

```
# Ensure that the login page loads correctly
def test_login_page_loads(self):
    tester = app.test_client(self)
    response = tester.get('/login')
    self.assertTrue(b'Please login' in response.data)
```

Again, after creating the test server, call the login route, then ensure that the text Please Login is part of the response.

Test again.

And it passes.

Why do you think that it's important to test the actual data rather than just a 200 reponse. Well, if you think about it, we don't know anything about the data returned if we test for a 200 response. It could be JSON. Or for all we know, it could be an entirely different page because we rendered the wrong template. So, if we test for actual text from the template, then we know that right template was rendered.

**

So, what else can we test on this page?

How about -

```
# Ensure login behaves correctly with correct credentials
# Ensure login behaves correctly with incorrect credentials
# Ensure logout behaves correctly
```

So that will be three different tests. First, let's jump into the Shell to figure out how to mock these requests.

```
>>> from app import app
>>> tester = app.test_client()
>>> response = tester.post('/login', data=dict(username="admin",password="admin"), follow_redirects = True)
>>> response
```

1. Import the app.
1. Create the test client.
1. So, we need to do a post request to the login route and pass in a username and password.
1. Then we should follow the redirects, since we need to test the page we're redirected to upon successful login which is the main page.
1. Now we should get a 200 response.

Cool. Now we can just test to ensure that text to that specific page is found within the response. We can see what to test by actually logging in.

Back to the browser. Alright - so we can test that "You were logged" in is part of the response.

Write the test -

```
# Ensure login behaves correctly with correct credentials
def test_correct_login(self):
    tester = app.test_client()
    response = tester.post(
        '/login',
        data=dict(username="admin", password="admin"),
        follow_redirects=True
    )
    self.assertIn(b'You were logged in', response.data)
```

1. Start with the function name.
1. Create the test client
1. Then hit the login route, passing in the correct user credentials.
1. Then assert that the text is in the response.

Test. Nice.

Now let's do the same thing for the next test. This will be similar. But what are we testing for? The response in the case of logging in with incorrect credentials.

Back to the browser. Try to login with incorrect credentials. So we want to ensure that "Invalid Credentials. Please try again." is part of the reponse.

```
# Ensure login behaves correctly with incorrect credentials
def test_incorrect_login(self):
    tester = app.test_client()
    response = tester.post(
        '/login',
        data=dict(username="wrong", password="wrong"),
        follow_redirects=True
    )
    self.assertIn(b'Invalid Credentials. Please try again.', response.data)
```

Test.

How about logging out?

```
# Ensure logout behaves correctly
def test_logout(self):
    tester = app.test_client()
    tester.post(
        '/login',
        data=dict(username="admin", password="admin"),
        follow_redirects=True
    )
    response = tester.get('/logout', follow_redirects=True)
    self.assertIn(b'You were logged out', response.data)
```

First we need to login, so let's just grab that from this previous test. Now write the response to logout.

Okay. Now let's test. All pass. Let's go back to sublime real quick. Take a look at those last three tests. They smell bad, meaning - there are problems with them. First there's redundency in the actual code. We can write some helper functions to DRY out our code so that we are not repeating code - but that's just  start. There's a few more issues, but they are a bit esoteric so I won't go over them. Since these test work, I'll leave them for now. We will be refactoring this in a futue video though.

Let's move on.

**

Go back the browser. What else do we need to test?

How about -

Ensure that the main page requires login

```
# Ensure that main page requires user login
def test_main_route_requires_login(self):
    tester = app.test_client()
    response = tester.get('/', follow_redirects=True)
    self.assertIn(b'You need to login first.', response.data)
```

A similar test would be to test that the logout page requires a user to be logged in to view. I'll let you write that test since it's so similar to the last test. Check the repo for the answer.

**

Finally, let's test that posts are shown on the main page.

```
# Ensure that posts show up on the main page
def test_posts_show_up_on_main_page(self):
    tester = app.test_client()
    response = tester.post(
        '/login',
        data=dict(username="admin", password="admin"),
        follow_redirects=True
    )
    self.assertIn(b'Hello from the shell', response.data)
```

One thing to be aware of here is that we are not using a test database for our tests, which is a big no-no. You never, ever want to mix test data with real data. Since we are not writing to the database, we can get away with it - but I will show you how to resolve this in a future video.

Likewise, notice how this test is testing whether a specific post is in the database. What happens if that data is removed? The test will fail of course. Thus, we actually should be adding data to the database in this test and then ensuring that the newly added data appears on the DOM. Again, I will save this for a future video.

**

I think that just about covers it. Did I miss anything? If so, first see if you can write a test for it, then comment below with a link to the code.

Next time I'll show you quickly how to deploy this app to Heroku before we start to scale out, building a production-quaity application. Thanks for watching!

