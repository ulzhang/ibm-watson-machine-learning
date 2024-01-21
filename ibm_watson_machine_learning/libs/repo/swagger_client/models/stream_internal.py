# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class StreamInternal(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, artifact_version_href=None, input=None, output=None):
        """
        StreamInternal - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'artifact_version_href': 'str',
            'input': 'StreamInputInternal',
            'output': 'StreamOutputInternal'
        }

        self.attribute_map = {
            'name': 'name',
            'artifact_version_href': 'artifactVersionHref',
            'input': 'input',
            'output': 'output'
        }

        self._name = name
        self._artifact_version_href = artifact_version_href
        self._input = input
        self._output = output

    @property
    def name(self):
        """
        Gets the name of this StreamInternal.
        The application name (need not be unique)

        :return: The name of this StreamInternal.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StreamInternal.
        The application name (need not be unique)

        :param name: The name of this StreamInternal.
        :type: str
        """

        self._name = name

    @property
    def artifact_version_href(self):
        """
        Gets the artifact_version_href of this StreamInternal.
        Href to the artifact version that is going to be deployed

        :return: The artifact_version_href of this StreamInternal.
        :rtype: str
        """
        return self._artifact_version_href

    @artifact_version_href.setter
    def artifact_version_href(self, artifact_version_href):
        """
        Sets the artifact_version_href of this StreamInternal.
        Href to the artifact version that is going to be deployed

        :param artifact_version_href: The artifact_version_href of this StreamInternal.
        :type: str
        """

        self._artifact_version_href = artifact_version_href

    @property
    def input(self):
        """
        Gets the input of this StreamInternal.


        :return: The input of this StreamInternal.
        :rtype: StreamInputInternal
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this StreamInternal.


        :param input: The input of this StreamInternal.
        :type: StreamInputInternal
        """

        self._input = input

    @property
    def output(self):
        """
        Gets the output of this StreamInternal.


        :return: The output of this StreamInternal.
        :rtype: StreamOutputInternal
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this StreamInternal.


        :param output: The output of this StreamInternal.
        :type: StreamOutputInternal
        """

        self._output = output

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
