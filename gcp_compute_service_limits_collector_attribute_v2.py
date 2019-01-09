# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class GcpComputeServiceLimitsCollectorAttributeV2(CollectorAttribute):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'period': 'int'
    }

    attribute_map = {
        'name': 'name',
        'period': 'period'
    }

    def __init__(self, name=None, period=None):  # noqa: E501
        """GcpComputeServiceLimitsCollectorAttributeV2 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._period = None
        self.discriminator = None

        self.name = name
        if period is not None:
            self.period = period

    @property
    def name(self):
        """Gets the name of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501


        :return: The name of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GcpComputeServiceLimitsCollectorAttributeV2.


        :param name: The name of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def period(self):
        """Gets the period of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501


        :return: The period of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this GcpComputeServiceLimitsCollectorAttributeV2.


        :param period: The period of this GcpComputeServiceLimitsCollectorAttributeV2.  # noqa: E501
        :type: int
        """

        self._period = period

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GcpComputeServiceLimitsCollectorAttributeV2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GcpComputeServiceLimitsCollectorAttributeV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
