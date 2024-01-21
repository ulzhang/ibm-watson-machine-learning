# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class SpaceModels(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, href=None, id=None):
        """
        SpaceModels - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute href
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute href
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'href': 'str',
            'id' : 'str'
        }

        self.attribute_map = {
            'href': 'href',
            'id': 'id'
        }

        self._href = href
        self._id = id

    @property
    def href(self):
        """
        Gets the href of this SpaceModels.


        :return: The href of this SpaceModels.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this SpaceModels.


        :param href: The href of this SpaceModels.
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """
        Gets the id of this PipelinesModels.


        :return: The id of this PipelinesModels.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelinesModels.


        :param href: The id of this PipelinesModels.
        :type: str
        """

        self._id = id

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
