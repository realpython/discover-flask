# tests/test_blog.py

import unittest

from base import BaseTestCase


class BlogPostTests(BaseTestCase):

    # Ensure a logged in user can add a new post
    def test_user_can_post(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.post(
                '/',
                data=dict(title="test", description="test"),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'New entry was successfully posted. Thanks.',
                          response.data)


if __name__ == '__main__':
    unittest.main()
