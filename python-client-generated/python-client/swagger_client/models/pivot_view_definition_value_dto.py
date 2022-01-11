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


class PivotViewDefinitionValueDto(object):
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
        'active': 'bool',
        'aggregation': 'str',
        'column_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'active': 'active',
        'aggregation': 'aggregation',
        'column_type': 'columnType',
        'name': 'name'
    }

    def __init__(self, active=None, aggregation=None, column_type=None, name=None, _configuration=None):  # noqa: E501
        """PivotViewDefinitionValueDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._aggregation = None
        self._column_type = None
        self._name = None
        self.discriminator = None

        self.active = active
        self.aggregation = aggregation
        if column_type is not None:
            self.column_type = column_type
        self.name = name

    @property
    def active(self):
        """Gets the active of this PivotViewDefinitionValueDto.  # noqa: E501


        :return: The active of this PivotViewDefinitionValueDto.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PivotViewDefinitionValueDto.


        :param active: The active of this PivotViewDefinitionValueDto.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def aggregation(self):
        """Gets the aggregation of this PivotViewDefinitionValueDto.  # noqa: E501

        The aggregation type to apply to the pivot view value  # noqa: E501

        :return: The aggregation of this PivotViewDefinitionValueDto.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this PivotViewDefinitionValueDto.

        The aggregation type to apply to the pivot view value  # noqa: E501

        :param aggregation: The aggregation of this PivotViewDefinitionValueDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and aggregation is None:
            raise ValueError("Invalid value for `aggregation`, must not be `None`")  # noqa: E501
        allowed_values = ["sum", "count", "distinctcount", "average", "median", "product", "min", "max", "percent", "percentofcolumn", "percentofrow", "difference", "percentdifference", "runningtotals", "stdevp", "stdevs"]  # noqa: E501
        if (self._configuration.client_side_validation and
                aggregation not in allowed_values):
            raise ValueError(
                "Invalid value for `aggregation` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation, allowed_values)
            )

        self._aggregation = aggregation

    @property
    def column_type(self):
        """Gets the column_type of this PivotViewDefinitionValueDto.  # noqa: E501

        The column type.  # noqa: E501

        :return: The column_type of this PivotViewDefinitionValueDto.  # noqa: E501
        :rtype: str
        """
        return self._column_type

    @column_type.setter
    def column_type(self, column_type):
        """Sets the column_type of this PivotViewDefinitionValueDto.

        The column type.  # noqa: E501

        :param column_type: The column_type of this PivotViewDefinitionValueDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["integer", "number", "boolean", "timestamp", "date", "string", "float"]  # noqa: E501
        if (self._configuration.client_side_validation and
                column_type not in allowed_values):
            raise ValueError(
                "Invalid value for `column_type` ({0}), must be one of {1}"  # noqa: E501
                .format(column_type, allowed_values)
            )

        self._column_type = column_type

    @property
    def name(self):
        """Gets the name of this PivotViewDefinitionValueDto.  # noqa: E501

        Name of the pivot view value. The maximum size is 255 characters.  # noqa: E501

        :return: The name of this PivotViewDefinitionValueDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PivotViewDefinitionValueDto.

        Name of the pivot view value. The maximum size is 255 characters.  # noqa: E501

        :param name: The name of this PivotViewDefinitionValueDto.  # noqa: E501
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
        if issubclass(PivotViewDefinitionValueDto, dict):
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
        if not isinstance(other, PivotViewDefinitionValueDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PivotViewDefinitionValueDto):
            return True

        return self.to_dict() != other.to_dict()