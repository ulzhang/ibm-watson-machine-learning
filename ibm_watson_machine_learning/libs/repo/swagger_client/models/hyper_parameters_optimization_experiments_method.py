# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class HyperParametersOptimizationExperimentsMethod(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, parameters=None):
        """
        HyperParametersOptimizationExperimentsMethod - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'parameters': 'list[HyperParametersOptimizationExperimentsMethodParameters]'
        }

        self.attribute_map = {
            'name': 'name',
            'parameters': 'parameters'
        }

        self._name = name
        self._parameters = parameters

    @property
    def name(self):
        """
        Gets the name of this HyperParametersOptimizationExperimentsMethod.


        :return: The name of this HyperParametersOptimizationExperimentsMethod.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperParametersOptimizationExperimentsMethod.


        :param name: The name of this HyperParametersOptimizationExperimentsMethod.
        :type: str
        """
        allowed_values = ["random", "rbfopt", "hyperband", "bandit"]
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def parameters(self):
        """
        Gets the parameters of this HyperParametersOptimizationExperimentsMethod.


        :return: The parameters of this HyperParametersOptimizationExperimentsMethod.
        :rtype: list[HyperParametersOptimizationExperimentsMethodParameters]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this HyperParametersOptimizationExperimentsMethod.


        :param parameters: The parameters of this HyperParametersOptimizationExperimentsMethod.
        :type: list[HyperParametersOptimizationExperimentsMethodParameters]
        """

        self._parameters = parameters

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
