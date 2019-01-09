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


class Macro(object):
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
        'variable': 'str',
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'variable': 'variable',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, variable=None, description=None, value=None):  # noqa: E501
        """Macro - a model defined in Swagger"""  # noqa: E501

        self._variable = None
        self._description = None
        self._value = None
        self.discriminator = None

        self.variable = variable
        if description is not None:
            self.description = description
        self.value = value

    @property
    def variable(self):
        """Gets the variable of this Macro.  # noqa: E501


        :return: The variable of this Macro.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this Macro.


        :param variable: The variable of this Macro.  # noqa: E501
        :type: str
        """
        if variable is None:
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501

        self._variable = variable

    @property
    def description(self):
        """Gets the description of this Macro.  # noqa: E501


        :return: The description of this Macro.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Macro.


        :param description: The description of this Macro.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this Macro.  # noqa: E501


        :return: The value of this Macro.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Macro.


        :param value: The value of this Macro.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(Macro, dict):
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
        if not isinstance(other, Macro):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
