# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.story import Story  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFollowingController(BaseTestCase):
    """FollowingController integration test stubs"""

    def test_delete_follow_user_id_story_id(self):
        """Test case for delete_follow_user_id_story_id

        
        """
        response = self.client.open(
            '/following/{user_id}/{story_id}'.format(user_id=56, story_id='story_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_following_user_id(self):
        """Test case for get_following_user_id

        Your GET endpoint
        """
        response = self.client.open(
            '/following/{user_id}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_follow_user_id_story_id(self):
        """Test case for post_follow_user_id_story_id

        
        """
        response = self.client.open(
            '/following/{user_id}/{story_id}'.format(user_id=56, story_id='story_id_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
