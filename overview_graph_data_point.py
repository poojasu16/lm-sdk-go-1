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


class OverviewGraphDataPoint(object):
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
        'aggregate_method': 'str',
        'data_point_name': 'str',
        'data_point_id': 'int',
        'consolidate_func': 'int'
    }

    attribute_map = {
        'aggregate_method': 'aggregateMethod',
        'data_point_name': 'dataPointName',
        'data_point_id': 'dataPointId',
        'consolidate_func': 'consolidateFunc'
    }

    def __init__(self, aggregate_method=None, data_point_name=None, data_point_id=None, consolidate_func=None):  # noqa: E501
        """OverviewGraphDataPoint - a model defined in Swagger"""  # noqa: E501

        self._aggregate_method = None
        self._data_point_name = None
        self._data_point_id = None
        self._consolidate_func = None
        self.discriminator = None

        if aggregate_method is not None:
            self.aggregate_method = aggregate_method
        if data_point_name is not None:
            self.data_point_name = data_point_name
        if data_point_id is not None:
            self.data_point_id = data_point_id
        if consolidate_func is not None:
            self.consolidate_func = consolidate_func

    @property
    def aggregate_method(self):
        """Gets the aggregate_method of this OverviewGraphDataPoint.  # noqa: E501


        :return: The aggregate_method of this OverviewGraphDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._aggregate_method

    @aggregate_method.setter
    def aggregate_method(self, aggregate_method):
        """Sets the aggregate_method of this OverviewGraphDataPoint.


        :param aggregate_method: The aggregate_method of this OverviewGraphDataPoint.  # noqa: E501
        :type: str
        """

        self._aggregate_method = aggregate_method

    @property
    def data_point_name(self):
        """Gets the data_point_name of this OverviewGraphDataPoint.  # noqa: E501


        :return: The data_point_name of this OverviewGraphDataPoint.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this OverviewGraphDataPoint.


        :param data_point_name: The data_point_name of this OverviewGraphDataPoint.  # noqa: E501
        :type: str
        """

        self._data_point_name = data_point_name

    @property
    def data_point_id(self):
        """Gets the data_point_id of this OverviewGraphDataPoint.  # noqa: E501


        :return: The data_point_id of this OverviewGraphDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this OverviewGraphDataPoint.


        :param data_point_id: The data_point_id of this OverviewGraphDataPoint.  # noqa: E501
        :type: int
        """

        self._data_point_id = data_point_id

    @property
    def consolidate_func(self):
        """Gets the consolidate_func of this OverviewGraphDataPoint.  # noqa: E501


        :return: The consolidate_func of this OverviewGraphDataPoint.  # noqa: E501
        :rtype: int
        """
        return self._consolidate_func

    @consolidate_func.setter
    def consolidate_func(self, consolidate_func):
        """Sets the consolidate_func of this OverviewGraphDataPoint.


        :param consolidate_func: The consolidate_func of this OverviewGraphDataPoint.  # noqa: E501
        :type: int
        """

        self._consolidate_func = consolidate_func

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
        if issubclass(OverviewGraphDataPoint, dict):
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
        if not isinstance(other, OverviewGraphDataPoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
