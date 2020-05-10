import connexion
import six

from swagger_server.models.story import Story  # noqa: E501
from swagger_server import util


def delete_follow_user_id_story_id(user_id, story_id):  # noqa: E501
    """delete_follow_user_id_story_id

    User unfollows a Story. # noqa: E501

    :param user_id: 
    :type user_id: int
    :param story_id: 
    :type story_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_following_user_id(user_id):  # noqa: E501
    """Your GET endpoint

    Get all stories a user is following. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: List[Story]
    """
    return 'do some magic!'


def post_follow_user_id_story_id(user_id, story_id):  # noqa: E501
    """post_follow_user_id_story_id

    User follows a story. # noqa: E501

    :param user_id: 
    :type user_id: int
    :param story_id: 
    :type story_id: str

    :rtype: None
    """
    return 'do some magic!'
