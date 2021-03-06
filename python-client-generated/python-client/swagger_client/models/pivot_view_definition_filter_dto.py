# coding: utf-8

"""
    Cerebral API

    The Wdata Preparation API allow users to import data sets from their source system, tag, organize, manipulate, share, export, and query against the data  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: scoutteam@workiva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class PivotViewDefinitionFilterDto(object):
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
        'between_value': 'str',
        'column_type': 'str',
        'exclude': 'bool',
        'filter': 'str',
        'filter_values': 'list[str]',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'between_value': 'betweenValue',
        'column_type': 'columnType',
        'exclude': 'exclude',
        'filter': 'filter',
        'filter_values': 'filterValues',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, between_value=None, column_type=None, exclude=None, filter=None, filter_values=None, name=None, value=None, _configuration=None):  # noqa: E501
        """PivotViewDefinitionFilterDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._between_value = None
        self._column_type = None
        self._exclude = None
        self._filter = None
        self._filter_values = None
        self._name = None
        self._value = None
        self.discriminator = None

        if between_value is not None:
            self.between_value = between_value
        self.column_type = column_type
        if exclude is not None:
            self.exclude = exclude
        if filter is not None:
            self.filter = filter
        if filter_values is not None:
            self.filter_values = filter_values
        self.name = name
        if value is not None:
            self.value = value

    @property
    def between_value(self):
        """Gets the between_value of this PivotViewDefinitionFilterDto.  # noqa: E501

        A second value for 'between' filters  # noqa: E501

        :return: The between_value of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._between_value

    @between_value.setter
    def between_value(self, between_value):
        """Sets the between_value of this PivotViewDefinitionFilterDto.

        A second value for 'between' filters  # noqa: E501

        :param between_value: The between_value of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                between_value is not None and len(between_value) > 255):
            raise ValueError("Invalid value for `between_value`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                between_value is not None and len(between_value) < 0):
            raise ValueError("Invalid value for `between_value`, length must be greater than or equal to `0`")  # noqa: E501

        self._between_value = between_value

    @property
    def column_type(self):
        """Gets the column_type of this PivotViewDefinitionFilterDto.  # noqa: E501

        The column type.  # noqa: E501

        :return: The column_type of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this PivotViewDefinitionFilterDto.

        The column type.  # noqa: E501

        :param column_type: The column_type of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and column_type is None:
            raise ValueError("Invalid value for `column_type`, must not be `None`")  # noqa: E501
        allowed_values = ["integer", "number", "boolean", "timestamp", "date", "string", "float"]  # noqa: E501
        if (self._configuration.client_side_validation and
                column_type not in allowed_values):
            raise ValueError(
                "Invalid value for `column_type` ({0}), must be one of {1}"  # noqa: E501
                .format(column_type, allowed_values)
            )

        self._column_type = column_type

    @property
    def exclude(self):
        """Gets the exclude of this PivotViewDefinitionFilterDto.  # noqa: E501

        True if value list is exclude, false if value list is include. Defaults to true.  # noqa: E501

        :return: The exclude of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: bool
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this PivotViewDefinitionFilterDto.

        True if value list is exclude, false if value list is include. Defaults to true.  # noqa: E501

        :param exclude: The exclude of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: bool
        """

        self._exclude = exclude

    @property
    def filter(self):
        """Gets the filter of this PivotViewDefinitionFilterDto.  # noqa: E501

        The filter to perform.  # noqa: E501

        :return: The filter of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PivotViewDefinitionFilterDto.

        The filter to perform.  # noqa: E501

        :param filter: The filter of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["EQUAL", "NOT_EQUAL", "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "BETWEEN", "NOT_BETWEEN"]  # noqa: E501
        if (self._configuration.client_side_validation and
                filter not in allowed_values):
            raise ValueError(
                "Invalid value for `filter` ({0}), must be one of {1}"  # noqa: E501
                .format(filter, allowed_values)
            )

        self._filter = filter

    @property
    def filter_values(self):
        """Gets the filter_values of this PivotViewDefinitionFilterDto.  # noqa: E501

        The values obtained after applying the filter  # noqa: E501

        :return: The filter_values of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter_values

    @filter_values.setter
    def filter_values(self, filter_values):
        """Sets the filter_values of this PivotViewDefinitionFilterDto.

        The values obtained after applying the filter  # noqa: E501

        :param filter_values: The filter_values of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: list[str]
        """

        self._filter_values = filter_values

    @property
    def name(self):
        """Gets the name of this PivotViewDefinitionFilterDto.  # noqa: E501

        The column for the pivot view filter. The maximum size is 255 characters.  # noqa: E501

        :return: The name of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PivotViewDefinitionFilterDto.

        The column for the pivot view filter. The maximum size is 255 characters.  # noqa: E501

        :param name: The name of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this PivotViewDefinitionFilterDto.  # noqa: E501

        The value to filter on.  # noqa: E501

        :return: The value of this PivotViewDefinitionFilterDto.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PivotViewDefinitionFilterDto.

        The value to filter on.  # noqa: E501

        :param value: The value of this PivotViewDefinitionFilterDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                value is not None and len(value) > 255):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                value is not None and len(value) < 0):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `0`")  # noqa: E501

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
        if issubclass(PivotViewDefinitionFilterDto, dict):
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
        if not isinstance(other, PivotViewDefinitionFilterDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PivotViewDefinitionFilterDto):
            return True

        return self.to_dict() != other.to_dict()
