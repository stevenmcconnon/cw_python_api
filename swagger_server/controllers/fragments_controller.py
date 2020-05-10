import connexion
import six

from swagger_server.models.story_fragment import StoryFragment  # noqa: E501
from swagger_server import util


def delete_fragment(fragment_id):  # noqa: E501
    """Delete a Story Fragment

    Delete Fragment from Story. # noqa: E501

    :param fragment_id: 
    :type fragment_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_fragments_story_id(story_id):  # noqa: E501
    """Your GET endpoint

    Get all Story Fragments for story_id. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: List[StoryFragment]
    """
    return 'do some magic!'


def post_fragments_story_id(story_id):  # noqa: E501
    """post_fragments_story_id

    Add new Fragment to story. # noqa: E501

    :param story_id: 
    :type story_id: str

    :rtype: None
    """
    return 'do some magic!'


def put_fragment(fragment_id, body=None):  # noqa: E501
    """Update Story Fragment

    Update a Story Fragment. # noqa: E501

    :param fragment_id: 
    :type fragment_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = StoryFragment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
