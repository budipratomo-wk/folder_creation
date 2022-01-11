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


class FolderableDto(object):
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
        'created': 'datetime',
        'description': 'str',
        'id': 'str',
        'metadata': 'object',
        'modified': 'datetime',
        'modified_by': 'str',
        'name': 'str',
        'parent_id': 'str',
        'type': 'int',
        'updated': 'datetime',
        'updated_by': 'str'
    }

    attribute_map = {
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'metadata': 'metadata',
        'modified': 'modified',
        'modified_by': 'modifiedBy',
        'name': 'name',
        'parent_id': 'parentId',
        'type': 'type',
        'updated': 'updated',
        'updated_by': 'updatedBy'
    }

    def __init__(self, created=None, description=None, id=None, metadata=None, modified=None, modified_by=None, name=None, parent_id=None, type=None, updated=None, updated_by=None, _configuration=None):  # noqa: E501
        """FolderableDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._description = None
        self._id = None
        self._metadata = None
        self._modified = None
        self._modified_by = None
        self._name = None
        self._parent_id = None
        self._type = None
        self._updated = None
        self._updated_by = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        self.id = id
        if metadata is not None:
            self.metadata = metadata
        if modified is not None:
            self.modified = modified
        if modified_by is not None:
            self.modified_by = modified_by
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        self.type = type
        if updated is not None:
            self.updated = updated
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def created(self):
        """Gets the created of this FolderableDto.  # noqa: E501

        When the entity was created  # noqa: E501

        :return: The created of this FolderableDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FolderableDto.

        When the entity was created  # noqa: E501

        :param created: The created of this FolderableDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this FolderableDto.  # noqa: E501

        A description of the folderable entity  # noqa: E501

        :return: The description of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FolderableDto.

        A description of the folderable entity  # noqa: E501

        :param description: The description of this FolderableDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this FolderableDto.  # noqa: E501

        The UUID unique identifier for the entity.  # noqa: E501

        :return: The id of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderableDto.

        The UUID unique identifier for the entity.  # noqa: E501

        :param id: The id of this FolderableDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                id is not None and not re.search(r'[a-f0-9]{12}4[a-f0-9]{3}[89aAbB][a-f0-9]{15}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/[a-f0-9]{12}4[a-f0-9]{3}[89aAbB][a-f0-9]{15}/`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this FolderableDto.  # noqa: E501

        Contains additional metadata about the entity returned. For example, a table entity might have a type attribute.  # noqa: E501

        :return: The metadata of this FolderableDto.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FolderableDto.

        Contains additional metadata about the entity returned. For example, a table entity might have a type attribute.  # noqa: E501

        :param metadata: The metadata of this FolderableDto.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def modified(self):
        """Gets the modified of this FolderableDto.  # noqa: E501

        When a significant event happened on the data object.  For example, for queries, this is when the last run occurred; for tables, this is when the last upload occurred.  # noqa: E501

        :return: The modified of this FolderableDto.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this FolderableDto.

        When a significant event happened on the data object.  For example, for queries, this is when the last run occurred; for tables, this is when the last upload occurred.  # noqa: E501

        :param modified: The modified of this FolderableDto.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def modified_by(self):
        """Gets the modified_by of this FolderableDto.  # noqa: E501

        The identifier of the user who last modified the entity  # noqa: E501

        :return: The modified_by of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this FolderableDto.

        The identifier of the user who last modified the entity  # noqa: E501

        :param modified_by: The modified_by of this FolderableDto.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def name(self):
        """Gets the name of this FolderableDto.  # noqa: E501

        The name of the folderable entity  # noqa: E501

        :return: The name of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderableDto.

        The name of the folderable entity  # noqa: E501

        :param name: The name of this FolderableDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this FolderableDto.  # noqa: E501

        The ID of the folder to which this entity belongs. This can be null if the entity is not in a folder.  # noqa: E501

        :return: The parent_id of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this FolderableDto.

        The ID of the folder to which this entity belongs. This can be null if the entity is not in a folder.  # noqa: E501

        :param parent_id: The parent_id of this FolderableDto.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def type(self):
        """Gets the type of this FolderableDto.  # noqa: E501

        The numerical identifier for the entity's type:  Query=100, Table=200, Pivot View=500, Folder=600, Shared Table=700  # noqa: E501

        :return: The type of this FolderableDto.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FolderableDto.

        The numerical identifier for the entity's type:  Query=100, Table=200, Pivot View=500, Folder=600, Shared Table=700  # noqa: E501

        :param type: The type of this FolderableDto.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this FolderableDto.  # noqa: E501

        When the data object was last updated  # noqa: E501

        :return: The updated of this FolderableDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this FolderableDto.

        When the data object was last updated  # noqa: E501

        :param updated: The updated of this FolderableDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def updated_by(self):
        """Gets the updated_by of this FolderableDto.  # noqa: E501

        The identifier of the user who last updated the entity  # noqa: E501

        :return: The updated_by of this FolderableDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this FolderableDto.

        The identifier of the user who last updated the entity  # noqa: E501

        :param updated_by: The updated_by of this FolderableDto.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

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
        if issubclass(FolderableDto, dict):
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
        if not isinstance(other, FolderableDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderableDto):
            return True

        return self.to_dict() != other.to_dict()
