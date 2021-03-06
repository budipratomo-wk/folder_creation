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


class ConnectionDto(object):
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
        'connection_id': 'str',
        'created': 'datetime',
        'created_by': 'str',
        'description': 'str',
        'destination_id': 'str',
        'destination_type': 'str',
        'last_run_by': 'str',
        'last_run_date': 'datetime',
        'last_run_destination_parameters': 'dict(str, object)',
        'last_run_job_id': 'str',
        'last_run_source_parameters': 'dict(str, object)',
        'metadata': 'dict(str, object)',
        'name': 'str',
        'source_id': 'str',
        'source_type': 'str'
    }

    attribute_map = {
        'connection_id': 'connectionId',
        'created': 'created',
        'created_by': 'createdBy',
        'description': 'description',
        'destination_id': 'destinationId',
        'destination_type': 'destinationType',
        'last_run_by': 'lastRunBy',
        'last_run_date': 'lastRunDate',
        'last_run_destination_parameters': 'lastRunDestinationParameters',
        'last_run_job_id': 'lastRunJobId',
        'last_run_source_parameters': 'lastRunSourceParameters',
        'metadata': 'metadata',
        'name': 'name',
        'source_id': 'sourceId',
        'source_type': 'sourceType'
    }

    def __init__(self, connection_id=None, created=None, created_by=None, description=None, destination_id=None, destination_type=None, last_run_by=None, last_run_date=None, last_run_destination_parameters=None, last_run_job_id=None, last_run_source_parameters=None, metadata=None, name=None, source_id=None, source_type=None, _configuration=None):  # noqa: E501
        """ConnectionDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._connection_id = None
        self._created = None
        self._created_by = None
        self._description = None
        self._destination_id = None
        self._destination_type = None
        self._last_run_by = None
        self._last_run_date = None
        self._last_run_destination_parameters = None
        self._last_run_job_id = None
        self._last_run_source_parameters = None
        self._metadata = None
        self._name = None
        self._source_id = None
        self._source_type = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if destination_id is not None:
            self.destination_id = destination_id
        if destination_type is not None:
            self.destination_type = destination_type
        if last_run_by is not None:
            self.last_run_by = last_run_by
        if last_run_date is not None:
            self.last_run_date = last_run_date
        if last_run_destination_parameters is not None:
            self.last_run_destination_parameters = last_run_destination_parameters
        if last_run_job_id is not None:
            self.last_run_job_id = last_run_job_id
        if last_run_source_parameters is not None:
            self.last_run_source_parameters = last_run_source_parameters
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if source_id is not None:
            self.source_id = source_id
        if source_type is not None:
            self.source_type = source_type

    @property
    def connection_id(self):
        """Gets the connection_id of this ConnectionDto.  # noqa: E501

        The unique ID of the connection  # noqa: E501

        :return: The connection_id of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this ConnectionDto.

        The unique ID of the connection  # noqa: E501

        :param connection_id: The connection_id of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._connection_id = connection_id

    @property
    def created(self):
        """Gets the created of this ConnectionDto.  # noqa: E501

        When the connection was created, as a datetime  # noqa: E501

        :return: The created of this ConnectionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConnectionDto.

        When the connection was created, as a datetime  # noqa: E501

        :param created: The created of this ConnectionDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this ConnectionDto.  # noqa: E501

        The ID of the user that created the connection  # noqa: E501

        :return: The created_by of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ConnectionDto.

        The ID of the user that created the connection  # noqa: E501

        :param created_by: The created_by of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def description(self):
        """Gets the description of this ConnectionDto.  # noqa: E501

        The description of the connection, if specified  # noqa: E501

        :return: The description of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectionDto.

        The description of the connection, if specified  # noqa: E501

        :param description: The description of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def destination_id(self):
        """Gets the destination_id of this ConnectionDto.  # noqa: E501

        The ID of the file or item the connection sends data to  # noqa: E501

        :return: The destination_id of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """Sets the destination_id of this ConnectionDto.

        The ID of the file or item the connection sends data to  # noqa: E501

        :param destination_id: The destination_id of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._destination_id = destination_id

    @property
    def destination_type(self):
        """Gets the destination_type of this ConnectionDto.  # noqa: E501

        The type of file or item the connection sends data to  # noqa: E501

        :return: The destination_type of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this ConnectionDto.

        The type of file or item the connection sends data to  # noqa: E501

        :param destination_type: The destination_type of this ConnectionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["spreadsheet", "spreadsheet_section", "presentation", "presentation_chart", "presentation_embedded_table", "document", "document_chart", "document_embedded_table", "wdata_query", "wdata_table", "wdata_table_dataset", "report", "unknown_record_type"]  # noqa: E501
        if (self._configuration.client_side_validation and
                destination_type not in allowed_values):
            raise ValueError(
                "Invalid value for `destination_type` ({0}), must be one of {1}"  # noqa: E501
                .format(destination_type, allowed_values)
            )

        self._destination_type = destination_type

    @property
    def last_run_by(self):
        """Gets the last_run_by of this ConnectionDto.  # noqa: E501

        The ID of the user that last ran the connection  # noqa: E501

        :return: The last_run_by of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._last_run_by

    @last_run_by.setter
    def last_run_by(self, last_run_by):
        """Sets the last_run_by of this ConnectionDto.

        The ID of the user that last ran the connection  # noqa: E501

        :param last_run_by: The last_run_by of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._last_run_by = last_run_by

    @property
    def last_run_date(self):
        """Gets the last_run_date of this ConnectionDto.  # noqa: E501

        When the connection last ran, as a datetime  # noqa: E501

        :return: The last_run_date of this ConnectionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run_date

    @last_run_date.setter
    def last_run_date(self, last_run_date):
        """Sets the last_run_date of this ConnectionDto.

        When the connection last ran, as a datetime  # noqa: E501

        :param last_run_date: The last_run_date of this ConnectionDto.  # noqa: E501
        :type: datetime
        """

        self._last_run_date = last_run_date

    @property
    def last_run_destination_parameters(self):
        """Gets the last_run_destination_parameters of this ConnectionDto.  # noqa: E501

        A map of the parameters used with the destination when the connection last ran  # noqa: E501

        :return: The last_run_destination_parameters of this ConnectionDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._last_run_destination_parameters

    @last_run_destination_parameters.setter
    def last_run_destination_parameters(self, last_run_destination_parameters):
        """Sets the last_run_destination_parameters of this ConnectionDto.

        A map of the parameters used with the destination when the connection last ran  # noqa: E501

        :param last_run_destination_parameters: The last_run_destination_parameters of this ConnectionDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._last_run_destination_parameters = last_run_destination_parameters

    @property
    def last_run_job_id(self):
        """Gets the last_run_job_id of this ConnectionDto.  # noqa: E501

        The ID of the connection's last run  # noqa: E501

        :return: The last_run_job_id of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._last_run_job_id

    @last_run_job_id.setter
    def last_run_job_id(self, last_run_job_id):
        """Sets the last_run_job_id of this ConnectionDto.

        The ID of the connection's last run  # noqa: E501

        :param last_run_job_id: The last_run_job_id of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._last_run_job_id = last_run_job_id

    @property
    def last_run_source_parameters(self):
        """Gets the last_run_source_parameters of this ConnectionDto.  # noqa: E501

        A map of the parameters used with the source when the connection last ran  # noqa: E501

        :return: The last_run_source_parameters of this ConnectionDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._last_run_source_parameters

    @last_run_source_parameters.setter
    def last_run_source_parameters(self, last_run_source_parameters):
        """Sets the last_run_source_parameters of this ConnectionDto.

        A map of the parameters used with the source when the connection last ran  # noqa: E501

        :param last_run_source_parameters: The last_run_source_parameters of this ConnectionDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._last_run_source_parameters = last_run_source_parameters

    @property
    def metadata(self):
        """Gets the metadata of this ConnectionDto.  # noqa: E501

        Any additional information about the connection  # noqa: E501

        :return: The metadata of this ConnectionDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ConnectionDto.

        Any additional information about the connection  # noqa: E501

        :param metadata: The metadata of this ConnectionDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this ConnectionDto.  # noqa: E501

        The name of the connection, if specified  # noqa: E501

        :return: The name of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectionDto.

        The name of the connection, if specified  # noqa: E501

        :param name: The name of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_id(self):
        """Gets the source_id of this ConnectionDto.  # noqa: E501

        The ID of the file or item the connection pulls data from  # noqa: E501

        :return: The source_id of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ConnectionDto.

        The ID of the file or item the connection pulls data from  # noqa: E501

        :param source_id: The source_id of this ConnectionDto.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

    @property
    def source_type(self):
        """Gets the source_type of this ConnectionDto.  # noqa: E501

        The type of file or item the connection pulls data from  # noqa: E501

        :return: The source_type of this ConnectionDto.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ConnectionDto.

        The type of file or item the connection pulls data from  # noqa: E501

        :param source_type: The source_type of this ConnectionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["spreadsheet", "spreadsheet_section", "presentation", "presentation_chart", "presentation_embedded_table", "document", "document_chart", "document_embedded_table", "wdata_query", "wdata_table", "wdata_table_dataset", "report", "unknown_record_type"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source_type not in allowed_values):
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

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
        if issubclass(ConnectionDto, dict):
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
        if not isinstance(other, ConnectionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectionDto):
            return True

        return self.to_dict() != other.to_dict()
