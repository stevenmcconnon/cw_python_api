# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.story_fragment import StoryFragment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFragmentsController(BaseTestCase):
    """FragmentsController integration test stubs"""

    def test_delete_fragment(self):
        """Test case for delete_fragment

        Delete a Story Fragment
        """
        response = self.client.open(
            '/fragment/{fragment_id}'.format(fragment_id='fragment_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_fragments_story_id(self):
        """Test case for get_fragments_story_id

        Your GET endpoint
        """
        response = self.client.open(
            '/fragments/{story_id}'.format(story_id='story_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_fragments_story_id(self):
        """Test case for post_fragments_story_id

        
        """
        response = self.client.open(
            '/fragments/{story_id}'.format(story_id='story_id_example'),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_fragment(self):
        """Test case for put_fragment

        Update Story Fragment
        """
        body = StoryFragment()
        response = self.client.open(
            '/fragment/{fragment_id}'.format(fragment_id='fragment_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
