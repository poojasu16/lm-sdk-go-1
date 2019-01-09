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

from logicmonitor_sdk.models.widget import Widget  # noqa: F401,E501


class NormalGraphWidget(Widget):
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
        'graph_name': 'str',
        'host_name': 'str',
        'h_id': 'int',
        'dsi_id': 'int',
        'ds_name': 'str',
        'graph_id': 'int',
        'dsi_name': 'str'
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
        'graph_name': 'graphName',
        'host_name': 'hostName',
        'h_id': 'hId',
        'dsi_id': 'dsiId',
        'ds_name': 'dsName',
        'graph_id': 'graphId',
        'dsi_name': 'dsiName'
    }

    def __init__(self, last_updated_by=None, user_permission=None, dashboard_id=None, name=None, description=None, last_updated_on=None, theme=None, interval=None, id=None, type=None, timescale=None, graph_name=None, host_name=None, h_id=None, dsi_id=None, ds_name=None, graph_id=None, dsi_name=None):  # noqa: E501
        """NormalGraphWidget - a model defined in Swagger"""  # noqa: E501

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
        self._graph_name = None
        self._host_name = None
        self._h_id = None
        self._dsi_id = None
        self._ds_name = None
        self._graph_id = None
        self._dsi_name = None
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
        if graph_name is not None:
            self.graph_name = graph_name
        if host_name is not None:
            self.host_name = host_name
        if h_id is not None:
            self.h_id = h_id
        self.dsi_id = dsi_id
        if ds_name is not None:
            self.ds_name = ds_name
        self.graph_id = graph_id
        if dsi_name is not None:
            self.dsi_name = dsi_name

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this NormalGraphWidget.  # noqa: E501

        The user that last updated the widget  # noqa: E501

        :return: The last_updated_by of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this NormalGraphWidget.

        The user that last updated the widget  # noqa: E501

        :param last_updated_by: The last_updated_by of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def user_permission(self):
        """Gets the user_permission of this NormalGraphWidget.  # noqa: E501

        The permission level of the user who last modified the widget  # noqa: E501

        :return: The user_permission of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this NormalGraphWidget.

        The permission level of the user who last modified the widget  # noqa: E501

        :param user_permission: The user_permission of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this NormalGraphWidget.  # noqa: E501

        The id of the dashboard the widget belongs to  # noqa: E501

        :return: The dashboard_id of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this NormalGraphWidget.

        The id of the dashboard the widget belongs to  # noqa: E501

        :param dashboard_id: The dashboard_id of this NormalGraphWidget.  # noqa: E501
        :type: int
        """
        if dashboard_id is None:
            raise ValueError("Invalid value for `dashboard_id`, must not be `None`")  # noqa: E501

        self._dashboard_id = dashboard_id

    @property
    def name(self):
        """Gets the name of this NormalGraphWidget.  # noqa: E501

        The name of the widget  # noqa: E501

        :return: The name of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NormalGraphWidget.

        The name of the widget  # noqa: E501

        :param name: The name of this NormalGraphWidget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this NormalGraphWidget.  # noqa: E501

        The description of the widget  # noqa: E501

        :return: The description of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NormalGraphWidget.

        The description of the widget  # noqa: E501

        :param description: The description of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_updated_on(self):
        """Gets the last_updated_on of this NormalGraphWidget.  # noqa: E501

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :return: The last_updated_on of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_on

    @last_updated_on.setter
    def last_updated_on(self, last_updated_on):
        """Sets the last_updated_on of this NormalGraphWidget.

        The time that corresponds to when the widget was last updated, in epoch format  # noqa: E501

        :param last_updated_on: The last_updated_on of this NormalGraphWidget.  # noqa: E501
        :type: int
        """

        self._last_updated_on = last_updated_on

    @property
    def theme(self):
        """Gets the theme of this NormalGraphWidget.  # noqa: E501

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :return: The theme of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this NormalGraphWidget.

        The color scheme of the widget. Options are: borderPurple | borderGray | borderBlue | solidPurple | solidGray | solidBlue | simplePurple | simpleBlue | simpleGray | newBorderGray | newBorderBlue | newBorderDarkBlue | newSolidGray | newSolidBlue | newSolidDarkBlue | newSimpleGray | newSimpleBlue |newSimpleDarkBlue  # noqa: E501

        :param theme: The theme of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._theme = theme

    @property
    def interval(self):
        """Gets the interval of this NormalGraphWidget.  # noqa: E501

        The refresh interval of the widget, in minutes  # noqa: E501

        :return: The interval of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this NormalGraphWidget.

        The refresh interval of the widget, in minutes  # noqa: E501

        :param interval: The interval of this NormalGraphWidget.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def id(self):
        """Gets the id of this NormalGraphWidget.  # noqa: E501

        The Id of the widget  # noqa: E501

        :return: The id of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NormalGraphWidget.

        The Id of the widget  # noqa: E501

        :param id: The id of this NormalGraphWidget.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this NormalGraphWidget.  # noqa: E501

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :return: The type of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NormalGraphWidget.

        alert | batchjob | flash | gmap | ngraph | ograph | cgraph | sgraph | netflowgraph | groupNetflowGraph | netflow | groupNetflow | html | bigNumber | gauge | pieChart | table | dynamicTable | deviceSLA | text | statsd | deviceStatus | serviceAlert | noc | websiteOverview | websiteOverallStatus | websiteIndividualStatus | websiteSLA  # noqa: E501

        :param type: The type of this NormalGraphWidget.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def timescale(self):
        """Gets the timescale of this NormalGraphWidget.  # noqa: E501

        The default timescale of the widget  # noqa: E501

        :return: The timescale of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._timescale

    @timescale.setter
    def timescale(self, timescale):
        """Sets the timescale of this NormalGraphWidget.

        The default timescale of the widget  # noqa: E501

        :param timescale: The timescale of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._timescale = timescale

    @property
    def graph_name(self):
        """Gets the graph_name of this NormalGraphWidget.  # noqa: E501

        The id of the datasource graph this widget was pinned from  # noqa: E501

        :return: The graph_name of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._graph_name

    @graph_name.setter
    def graph_name(self, graph_name):
        """Sets the graph_name of this NormalGraphWidget.

        The id of the datasource graph this widget was pinned from  # noqa: E501

        :param graph_name: The graph_name of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._graph_name = graph_name

    @property
    def host_name(self):
        """Gets the host_name of this NormalGraphWidget.  # noqa: E501

        The display name of the device the graph was pinned from  # noqa: E501

        :return: The host_name of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this NormalGraphWidget.

        The display name of the device the graph was pinned from  # noqa: E501

        :param host_name: The host_name of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def h_id(self):
        """Gets the h_id of this NormalGraphWidget.  # noqa: E501

        The id of the device the graph was pinned from  # noqa: E501

        :return: The h_id of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._h_id

    @h_id.setter
    def h_id(self, h_id):
        """Sets the h_id of this NormalGraphWidget.

        The id of the device the graph was pinned from  # noqa: E501

        :param h_id: The h_id of this NormalGraphWidget.  # noqa: E501
        :type: int
        """

        self._h_id = h_id

    @property
    def dsi_id(self):
        """Gets the dsi_id of this NormalGraphWidget.  # noqa: E501

        The id of the datasource instance the graph was pinned from  # noqa: E501

        :return: The dsi_id of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._dsi_id

    @dsi_id.setter
    def dsi_id(self, dsi_id):
        """Sets the dsi_id of this NormalGraphWidget.

        The id of the datasource instance the graph was pinned from  # noqa: E501

        :param dsi_id: The dsi_id of this NormalGraphWidget.  # noqa: E501
        :type: int
        """
        if dsi_id is None:
            raise ValueError("Invalid value for `dsi_id`, must not be `None`")  # noqa: E501

        self._dsi_id = dsi_id

    @property
    def ds_name(self):
        """Gets the ds_name of this NormalGraphWidget.  # noqa: E501

        The name (not display name) of the datasource the graph is associated with  # noqa: E501

        :return: The ds_name of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._ds_name

    @ds_name.setter
    def ds_name(self, ds_name):
        """Sets the ds_name of this NormalGraphWidget.

        The name (not display name) of the datasource the graph is associated with  # noqa: E501

        :param ds_name: The ds_name of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._ds_name = ds_name

    @property
    def graph_id(self):
        """Gets the graph_id of this NormalGraphWidget.  # noqa: E501

        The id of the datasource graph this widget was pinned from  # noqa: E501

        :return: The graph_id of this NormalGraphWidget.  # noqa: E501
        :rtype: int
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this NormalGraphWidget.

        The id of the datasource graph this widget was pinned from  # noqa: E501

        :param graph_id: The graph_id of this NormalGraphWidget.  # noqa: E501
        :type: int
        """
        if graph_id is None:
            raise ValueError("Invalid value for `graph_id`, must not be `None`")  # noqa: E501

        self._graph_id = graph_id

    @property
    def dsi_name(self):
        """Gets the dsi_name of this NormalGraphWidget.  # noqa: E501

        The name of the instance the graph was pinned from  # noqa: E501

        :return: The dsi_name of this NormalGraphWidget.  # noqa: E501
        :rtype: str
        """
        return self._dsi_name

    @dsi_name.setter
    def dsi_name(self, dsi_name):
        """Sets the dsi_name of this NormalGraphWidget.

        The name of the instance the graph was pinned from  # noqa: E501

        :param dsi_name: The dsi_name of this NormalGraphWidget.  # noqa: E501
        :type: str
        """

        self._dsi_name = dsi_name

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
        if issubclass(NormalGraphWidget, dict):
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
        if not isinstance(other, NormalGraphWidget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
