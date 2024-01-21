# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class DeployInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, artifact_version_href=None, name=None):
        """
        DeployInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'artifact_version_href': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'artifact_version_href': 'artifactVersionHref',
            'name': 'name'
        }

        self._artifact_version_href = artifact_version_href
        self._name = name

    @property
    def artifact_version_href(self):
        """
        Gets the artifact_version_href of this DeployInput.
        Href to the artifact version that is going to be deployed

        :return: The artifact_version_href of this DeployInput.
        :rtype: str
        """
        return self._artifact_version_href

    @artifact_version_href.setter
    def artifact_version_href(self, artifact_version_href):
        """
        Sets the artifact_version_href of this DeployInput.
        Href to the artifact version that is going to be deployed

        :param artifact_version_href: The artifact_version_href of this DeployInput.
        :type: str
        """

        self._artifact_version_href = artifact_version_href

    @property
    def name(self):
        """
        Gets the name of this DeployInput.
        user-friendly name for the deployment

        :return: The name of this DeployInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeployInput.
        user-friendly name for the deployment

        :param name: The name of this DeployInput.
        :type: str
        """

        self._name = name

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
