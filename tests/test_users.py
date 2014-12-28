# tests/test_users.py


import unittest

from flask.ext.login import current_user
from flask import request

from base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):

    # Ensure user can register
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Michael', email='michael@realpython.com',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "Michael")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='michael@realpython.com').first()
            self.assertTrue(str(user) == '<name - Michael>')

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Michael', email='michael',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertIn(b'/register/', request.url)

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="admin", password='admin'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))


class UserViewsTests(BaseTestCase):

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were logged out', response.data)
            self.assertFalse(current_user.is_active())

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


if __name__ == '__main__':
    unittest.main()
