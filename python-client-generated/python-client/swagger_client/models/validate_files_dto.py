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


class ValidateFilesDto(object):
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
        'deleted_files': 'list[FileMetaDto]',
        'repaired_files': 'list[FileMetaDto]'
    }

    attribute_map = {
        'deleted_files': 'deletedFiles',
        'repaired_files': 'repairedFiles'
    }

    def __init__(self, deleted_files=None, repaired_files=None, _configuration=None):  # noqa: E501
        """ValidateFilesDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deleted_files = None
        self._repaired_files = None
        self.discriminator = None

        if deleted_files is not None:
            self.deleted_files = deleted_files
        if repaired_files is not None:
            self.repaired_files = repaired_files

    @property
    def deleted_files(self):
        """Gets the deleted_files of this ValidateFilesDto.  # noqa: E501

        A list of files that were deleted during the validation because not enough information was available to repair them. These files will no longer be available via the endpoint and will not be included in queries.  # noqa: E501

        :return: The deleted_files of this ValidateFilesDto.  # noqa: E501
        :rtype: list[FileMetaDto]
        """
        return self._deleted_files

    @deleted_files.setter
    def deleted_files(self, deleted_files):
        """Sets the deleted_files of this ValidateFilesDto.

        A list of files that were deleted during the validation because not enough information was available to repair them. These files will no longer be available via the endpoint and will not be included in queries.  # noqa: E501

        :param deleted_files: The deleted_files of this ValidateFilesDto.  # noqa: E501
        :type: list[FileMetaDto]
        """

        self._deleted_files = deleted_files

    @property
    def repaired_files(self):
        """Gets the repaired_files of this ValidateFilesDto.  # noqa: E501

        A list of files that were modified during the validation and will continue to be visible and to be usable in the account.  # noqa: E501

        :return: The repaired_files of this ValidateFilesDto.  # noqa: E501
        :rtype: list[FileMetaDto]
        """
        return self._repaired_files

    @repaired_files.setter
    def repaired_files(self, repaired_files):
        """Sets the repaired_files of this ValidateFilesDto.

        A list of files that were modified during the validation and will continue to be visible and to be usable in the account.  # noqa: E501

        :param repaired_files: The repaired_files of this ValidateFilesDto.  # noqa: E501
        :type: list[FileMetaDto]
        """

        self._repaired_files = repaired_files

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
        if issubclass(ValidateFilesDto, dict):
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
        if not isinstance(other, ValidateFilesDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidateFilesDto):
            return True

        return self.to_dict() != other.to_dict()
