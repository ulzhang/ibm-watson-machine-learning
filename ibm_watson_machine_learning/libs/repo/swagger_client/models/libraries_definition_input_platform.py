# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems


class LibrariesDefinitionInputPlatform(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, versions=None):
        """
        LibrariesDefinitionInputPlatform - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'versions': 'list(str)'
        }

        self.attribute_map = {
            'name': 'name',
            'versions': 'versions'
        }

        self._name = name
        self._versions = versions

    @property
    def name(self):
        """
        Gets the name of this LibrariesDefinitionInputPlatform.


        :return: The name of this LibrariesDefinitionInputPlatform.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LibrariesDefinitionInputPlatform.


        :param name: The name of this LibrariesDefinitionInputPlatform.
        :type: str
        """
        self._name = name

    @property
    def versions(self):
        """
        Gets the versions of this LibrariesDefinitionInputPlatform.


        :return: The versions of this LibrariesDefinitionInputPlatform.
        :rtype: str
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this LibrariesDefinitionInputPlatform.


        :param versions: The version of this LibrariesDefinitionInputPlatform.
        :type: list(str)
        """
        self._versions = versions

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
