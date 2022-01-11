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


class RefreshBatchDto(object):
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
        'batch_refresh_id': 'str',
        'child_refreshes': 'list[ConnectionRunDto]',
        'created': 'datetime',
        'created_by': 'str',
        'destination_status': 'str',
        'error': 'str',
        'source_status': 'str',
        'updated': 'datetime'
    }

    attribute_map = {
        'batch_refresh_id': 'batchRefreshId',
        'child_refreshes': 'childRefreshes',
        'created': 'created',
        'created_by': 'createdBy',
        'destination_status': 'destinationStatus',
        'error': 'error',
        'source_status': 'sourceStatus',
        'updated': 'updated'
    }

    def __init__(self, batch_refresh_id=None, child_refreshes=None, created=None, created_by=None, destination_status=None, error=None, source_status=None, updated=None, _configuration=None):  # noqa: E501
        """RefreshBatchDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_refresh_id = None
        self._child_refreshes = None
        self._created = None
        self._created_by = None
        self._destination_status = None
        self._error = None
        self._source_status = None
        self._updated = None
        self.discriminator = None

        if batch_refresh_id is not None:
            self.batch_refresh_id = batch_refresh_id
        if child_refreshes is not None:
            self.child_refreshes = child_refreshes
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if destination_status is not None:
            self.destination_status = destination_status
        if error is not None:
            self.error = error
        if source_status is not None:
            self.source_status = source_status
        if updated is not None:
            self.updated = updated

    @property
    def batch_refresh_id(self):
        """Gets the batch_refresh_id of this RefreshBatchDto.  # noqa: E501

        The unique ID of the batch  # noqa: E501

        :return: The batch_refresh_id of this RefreshBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._batch_refresh_id

    @batch_refresh_id.setter
    def batch_refresh_id(self, batch_refresh_id):
        """Sets the batch_refresh_id of this RefreshBatchDto.

        The unique ID of the batch  # noqa: E501

        :param batch_refresh_id: The batch_refresh_id of this RefreshBatchDto.  # noqa: E501
        :type: str
        """

        self._batch_refresh_id = batch_refresh_id

    @property
    def child_refreshes(self):
        """Gets the child_refreshes of this RefreshBatchDto.  # noqa: E501

        The list of jobs initiated by the batch  # noqa: E501

        :return: The child_refreshes of this RefreshBatchDto.  # noqa: E501
        :rtype: list[ConnectionRunDto]
        """
        return self._child_refreshes

    @child_refreshes.setter
    def child_refreshes(self, child_refreshes):
        """Sets the child_refreshes of this RefreshBatchDto.

        The list of jobs initiated by the batch  # noqa: E501

        :param child_refreshes: The child_refreshes of this RefreshBatchDto.  # noqa: E501
        :type: list[ConnectionRunDto]
        """

        self._child_refreshes = child_refreshes

    @property
    def created(self):
        """Gets the created of this RefreshBatchDto.  # noqa: E501

        When the batch was created, as a datetime  # noqa: E501

        :return: The created of this RefreshBatchDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this RefreshBatchDto.

        When the batch was created, as a datetime  # noqa: E501

        :param created: The created of this RefreshBatchDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this RefreshBatchDto.  # noqa: E501

        The ID of the user that created the batch  # noqa: E501

        :return: The created_by of this RefreshBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RefreshBatchDto.

        The ID of the user that created the batch  # noqa: E501

        :param created_by: The created_by of this RefreshBatchDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def destination_status(self):
        """Gets the destination_status of this RefreshBatchDto.  # noqa: E501

        The run status of the destination  # noqa: E501

        :return: The destination_status of this RefreshBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._destination_status

    @destination_status.setter
    def destination_status(self, destination_status):
        """Sets the destination_status of this RefreshBatchDto.

        The run status of the destination  # noqa: E501

        :param destination_status: The destination_status of this RefreshBatchDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_started", "running", "complete", "error", "cancelled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                destination_status not in allowed_values):
            raise ValueError(
                "Invalid value for `destination_status` ({0}), must be one of {1}"  # noqa: E501
                .format(destination_status, allowed_values)
            )

        self._destination_status = destination_status

    @property
    def error(self):
        """Gets the error of this RefreshBatchDto.  # noqa: E501

        Any error encountered while initiating the batch  # noqa: E501

        :return: The error of this RefreshBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RefreshBatchDto.

        Any error encountered while initiating the batch  # noqa: E501

        :param error: The error of this RefreshBatchDto.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def source_status(self):
        """Gets the source_status of this RefreshBatchDto.  # noqa: E501

        The run status of the source  # noqa: E501

        :return: The source_status of this RefreshBatchDto.  # noqa: E501
        :rtype: str
        """
        return self._source_status

    @source_status.setter
    def source_status(self, source_status):
        """Sets the source_status of this RefreshBatchDto.

        The run status of the source  # noqa: E501

        :param source_status: The source_status of this RefreshBatchDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_started", "running", "complete", "error", "cancelled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source_status not in allowed_values):
            raise ValueError(
                "Invalid value for `source_status` ({0}), must be one of {1}"  # noqa: E501
                .format(source_status, allowed_values)
            )

        self._source_status = source_status

    @property
    def updated(self):
        """Gets the updated of this RefreshBatchDto.  # noqa: E501

        When the batch was updated, as a datetime  # noqa: E501

        :return: The updated of this RefreshBatchDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RefreshBatchDto.

        When the batch was updated, as a datetime  # noqa: E501

        :param updated: The updated of this RefreshBatchDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if issubclass(RefreshBatchDto, dict):
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
        if not isinstance(other, RefreshBatchDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefreshBatchDto):
            return True

        return self.to_dict() != other.to_dict()