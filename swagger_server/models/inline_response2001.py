# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, user_id: int=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param user_id: The user_id of this InlineResponse2001.  # noqa: E501
        :type user_id: int
        """
        self.swagger_types = {
            'user_id': int
        }

        self.attribute_map = {
            'user_id': 'user_id'
        }
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> int:
        """Gets the user_id of this InlineResponse2001.


        :return: The user_id of this InlineResponse2001.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this InlineResponse2001.


        :param user_id: The user_id of this InlineResponse2001.
        :type user_id: int
        """

        self._user_id = user_id