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


class ValidateTablesDto(object):
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
        'deleted_tables': 'list[TableDto]',
        'repaired_tables': 'list[TableDto]'
    }

    attribute_map = {
        'deleted_tables': 'deletedTables',
        'repaired_tables': 'repairedTables'
    }

    def __init__(self, deleted_tables=None, repaired_tables=None, _configuration=None):  # noqa: E501
        """ValidateTablesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deleted_tables = None
        self._repaired_tables = None
        self.discriminator = None

        if deleted_tables is not None:
            self.deleted_tables = deleted_tables
        if repaired_tables is not None:
            self.repaired_tables = repaired_tables

    @property
    def deleted_tables(self):
        """Gets the deleted_tables of this ValidateTablesDto.  # noqa: E501

        A list of tables that were deleted during the validation because not enough information was available to repair them. These tables will no longer be available via the endpoint and queries using these tables will cease to function properly.  # noqa: E501

        :return: The deleted_tables of this ValidateTablesDto.  # noqa: E501
        :rtype: list[TableDto]
        """
        return self._deleted_tables

    @deleted_tables.setter
    def deleted_tables(self, deleted_tables):
        """Sets the deleted_tables of this ValidateTablesDto.

        A list of tables that were deleted during the validation because not enough information was available to repair them. These tables will no longer be available via the endpoint and queries using these tables will cease to function properly.  # noqa: E501

        :param deleted_tables: The deleted_tables of this ValidateTablesDto.  # noqa: E501
        :type: list[TableDto]
        """

        self._deleted_tables = deleted_tables

    @property
    def repaired_tables(self):
        """Gets the repaired_tables of this ValidateTablesDto.  # noqa: E501

        A list of tables that were modified during the validation and will continue to be visible and to be usable in the account.  # noqa: E501

        :return: The repaired_tables of this ValidateTablesDto.  # noqa: E501
        :rtype: list[TableDto]
        """
        return self._repaired_tables

    @repaired_tables.setter
    def repaired_tables(self, repaired_tables):
        """Sets the repaired_tables of this ValidateTablesDto.

        A list of tables that were modified during the validation and will continue to be visible and to be usable in the account.  # noqa: E501

        :param repaired_tables: The repaired_tables of this ValidateTablesDto.  # noqa: E501
        :type: list[TableDto]
        """

        self._repaired_tables = repaired_tables

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
        if issubclass(ValidateTablesDto, dict):
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
        if not isinstance(other, ValidateTablesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidateTablesDto):
            return True

        return self.to_dict() != other.to_dict()
