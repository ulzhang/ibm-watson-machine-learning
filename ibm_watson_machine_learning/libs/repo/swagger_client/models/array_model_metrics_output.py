# coding: utf-8

"""
    IBM Watson Machine Learning REST API

    ## Authorization  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://ibm-watson-ml.mybluemix.net\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v2/identity/token `   ### Apache Spark Service Credentials  The IBM Watson Machine Learning co-operates with the Apache Spark as a Service to deploy pipeline models. For API methods requiring Apache Spark Service instance a custom header: `X-Spark-Service-Instance` with Service Credentials must be specified. The header value is a **base64 encoded** string with the Service Credentials JSON data.  [Example of API method requiring Apache Spark Service](https://console.ng.bluemix.net/docs/services/PredictiveModeling/index-gentopic1.html#pm_service_api_spark_batch) 

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  -----------------------------------------------------------------------------------------
#  (C) Copyright IBM Corp. 2017-2024.
#  https://opensource.org/licenses/BSD-3-Clause
#  -----------------------------------------------------------------------------------------

from pprint import pformat
from six import iteritems
import re


class ArrayModelMetricsOutput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, resources=None):
        """
        ArrayModelMetricsOutput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'resources': 'list[ModelMetrics]'
        }

        self.attribute_map = {
            'resources': 'resources'
        }

        self._resources = resources

    @property
    def resources(self):
        """
        Gets the resources of this ArrayModelMetricsOutput.


        :return: The resources of this ArrayModelMetricsOutput.
        :rtype: list[ModelMetrics]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this ArrayModelMetricsOutput.


        :param resources: The resources of this ArrayModelMetricsOutput.
        :type: list[ModelMetrics]
        """

        self._resources = resources

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
