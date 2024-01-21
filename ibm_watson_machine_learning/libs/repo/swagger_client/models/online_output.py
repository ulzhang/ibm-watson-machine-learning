# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class OnlineOutput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, metadata=None, entity=None):
        """
        OnlineOutput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'metadata': 'MetaObjectMetadata',
            'entity': 'object'
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'entity': 'entity'
        }

        self._metadata = metadata
        self._entity = entity

    @property
    def metadata(self):
        """
        Gets the metadata of this OnlineOutput.


        :return: The metadata of this OnlineOutput.
        :rtype: MetaObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this OnlineOutput.


        :param metadata: The metadata of this OnlineOutput.
        :type: MetaObjectMetadata
        """

        self._metadata = metadata

    @property
    def entity(self):
        """
        Gets the entity of this OnlineOutput.


        :return: The entity of this OnlineOutput.
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this OnlineOutput.


        :param entity: The entity of this OnlineOutput.
        :type: object
        """

        self._entity = entity

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
