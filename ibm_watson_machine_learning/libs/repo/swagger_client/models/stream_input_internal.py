# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class StreamInputInternal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connection=None, source=None):
        """
        StreamInputInternal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connection': 'dict(str, str)',
            'source': 'dict(str, str)'
        }

        self.attribute_map = {
            'connection': 'connection',
            'source': 'source'
        }

        self._connection = connection
        self._source = source

    @property
    def connection(self):
        """
        Gets the connection of this StreamInputInternal.
        Service credential of input  messagehub

        :return: The connection of this StreamInputInternal.
        :rtype: dict(str, str)
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this StreamInputInternal.
        Service credential of input  messagehub

        :param connection: The connection of this StreamInputInternal.
        :type: dict(str, str)
        """

        self._connection = connection

    @property
    def source(self):
        """
        Gets the source of this StreamInputInternal.
        Additional configuration for the connection object

        :return: The source of this StreamInputInternal.
        :rtype: dict(str, str)
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this StreamInputInternal.
        Additional configuration for the connection object

        :param source: The source of this StreamInputInternal.
        :type: dict(str, str)
        """

        self._source = source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
