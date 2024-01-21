# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class StreamOutputInternal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, connection=None, target=None):
        """
        StreamOutputInternal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'connection': 'dict(str, str)',
            'target': 'dict(str, str)'
        }

        self.attribute_map = {
            'connection': 'connection',
            'target': 'target'
        }

        self._connection = connection
        self._target = target

    @property
    def connection(self):
        """
        Gets the connection of this StreamOutputInternal.
        service credential of output datasource (eg messagehu/s3/objectstore)

        :return: The connection of this StreamOutputInternal.
        :rtype: dict(str, str)
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this StreamOutputInternal.
        service credential of output datasource (eg messagehu/s3/objectstore)

        :param connection: The connection of this StreamOutputInternal.
        :type: dict(str, str)
        """

        self._connection = connection

    @property
    def target(self):
        """
        Gets the target of this StreamOutputInternal.
        Additional configuration for the connection object

        :return: The target of this StreamOutputInternal.
        :rtype: dict(str, str)
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this StreamOutputInternal.
        Additional configuration for the connection object

        :param target: The target of this StreamOutputInternal.
        :type: dict(str, str)
        """

        self._target = target

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
