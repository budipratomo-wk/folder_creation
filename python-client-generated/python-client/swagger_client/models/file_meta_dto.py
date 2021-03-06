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


class FileMetaDto(object):
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
        'created': 'datetime',
        'delimiter': 'str',
        'id': 'str',
        'key': 'str',
        'metadata': 'dict(str, dict(str, object))',
        'name': 'str',
        'num_errors': 'int',
        'num_records': 'int',
        'original_file_size': 'int',
        'source': 'str',
        'status': 'str',
        'table_id': 'str',
        'tags': 'dict(str, str)',
        'updated': 'datetime',
        'user_id': 'str',
        'version': 'int'
    }

    attribute_map = {
        'column_mappings': 'columnMappings',
        'created': 'created',
        'delimiter': 'delimiter',
        'id': 'id',
        'key': 'key',
        'metadata': 'metadata',
        'name': 'name',
        'num_errors': 'numErrors',
        'num_records': 'numRecords',
        'original_file_size': 'originalFileSize',
        'source': 'source',
        'status': 'status',
        'table_id': 'tableId',
        'tags': 'tags',
        'updated': 'updated',
        'user_id': 'userId',
        'version': 'version'
    }

    def __init__(self, column_mappings=None, created=None, delimiter=None, id=None, key=None, metadata=None, name=None, num_errors=None, num_records=None, original_file_size=None, source=None, status=None, table_id=None, tags=None, updated=None, user_id=None, version=None, _configuration=None):  # noqa: E501
        """FileMetaDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._column_mappings = None
        self._created = None
        self._delimiter = None
        self._id = None
        self._key = None
        self._metadata = None
        self._name = None
        self._num_errors = None
        self._num_records = None
        self._original_file_size = None
        self._source = None
        self._status = None
        self._table_id = None
        self._tags = None
        self._updated = None
        self._user_id = None
        self._version = None
        self.discriminator = None

        if column_mappings is not None:
            self.column_mappings = column_mappings
        if created is not None:
            self.created = created
        if delimiter is not None:
            self.delimiter = delimiter
        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if num_errors is not None:
            self.num_errors = num_errors
        if num_records is not None:
            self.num_records = num_records
        if original_file_size is not None:
            self.original_file_size = original_file_size
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status
        if table_id is not None:
            self.table_id = table_id
        if tags is not None:
            self.tags = tags
        if updated is not None:
            self.updated = updated
        if user_id is not None:
            self.user_id = user_id
        if version is not None:
            self.version = version

    @property
    def column_mappings(self):
        """Gets the column_mappings of this FileMetaDto.  # noqa: E501

        Maps the columns in the physical file (CSV or JSON) to the columns in fact table = {\"physical_col1\":\"table_col1\", \"physical_col2\":\"table_col2\"}  # noqa: E501

        :return: The column_mappings of this FileMetaDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._column_mappings

    @column_mappings.setter
    def column_mappings(self, column_mappings):
        """Sets the column_mappings of this FileMetaDto.

        Maps the columns in the physical file (CSV or JSON) to the columns in fact table = {\"physical_col1\":\"table_col1\", \"physical_col2\":\"table_col2\"}  # noqa: E501

        :param column_mappings: The column_mappings of this FileMetaDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._column_mappings = column_mappings

    @property
    def created(self):
        """Gets the created of this FileMetaDto.  # noqa: E501

        When the entity was created  # noqa: E501

        :return: The created of this FileMetaDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileMetaDto.

        When the entity was created  # noqa: E501

        :param created: The created of this FileMetaDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def delimiter(self):
        """Gets the delimiter of this FileMetaDto.  # noqa: E501

        The character to use as a delimiter within the file to separate one field from another.  The default is comma  # noqa: E501

        :return: The delimiter of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this FileMetaDto.

        The character to use as a delimiter within the file to separate one field from another.  The default is comma  # noqa: E501

        :param delimiter: The delimiter of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._delimiter = delimiter

    @property
    def id(self):
        """Gets the id of this FileMetaDto.  # noqa: E501

        The entity's unique identifier  # noqa: E501

        :return: The id of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileMetaDto.

        The entity's unique identifier  # noqa: E501

        :param id: The id of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this FileMetaDto.  # noqa: E501

        The key is here for backwards compatibility only and will always be an empty string.  # noqa: E501

        :return: The key of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this FileMetaDto.

        The key is here for backwards compatibility only and will always be an empty string.  # noqa: E501

        :param key: The key of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def metadata(self):
        """Gets the metadata of this FileMetaDto.  # noqa: E501

        The file's meta data  # noqa: E501

        :return: The metadata of this FileMetaDto.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FileMetaDto.

        The file's meta data  # noqa: E501

        :param metadata: The metadata of this FileMetaDto.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this FileMetaDto.  # noqa: E501

        The name of the file  # noqa: E501

        :return: The name of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileMetaDto.

        The name of the file  # noqa: E501

        :param name: The name of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def num_errors(self):
        """Gets the num_errors of this FileMetaDto.  # noqa: E501

        Number of errors found in the file  # noqa: E501

        :return: The num_errors of this FileMetaDto.  # noqa: E501
        :rtype: int
        """
        return self._num_errors

    @num_errors.setter
    def num_errors(self, num_errors):
        """Sets the num_errors of this FileMetaDto.

        Number of errors found in the file  # noqa: E501

        :param num_errors: The num_errors of this FileMetaDto.  # noqa: E501
        :type: int
        """

        self._num_errors = num_errors

    @property
    def num_records(self):
        """Gets the num_records of this FileMetaDto.  # noqa: E501

        Number of records imported from this file.  This will only be non-zero if the file is in the IMPORTED status.  # noqa: E501

        :return: The num_records of this FileMetaDto.  # noqa: E501
        :rtype: int
        """
        return self._num_records

    @num_records.setter
    def num_records(self, num_records):
        """Sets the num_records of this FileMetaDto.

        Number of records imported from this file.  This will only be non-zero if the file is in the IMPORTED status.  # noqa: E501

        :param num_records: The num_records of this FileMetaDto.  # noqa: E501
        :type: int
        """

        self._num_records = num_records

    @property
    def original_file_size(self):
        """Gets the original_file_size of this FileMetaDto.  # noqa: E501

        Size of the original file that was uploaded.  # noqa: E501

        :return: The original_file_size of this FileMetaDto.  # noqa: E501
        :rtype: int
        """
        return self._original_file_size

    @original_file_size.setter
    def original_file_size(self, original_file_size):
        """Sets the original_file_size of this FileMetaDto.

        Size of the original file that was uploaded.  # noqa: E501

        :param original_file_size: The original_file_size of this FileMetaDto.  # noqa: E501
        :type: int
        """

        self._original_file_size = original_file_size

    @property
    def source(self):
        """Gets the source of this FileMetaDto.  # noqa: E501

        URI that describes the source location of this file if imported from another system. For instance, this will have a spreadsheet URL if this file was imported from spreadsheets. This will be null if the file was uploaded using the data prep API.  # noqa: E501

        :return: The source of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this FileMetaDto.

        URI that describes the source location of this file if imported from another system. For instance, this will have a spreadsheet URL if this file was imported from spreadsheets. This will be null if the file was uploaded using the data prep API.  # noqa: E501

        :param source: The source of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def status(self):
        """Gets the status of this FileMetaDto.  # noqa: E501

        The files's current status  # noqa: E501

        :return: The status of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileMetaDto.

        The files's current status  # noqa: E501

        :param status: The status of this FileMetaDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["STAGING", "STAGED", "IMPORTING", "IMPORTED", "ERROR"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def table_id(self):
        """Gets the table_id of this FileMetaDto.  # noqa: E501

        The unique identifier for the table  # noqa: E501

        :return: The table_id of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this FileMetaDto.

        The unique identifier for the table  # noqa: E501

        :param table_id: The table_id of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._table_id = table_id

    @property
    def tags(self):
        """Gets the tags of this FileMetaDto.  # noqa: E501

        The tags associated with the file  # noqa: E501

        :return: The tags of this FileMetaDto.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FileMetaDto.

        The tags associated with the file  # noqa: E501

        :param tags: The tags of this FileMetaDto.  # noqa: E501
        :type: dict(str, str)
        """

        self._tags = tags

    @property
    def updated(self):
        """Gets the updated of this FileMetaDto.  # noqa: E501

        When the entity was last updated  # noqa: E501

        :return: The updated of this FileMetaDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this FileMetaDto.

        When the entity was last updated  # noqa: E501

        :param updated: The updated of this FileMetaDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def user_id(self):
        """Gets the user_id of this FileMetaDto.  # noqa: E501

        The owner of the entity  # noqa: E501

        :return: The user_id of this FileMetaDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this FileMetaDto.

        The owner of the entity  # noqa: E501

        :param user_id: The user_id of this FileMetaDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def version(self):
        """Gets the version of this FileMetaDto.  # noqa: E501

        The version of the current representation of the entity  # noqa: E501

        :return: The version of this FileMetaDto.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileMetaDto.

        The version of the current representation of the entity  # noqa: E501

        :param version: The version of this FileMetaDto.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(FileMetaDto, dict):
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
        if not isinstance(other, FileMetaDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMetaDto):
            return True

        return self.to_dict() != other.to_dict()
