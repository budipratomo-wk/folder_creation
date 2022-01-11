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


class ImportDto(object):
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
        'column_mappings': 'dict(str, str)',
        'delimiter': 'str',
        'file_id': 'str',
        'metadata': 'dict(str, dict(str, object))',
        'tags': 'dict(str, str)'
    }

    attribute_map = {
        'column_mappings': 'columnMappings',
        'delimiter': 'delimiter',
        'file_id': 'fileId',
        'metadata': 'metadata',
        'tags': 'tags'
    }

    def __init__(self, column_mappings=None, delimiter=None, file_id=None, metadata=None, tags=None, _configuration=None):  # noqa: E501
        """ImportDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._column_mappings = None
        self._delimiter = None
        self._file_id = None
        self._metadata = None
        self._tags = None
        self.discriminator = None

        if column_mappings is not None:
            self.column_mappings = column_mappings
        if delimiter is not None:
            self.delimiter = delimiter
        self.file_id = file_id
        if metadata is not None:
            self.metadata = metadata
        if tags is not None:
            self.tags = tags

    @property
    def column_mappings(self):
        """Gets the column_mappings of this ImportDto.  # noqa: E501

        a map of import column names to table column ids  # noqa: E501

        :return: The column_mappings of this ImportDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._column_mappings

    @column_mappings.setter
    def column_mappings(self, column_mappings):
        """Sets the column_mappings of this ImportDto.

        a map of import column names to table column ids  # noqa: E501

        :param column_mappings: The column_mappings of this ImportDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._column_mappings = column_mappings

    @property
    def delimiter(self):
        """Gets the delimiter of this ImportDto.  # noqa: E501

        For overriding the file metadata's delimiter. The file delimiter is the character to use within the file to separate one field from another. If this value is not set, the import will use the file's set delimiter. If this value is set, the file metadata's delimiter will be updated on the file object.  # noqa: E501

        :return: The delimiter of this ImportDto.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ImportDto.

        For overriding the file metadata's delimiter. The file delimiter is the character to use within the file to separate one field from another. If this value is not set, the import will use the file's set delimiter. If this value is set, the file metadata's delimiter will be updated on the file object.  # noqa: E501

        :param delimiter: The delimiter of this ImportDto.  # noqa: E501
        :type: str
        """

        self._delimiter = delimiter

    @property
    def file_id(self):
        """Gets the file_id of this ImportDto.  # noqa: E501

        id of the file to import to the table  # noqa: E501

        :return: The file_id of this ImportDto.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ImportDto.

        id of the file to import to the table  # noqa: E501

        :param file_id: The file_id of this ImportDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and file_id is None:
            raise ValueError("Invalid value for `file_id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                file_id is not None and len(file_id) > 32):
            raise ValueError("Invalid value for `file_id`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                file_id is not None and len(file_id) < 0):
            raise ValueError("Invalid value for `file_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._file_id = file_id

    @property
    def metadata(self):
        """Gets the metadata of this ImportDto.  # noqa: E501

        For overriding column metadata specifically for this import. The keys in this object are column identifiers with the values being metadata objects.  # noqa: E501

        :return: The metadata of this ImportDto.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ImportDto.

        For overriding column metadata specifically for this import. The keys in this object are column identifiers with the values being metadata objects.  # noqa: E501

        :param metadata: The metadata of this ImportDto.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._metadata = metadata

    @property
    def tags(self):
        """Gets the tags of this ImportDto.  # noqa: E501

        an object containing keys and values, which becomes the tag map  # noqa: E501

        :return: The tags of this ImportDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ImportDto.

        an object containing keys and values, which becomes the tag map  # noqa: E501

        :param tags: The tags of this ImportDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

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
        if issubclass(ImportDto, dict):
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
        if not isinstance(other, ImportDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImportDto):
            return True

        return self.to_dict() != other.to_dict()