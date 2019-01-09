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

from logicmonitor_sdk.models.dynamic_table_widget_column import DynamicTableWidgetColumn  # noqa: F401,E501
from logicmonitor_sdk.models.dynamic_table_widget_row import DynamicTableWidgetRow  # noqa: F401,E501
from logicmonitor_sdk.models.table_widget_forecast_configuration import TableWidgetForecastConfiguration  # noqa: F401,E501
from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501


class DynamicTableWidget(Widget):
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
        'last_updated_by': 'str',
        'user_permission': 'str',
        'dashboard_id': 'int',
        'name': 'str',
        'description': 'str',
        'last_updated_on': 'int',
        'theme': 'str',
        'interval': 'int',
        'id': 'int',
        'type': 'str',
        'timescale': 'str',
        'data_source_id': 'int',
        'top_x': 'int',
        'data_source_full_name': 'str',
        'columns': 'list[DynamicTableWidgetColumn]',
        'sort_order': 'str',
        'forecast': 'TableWidgetForecastConfiguration',
        'rows': 'list[DynamicTableWidgetRow]'
    }

    attribute_map = {
        'last_updated_by': 'lastUpdatedBy',
        'user_permission': 'userPermission',
        'dashboard_id': 'dashboardId',
        'name': 'name',
        'description': 'description',
        'last_updated_on': 'lastUpdatedOn',
        'theme': 'theme',
        'interval': 'interval',
        'id': 'id',
        'type': 'type',
        'timescale': 'timescale',
        'data_source_id': 'dataSourceId',
        'top_x': 'topX',
        'data_source_full_name': 'dataSourceFullName',
        'columns': 'columns',
        'sort_order': 'sortOrder',
        'forecast': 'forecast',
        'rows': 'rows'
    }

    def __init__(self, last_updated_by=None, user_permission=None, dashboard_id=None, name=None, description=None, last_updated_on=None, theme=None, interval=None, id=None, type=None, timescale=None, data_source_id=None, top_x=None, data_source_full_name=None, columns=None, sort_order=None, forecast=None, rows=None):  # noqa: E501
        """DynamicTableWidget - a model defined in Swagger"""  # noqa: E501

        self._last_updated_by = None
        self._user_permission = None
        self._dashboard_id = None
        self._name = None
        self._description = None
        self._last_updated_on = None
        self._theme = None
        self._interval = None
        self._id = None
        self._type = None
        self._timescale = None
        self._data_source_id = None
        self._top_x = None
        self._data_source_full_name = None
        self._columns = None
        self._sort_order = None
        self._forecast = None
        self._rows = None
        self.discriminator = None

        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if user_permission is not None:
            self.user_permission = user_permission
        self.dashboard_id = dashboard_id
        self.name = name
        if description is not None:
            self.description = description
        if last_updated_on is not None:
            self.last_updated_on = last_updated_on
        if theme is not None:
            self.theme = theme
        if interval is not None:
            self.interval = interval
        if id is not None:
            self.id = id
        self.type = type
        if timescale is not None:
            self.timescale = timescale
        self.data_source_id = data_source_id
        if top_x is not None:
            self.top_x = top_x
        if data_source_full_name is not None:
            self.data_source_full_name = data_source_full_name
        self.columns = columns
        if sort_order is not None:
            self.sort_order = sort_order
        if forecast is not None:
            self.forecast = forecast
        self.rows = rows

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this DynamicTableWidget.  # noqa: E501

        The user that last updated the widget  # noqa: E501

        :return: The last_updated_by of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this DynamicTableWidget.

        The user that last updated the widget  # noqa: E501

        :param last_updated_by: The last_updated_by of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def user_permission(self):
        """Gets the user_permission of this DynamicTableWidget.  # noqa: E501

        The permission level of the user who last modified the widget  # noqa: E501

        :return: The user_permission of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this DynamicTableWidget.

        The permission level of the user who last modified the widget  # noqa: E501

        :param user_permission: The user_permission of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this DynamicTableWidget.  # noqa: E501

        The id of the dashboard the widget belongs to  # noqa: E501

        :return: The dashboard_id of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this DynamicTableWidget.

        The id of the dashboard the widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this DynamicTableWidget.  # noqa: E501
        :type: int
        """
        if dashboard_id is None:
            raise ValueError("Invalid value for `dashboard_id`, must not be `None`")  # noqa: E501

        self._dashboard_id = dashboard_id

    @property
    def name(self):
        """Gets the name of this DynamicTableWidget.  # noqa: E501

        The name of the widget  # noqa: E501

        :return: The name of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DynamicTableWidget.

        The name of the widget  # noqa: E501

        :param name: The name of this DynamicTableWidget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DynamicTableWidget.  # noqa: E501

        The description of the widget  # noqa: E501

        :return: The description of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DynamicTableWidget.

        The description of the widget  # noqa: E501

        :param description: The description of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this DynamicTableWidget.  # noqa: E501

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :return: The last_updated_on of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this DynamicTableWidget.

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :param last_updated_on: The last_updated_on of this DynamicTableWidget.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def theme(self):
        """Gets the theme of this DynamicTableWidget.  # noqa: E501

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :return: The theme of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this DynamicTableWidget.

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :param theme: The theme of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def interval(self):
        """Gets the interval of this DynamicTableWidget.  # noqa: E501

        The refresh interval of the widget, in minutes  # noqa: E501

        :return: The interval of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DynamicTableWidget.

        The refresh interval of the widget, in minutes  # noqa: E501

        :param interval: The interval of this DynamicTableWidget.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def id(self):
        """Gets the id of this DynamicTableWidget.  # noqa: E501

        The Id of the widget  # noqa: E501

        :return: The id of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DynamicTableWidget.

        The Id of the widget  # noqa: E501

        :param id: The id of this DynamicTableWidget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this DynamicTableWidget.  # noqa: E501

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :return: The type of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DynamicTableWidget.

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :param type: The type of this DynamicTableWidget.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def timescale(self):
        """Gets the timescale of this DynamicTableWidget.  # noqa: E501

        The default timescale of the widget  # noqa: E501

        :return: The timescale of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._timescale

    @timescale.setter
    def timescale(self, timescale):
        """Sets the timescale of this DynamicTableWidget.

        The default timescale of the widget  # noqa: E501

        :param timescale: The timescale of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._timescale = timescale

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DynamicTableWidget.  # noqa: E501

        The id of the selected datasource  # noqa: E501

        :return: The data_source_id of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DynamicTableWidget.

        The id of the selected datasource  # noqa: E501

        :param data_source_id: The data_source_id of this DynamicTableWidget.  # noqa: E501
        :type: int
        """
        if data_source_id is None:
            raise ValueError("Invalid value for `data_source_id`, must not be `None`")  # noqa: E501

        self._data_source_id = data_source_id

    @property
    def top_x(self):
        """Gets the top_x of this DynamicTableWidget.  # noqa: E501


        :return: The top_x of this DynamicTableWidget.  # noqa: E501
        :rtype: int
        """
        return self._top_x

    @top_x.setter
    def top_x(self, top_x):
        """Sets the top_x of this DynamicTableWidget.


        :param top_x: The top_x of this DynamicTableWidget.  # noqa: E501
        :type: int
        """

        self._top_x = top_x

    @property
    def data_source_full_name(self):
        """Gets the data_source_full_name of this DynamicTableWidget.  # noqa: E501

        The full name of the selected datasource  # noqa: E501

        :return: The data_source_full_name of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._data_source_full_name

    @data_source_full_name.setter
    def data_source_full_name(self, data_source_full_name):
        """Sets the data_source_full_name of this DynamicTableWidget.

        The full name of the selected datasource  # noqa: E501

        :param data_source_full_name: The data_source_full_name of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._data_source_full_name = data_source_full_name

    @property
    def columns(self):
        """Gets the columns of this DynamicTableWidget.  # noqa: E501


        :return: The columns of this DynamicTableWidget.  # noqa: E501
        :rtype: list[DynamicTableWidgetColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this DynamicTableWidget.


        :param columns: The columns of this DynamicTableWidget.  # noqa: E501
        :type: list[DynamicTableWidgetColumn]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def sort_order(self):
        """Gets the sort_order of this DynamicTableWidget.  # noqa: E501


        :return: The sort_order of this DynamicTableWidget.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this DynamicTableWidget.


        :param sort_order: The sort_order of this DynamicTableWidget.  # noqa: E501
        :type: str
        """

        self._sort_order = sort_order

    @property
    def forecast(self):
        """Gets the forecast of this DynamicTableWidget.  # noqa: E501


        :return: The forecast of this DynamicTableWidget.  # noqa: E501
        :rtype: TableWidgetForecastConfiguration
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast):
        """Sets the forecast of this DynamicTableWidget.


        :param forecast: The forecast of this DynamicTableWidget.  # noqa: E501
        :type: TableWidgetForecastConfiguration
        """

        self._forecast = forecast

    @property
    def rows(self):
        """Gets the rows of this DynamicTableWidget.  # noqa: E501


        :return: The rows of this DynamicTableWidget.  # noqa: E501
        :rtype: list[DynamicTableWidgetRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this DynamicTableWidget.


        :param rows: The rows of this DynamicTableWidget.  # noqa: E501
        :type: list[DynamicTableWidgetRow]
        """
        if rows is None:
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

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
        if issubclass(DynamicTableWidget, dict):
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
        if not isinstance(other, DynamicTableWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
