# coding: utf-8

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class EvaluationDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, method=None, metrics=None):
        """
        EvaluationDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'method': 'str',
            'metrics': 'list[EvaluationDefinitionMetrics]'
        }

        self.attribute_map = {
            'method': 'method',
            'metrics': 'metrics'
        }

        self._method = method
        self._metrics = metrics

    @property
    def method(self):
        """
        Gets the method of this EvaluationDefinition.
        The name of the evaluation algorithm

        :return: The method of this EvaluationDefinition.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this EvaluationDefinition.
        The name of the evaluation algorithm

        :param method: The method of this EvaluationDefinition.
        :type: str
        """

        self._method = method

    @property
    def metrics(self):
        """
        Gets the metrics of this EvaluationDefinition.


        :return: The metrics of this EvaluationDefinition.
        :rtype: list[EvaluationDefinitionMetrics]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this EvaluationDefinition.


        :param metrics: The metrics of this EvaluationDefinition.
        :type: list[EvaluationDefinitionMetrics]
        """

        self._metrics = metrics

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
