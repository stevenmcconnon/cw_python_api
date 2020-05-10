# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFriendsController(BaseTestCase):
    """FriendsController integration test stubs"""

    def test_delete_friend(self):
        """Test case for delete_friend

        Remove a Friend
        """
        response = self.client.open(
            '/friend/{user_id}/{friend_id}'.format(friend_id='friend_id_example', user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_friends_user_id(self):
        """Test case for delete_friends_user_id

        Delete all Friends of User
        """
        response = self.client.open(
            '/friends/{user_id}'.format(user_id='user_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_friends(self):
        """Test case for get_friends

        Get all Friends of User
        """
        response = self.client.open(
            '/friends/{user_id}'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_friend(self):
        """Test case for post_friend

        Add New Friend
        """
        response = self.client.open(
            '/friend/{user_id}/{friend_id}'.format(friend_id='friend_id_example', user_id='user_id_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
