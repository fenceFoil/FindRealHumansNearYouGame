# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Likes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, source_player_id: int=None, dest_player_id: int=None, round_num: int=None, action: str=None):  # noqa: E501
        """Likes - a model defined in Swagger

        :param source_player_id: The source_player_id of this Likes.  # noqa: E501
        :type source_player_id: int
        :param dest_player_id: The dest_player_id of this Likes.  # noqa: E501
        :type dest_player_id: int
        :param round_num: The round_num of this Likes.  # noqa: E501
        :type round_num: int
        :param action: The action of this Likes.  # noqa: E501
        :type action: str
        """
        self.swagger_types = {
            'source_player_id': int,
            'dest_player_id': int,
            'round_num': int,
            'action': str
        }

        self.attribute_map = {
            'source_player_id': 'source_player_id',
            'dest_player_id': 'dest_player_id',
            'round_num': 'round_num',
            'action': 'action'
        }

        self._source_player_id = source_player_id
        self._dest_player_id = dest_player_id
        self._round_num = round_num
        self._action = action

    @classmethod
    def from_dict(cls, dikt) -> 'Likes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The likes of this Likes.  # noqa: E501
        :rtype: Likes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source_player_id(self) -> int:
        """Gets the source_player_id of this Likes.


        :return: The source_player_id of this Likes.
        :rtype: int
        """
        return self._source_player_id

    @source_player_id.setter
    def source_player_id(self, source_player_id: int):
        """Sets the source_player_id of this Likes.


        :param source_player_id: The source_player_id of this Likes.
        :type source_player_id: int
        """

        self._source_player_id = source_player_id

    @property
    def dest_player_id(self) -> int:
        """Gets the dest_player_id of this Likes.


        :return: The dest_player_id of this Likes.
        :rtype: int
        """
        return self._dest_player_id

    @dest_player_id.setter
    def dest_player_id(self, dest_player_id: int):
        """Sets the dest_player_id of this Likes.


        :param dest_player_id: The dest_player_id of this Likes.
        :type dest_player_id: int
        """

        self._dest_player_id = dest_player_id

    @property
    def round_num(self) -> int:
        """Gets the round_num of this Likes.


        :return: The round_num of this Likes.
        :rtype: int
        """
        return self._round_num

    @round_num.setter
    def round_num(self, round_num: int):
        """Sets the round_num of this Likes.


        :param round_num: The round_num of this Likes.
        :type round_num: int
        """

        self._round_num = round_num

    @property
    def action(self) -> str:
        """Gets the action of this Likes.

          # noqa: E501

        :return: The action of this Likes.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action: str):
        """Sets the action of this Likes.

          # noqa: E501

        :param action: The action of this Likes.
        :type action: str
        """

        self._action = action