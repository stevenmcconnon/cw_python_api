import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def delete_friend(friend_id, user_id):  # noqa: E501
    """Remove a Friend

    Remove a friend relationship. # noqa: E501

    :param friend_id: 
    :type friend_id: str
    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def delete_friends_user_id(user_id):  # noqa: E501
    """Delete all Friends of User

    Delete all friends of user. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_friends(user_id):  # noqa: E501
    """Get all Friends of User

    Get all friends of user. # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: List[User]
    """
    return 'do some magic!'


def post_friend(friend_id, user_id):  # noqa: E501
    """Add New Friend

    Add a friend relationship. # noqa: E501

    :param friend_id: 
    :type friend_id: str
    :param user_id: 
    :type user_id: str

    :rtype: None
    """
    return 'do some magic!'
