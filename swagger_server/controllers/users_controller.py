import connexion
import six

from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


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


def delete_user(user_id, user_id2=None):  # noqa: E501
    """delete_user

    Delete a user by user_id. # noqa: E501

    :param user_id: 
    :type user_id: str
    :param user_id2: 
    :type user_id2: int

    :rtype: None
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


def get_user(user_id):  # noqa: E501
    """Your GET endpoint

    Get a User by user_id. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: User
    """
    return 'do some magic3!'


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


def post_user(body=None):  # noqa: E501
    """post_user

    Creates a user, returns a user_id. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_user(user_id, body=None):  # noqa: E501
    """put_user

    Update a User by user_id. # noqa: E501

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
