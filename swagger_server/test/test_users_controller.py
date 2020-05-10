# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_delete_story_user(self):
        """Test case for delete_story_user

        
        """
        response = self.client.open(
            '/story_user/{story_id}/{user_id}'.format(story_id=56, user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_story_users(self):
        """Test case for delete_story_users

        
        """
        response = self.client.open(
            '/story_users/{story_id}'.format(story_id='story_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        
        """
        query_string = [('user_id2', 56)]
        response = self.client.open(
            '/user/{user_id}'.format(user_id='user_id_example'),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_story_users(self):
        """Test case for get_story_users

        Your GET endpoint
        """
        response = self.client.open(
            '/story_users/{story_id}'.format(story_id='story_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user(self):
        """Test case for get_user

        Your GET endpoint
        """
        response = self.client.open(
            '/user/{user_id}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_story_user(self):
        """Test case for post_story_user

        
        """
        body = None
        response = self.client.open(
            '/story_user/{story_id}/{user_id}'.format(story_id=56, user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_user(self):
        """Test case for post_user

        
        """
        body = User()
        response = self.client.open(
            '/user/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_user(self):
        """Test case for put_user

        
        """
        body = User()
        response = self.client.open(
            '/user/{user_id}'.format(user_id='user_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
