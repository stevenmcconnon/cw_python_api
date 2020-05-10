# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Story(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, title: str=None, language: str=None, private: bool=None, last_updated: str=None):  # noqa: E501
        """Story - a model defined in Swagger

        :param id: The id of this Story.  # noqa: E501
        :type id: str
        :param title: The title of this Story.  # noqa: E501
        :type title: str
        :param language: The language of this Story.  # noqa: E501
        :type language: str
        :param private: The private of this Story.  # noqa: E501
        :type private: bool
        :param last_updated: The last_updated of this Story.  # noqa: E501
        :type last_updated: str
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'language': str,
            'private': bool,
            'last_updated': str
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'language': 'language',
            'private': 'private',
            'last_updated': 'last_updated'
        }
        self._id = id
        self._title = title
        self._language = language
        self._private = private
        self._last_updated = last_updated

    @classmethod
    def from_dict(cls, dikt) -> 'Story':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Story of this Story.  # noqa: E501
        :rtype: Story
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Story.


        :return: The id of this Story.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Story.


        :param id: The id of this Story.
        :type id: str
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Story.


        :return: The title of this Story.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Story.


        :param title: The title of this Story.
        :type title: str
        """

        self._title = title

    @property
    def language(self) -> str:
        """Gets the language of this Story.


        :return: The language of this Story.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language: str):
        """Sets the language of this Story.


        :param language: The language of this Story.
        :type language: str
        """

        self._language = language

    @property
    def private(self) -> bool:
        """Gets the private of this Story.


        :return: The private of this Story.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private: bool):
        """Sets the private of this Story.


        :param private: The private of this Story.
        :type private: bool
        """

        self._private = private

    @property
    def last_updated(self) -> str:
        """Gets the last_updated of this Story.

        Date  # noqa: E501

        :return: The last_updated of this Story.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated: str):
        """Sets the last_updated of this Story.

        Date  # noqa: E501

        :param last_updated: The last_updated of this Story.
        :type last_updated: str
        """

        self._last_updated = last_updated
