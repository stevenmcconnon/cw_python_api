# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.story import Story  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStoriesController(BaseTestCase):
    """StoriesController integration test stubs"""

    def test_delete_story_story_id(self):
        """Test case for delete_story_story_id

        
        """
        response = self.client.open(
            '/story/{story_id}'.format(story_id='story_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_get_story_story_id(self):
        """Test case for get_story_story_id

        Your GET endpoint
        """
        response = self.client.open(
            '/story/{story_id}'.format(story_id='story_id_example'),
            method='GET')
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

    def test_post_story(self):
        """Test case for post_story

        Create Story
        """
        body = Story()
        response = self.client.open(
            '/story/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
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

    def test_put_story_story_id(self):
        """Test case for put_story_story_id

        
        """
        body = None
        response = self.client.open(
            '/story/{story_id}'.format(story_id='story_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
