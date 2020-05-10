# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, story_id: int=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param story_id: The story_id of this InlineResponse200.  # noqa: E501
        :type story_id: int
        """
        self.swagger_types = {
            'story_id': int
        }

        self.attribute_map = {
            'story_id': 'story_id'
        }
        self._story_id = story_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def story_id(self) -> int:
        """Gets the story_id of this InlineResponse200.


        :return: The story_id of this InlineResponse200.
        :rtype: int
        """
        return self._story_id

    @story_id.setter
    def story_id(self, story_id: int):
        """Sets the story_id of this InlineResponse200.


        :param story_id: The story_id of this InlineResponse200.
        :type story_id: int
        """

        self._story_id = story_id
