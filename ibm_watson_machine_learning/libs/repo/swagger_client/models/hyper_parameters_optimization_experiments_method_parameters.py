# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class HyperParametersOptimizationExperimentsMethodParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, string_value=None, double_value=None, int_value=None):
        """
        HyperParametersOptimizationExperimentsMethodParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """

        self.swagger_types = {
            'name': 'str',
            'string_value': 'str',
            'double_value': 'float',
            'int_value': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'string_value': 'string_value',
            'double_value': 'double_value',
            'int_value': 'int_value'
        }

        self._name = name
        self._string_value = string_value
        self._double_value = double_value
        self._int_value = int_value

    @property
    def name(self):
        """
        Gets the name of this HyperParametersOptimizationExperimentsMethodParameters.


        :return: The name of this HyperParametersOptimizationExperimentsMethodParameters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperParametersOptimizationExperimentsMethodParameters.


        :param name: The name of this HyperParametersOptimizationExperimentsMethodParameters.
        :type: str
        """

        self._name = name

    @property
    def string_value(self):
        """
        Gets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :return: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """
        Sets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :param value: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :type: str
        """

        self._string_value = string_value

    @property
    def double_value(self):
        """
        Gets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :return: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :rtype: float
        """
        return self._double_value

    @double_value.setter
    def double_value(self, double_value):
        """
        Sets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :param value: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :type: float
        """

        self._double_value = double_value

    @property
    def int_value(self):
        """
        Gets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :return: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :rtype: int
        """
        return self._int_value

    @int_value.setter
    def int_value(self, int_value):
        """
        Sets the value of this HyperParametersOptimizationExperimentsMethodParameters.


        :param value: The value of this HyperParametersOptimizationExperimentsMethodParameters.
        :type: int
        """

        self._int_value = int_value

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
