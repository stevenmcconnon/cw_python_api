import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.story import Story  # noqa: E501
from swagger_server import util


def delete_story_story_id(story_id):  # noqa: E501
    """delete_story_story_id

    Delete a story by story_id. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_story_user(story_id, user_id):  # noqa: E501
    """delete_story_user

    Removes a User from a Story. # noqa: E501

    :param story_id: 
    :type story_id: int
    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_story_users(story_id):  # noqa: E501
    """delete_story_users

    Delete all users for a story. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_story_story_id(story_id):  # noqa: E501
    """Your GET endpoint

    Get a story by story_id. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: Story
    """
    return 'do some magic!'


def get_story_users(story_id):  # noqa: E501
    """Your GET endpoint

    Returns a list of user_id&#x27;s for a private story. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def post_story(body=None):  # noqa: E501
    """Create Story

    Create a new Story, get back a story_id. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = Story.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_story_user(story_id, user_id, body=None):  # noqa: E501
    """post_story_user

    Add user to story. # noqa: E501

    :param story_id: 
    :type story_id: int
    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_story_story_id(story_id, body=None):  # noqa: E501
    """put_story_story_id

    Update a Story by story_id. # noqa: E501

    :param story_id: 
    :type story_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Story.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
