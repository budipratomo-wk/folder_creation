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


class QueryDto(object):
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
        'definition': 'PivotDefinitionDto',
        'dependencies': 'list[QueryDependencyDto]',
        'description': 'str',
        'history_revision': 'int',
        'id': 'str',
        'last_run': 'datetime',
        'last_run_by': 'str',
        'name': 'str',
        'parameters': 'list[QueryParameterDto]',
        'parent_id': 'str',
        'primary_query_result_id': 'str',
        'query_text': 'str',
        'temporary': 'bool',
        'type': 'str',
        'updated': 'datetime',
        'user_id': 'str',
        'version': 'int'
    }

    attribute_map = {
        'created': 'created',
        'definition': 'definition',
        'dependencies': 'dependencies',
        'description': 'description',
        'history_revision': 'historyRevision',
        'id': 'id',
        'last_run': 'lastRun',
        'last_run_by': 'lastRunBy',
        'name': 'name',
        'parameters': 'parameters',
        'parent_id': 'parentId',
        'primary_query_result_id': 'primaryQueryResultId',
        'query_text': 'queryText',
        'temporary': 'temporary',
        'type': 'type',
        'updated': 'updated',
        'user_id': 'userId',
        'version': 'version'
    }

    def __init__(self, created=None, definition=None, dependencies=None, description=None, history_revision=None, id=None, last_run=None, last_run_by=None, name=None, parameters=None, parent_id=None, primary_query_result_id=None, query_text=None, temporary=None, type=None, updated=None, user_id=None, version=None, _configuration=None):  # noqa: E501
        """QueryDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._definition = None
        self._dependencies = None
        self._description = None
        self._history_revision = None
        self._id = None
        self._last_run = None
        self._last_run_by = None
        self._name = None
        self._parameters = None
        self._parent_id = None
        self._primary_query_result_id = None
        self._query_text = None
        self._temporary = None
        self._type = None
        self._updated = None
        self._user_id = None
        self._version = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if definition is not None:
            self.definition = definition
        if dependencies is not None:
            self.dependencies = dependencies
        if description is not None:
            self.description = description
        if history_revision is not None:
            self.history_revision = history_revision
        if id is not None:
            self.id = id
        if last_run is not None:
            self.last_run = last_run
        if last_run_by is not None:
            self.last_run_by = last_run_by
        if name is not None:
            self.name = name
        if parameters is not None:
            self.parameters = parameters
        if parent_id is not None:
            self.parent_id = parent_id
        if primary_query_result_id is not None:
            self.primary_query_result_id = primary_query_result_id
        self.query_text = query_text
        if temporary is not None:
            self.temporary = temporary
        if type is not None:
            self.type = type
        if updated is not None:
            self.updated = updated
        if user_id is not None:
            self.user_id = user_id
        if version is not None:
            self.version = version

    @property
    def created(self):
        """Gets the created of this QueryDto.  # noqa: E501

        When the entity was created  # noqa: E501

        :return: The created of this QueryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this QueryDto.

        When the entity was created  # noqa: E501

        :param created: The created of this QueryDto.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def definition(self):
        """Gets the definition of this QueryDto.  # noqa: E501

        The pivot view's definition  # noqa: E501

        :return: The definition of this QueryDto.  # noqa: E501
        :rtype: PivotDefinitionDto
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this QueryDto.

        The pivot view's definition  # noqa: E501

        :param definition: The definition of this QueryDto.  # noqa: E501
        :type: PivotDefinitionDto
        """

        self._definition = definition

    @property
    def dependencies(self):
        """Gets the dependencies of this QueryDto.  # noqa: E501

        A structured list of dependencies that this query relies upon. This list is populated by the server from the query text. Each dependency model contains enough information to find the source object.  # noqa: E501

        :return: The dependencies of this QueryDto.  # noqa: E501
        :rtype: list[QueryDependencyDto]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this QueryDto.

        A structured list of dependencies that this query relies upon. This list is populated by the server from the query text. Each dependency model contains enough information to find the source object.  # noqa: E501

        :param dependencies: The dependencies of this QueryDto.  # noqa: E501
        :type: list[QueryDependencyDto]
        """

        self._dependencies = dependencies

    @property
    def description(self):
        """Gets the description of this QueryDto.  # noqa: E501

        The description of the query  # noqa: E501

        :return: The description of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryDto.

        The description of the query  # noqa: E501

        :param description: The description of this QueryDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 10000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `10000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def history_revision(self):
        """Gets the history_revision of this QueryDto.  # noqa: E501

        Historical revision number of this entity  # noqa: E501

        :return: The history_revision of this QueryDto.  # noqa: E501
        :rtype: int
        """
        return self._history_revision

    @history_revision.setter
    def history_revision(self, history_revision):
        """Sets the history_revision of this QueryDto.

        Historical revision number of this entity  # noqa: E501

        :param history_revision: The history_revision of this QueryDto.  # noqa: E501
        :type: int
        """

        self._history_revision = history_revision

    @property
    def id(self):
        """Gets the id of this QueryDto.  # noqa: E501

        The entity's unique identifier  # noqa: E501

        :return: The id of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryDto.

        The entity's unique identifier  # noqa: E501

        :param id: The id of this QueryDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_run(self):
        """Gets the last_run of this QueryDto.  # noqa: E501

        If non-null, indicates the last time this query was run.  # noqa: E501

        :return: The last_run of this QueryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this QueryDto.

        If non-null, indicates the last time this query was run.  # noqa: E501

        :param last_run: The last_run of this QueryDto.  # noqa: E501
        :type: datetime
        """

        self._last_run = last_run

    @property
    def last_run_by(self):
        """Gets the last_run_by of this QueryDto.  # noqa: E501

        If non-null, indicates the last user that ran the query.  # noqa: E501

        :return: The last_run_by of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._last_run_by

    @last_run_by.setter
    def last_run_by(self, last_run_by):
        """Sets the last_run_by of this QueryDto.

        If non-null, indicates the last user that ran the query.  # noqa: E501

        :param last_run_by: The last_run_by of this QueryDto.  # noqa: E501
        :type: str
        """

        self._last_run_by = last_run_by

    @property
    def name(self):
        """Gets the name of this QueryDto.  # noqa: E501

        The name of the query  # noqa: E501

        :return: The name of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryDto.

        The name of the query  # noqa: E501

        :param name: The name of this QueryDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 0):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this QueryDto.  # noqa: E501

        The query parameters  # noqa: E501

        :return: The parameters of this QueryDto.  # noqa: E501
        :rtype: list[QueryParameterDto]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this QueryDto.

        The query parameters  # noqa: E501

        :param parameters: The parameters of this QueryDto.  # noqa: E501
        :type: list[QueryParameterDto]
        """

        self._parameters = parameters

    @property
    def parent_id(self):
        """Gets the parent_id of this QueryDto.  # noqa: E501

        If non-null, indicates the parent of this entity. Must be modified through the folder api.  # noqa: E501

        :return: The parent_id of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this QueryDto.

        If non-null, indicates the parent of this entity. Must be modified through the folder api.  # noqa: E501

        :param parent_id: The parent_id of this QueryDto.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def primary_query_result_id(self):
        """Gets the primary_query_result_id of this QueryDto.  # noqa: E501

        The identifier of the primary query result  # noqa: E501

        :return: The primary_query_result_id of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._primary_query_result_id

    @primary_query_result_id.setter
    def primary_query_result_id(self, primary_query_result_id):
        """Sets the primary_query_result_id of this QueryDto.

        The identifier of the primary query result  # noqa: E501

        :param primary_query_result_id: The primary_query_result_id of this QueryDto.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                primary_query_result_id is not None and len(primary_query_result_id) > 32):
            raise ValueError("Invalid value for `primary_query_result_id`, length must be less than or equal to `32`")  # noqa: E501
        if (self._configuration.client_side_validation and
                primary_query_result_id is not None and len(primary_query_result_id) < 0):
            raise ValueError("Invalid value for `primary_query_result_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._primary_query_result_id = primary_query_result_id

    @property
    def query_text(self):
        """Gets the query_text of this QueryDto.  # noqa: E501

        Max size is 30000 characters.  Is required.  Must be a valid DML statement.  # noqa: E501

        :return: The query_text of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._query_text

    @query_text.setter
    def query_text(self, query_text):
        """Sets the query_text of this QueryDto.

        Max size is 30000 characters.  Is required.  Must be a valid DML statement.  # noqa: E501

        :param query_text: The query_text of this QueryDto.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and query_text is None:
            raise ValueError("Invalid value for `query_text`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                query_text is not None and len(query_text) > 30000):
            raise ValueError("Invalid value for `query_text`, length must be less than or equal to `30000`")  # noqa: E501
        if (self._configuration.client_side_validation and
                query_text is not None and len(query_text) < 0):
            raise ValueError("Invalid value for `query_text`, length must be greater than or equal to `0`")  # noqa: E501

        self._query_text = query_text

    @property
    def temporary(self):
        """Gets the temporary of this QueryDto.  # noqa: E501

        Denotes if this query is meant to be temporary.  Default is false.  # noqa: E501

        :return: The temporary of this QueryDto.  # noqa: E501
        :rtype: bool
        """
        return self._temporary

    @temporary.setter
    def temporary(self, temporary):
        """Sets the temporary of this QueryDto.

        Denotes if this query is meant to be temporary.  Default is false.  # noqa: E501

        :param temporary: The temporary of this QueryDto.  # noqa: E501
        :type: bool
        """

        self._temporary = temporary

    @property
    def type(self):
        """Gets the type of this QueryDto.  # noqa: E501

        This field exists for backwards compatibility only and will always be an empty string.  # noqa: E501

        :return: The type of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryDto.

        This field exists for backwards compatibility only and will always be an empty string.  # noqa: E501

        :param type: The type of this QueryDto.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated(self):
        """Gets the updated of this QueryDto.  # noqa: E501

        When the entity was last updated  # noqa: E501

        :return: The updated of this QueryDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this QueryDto.

        When the entity was last updated  # noqa: E501

        :param updated: The updated of this QueryDto.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def user_id(self):
        """Gets the user_id of this QueryDto.  # noqa: E501

        The owner of the entity  # noqa: E501

        :return: The user_id of this QueryDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this QueryDto.

        The owner of the entity  # noqa: E501

        :param user_id: The user_id of this QueryDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def version(self):
        """Gets the version of this QueryDto.  # noqa: E501

        The version of the current representation of the entity  # noqa: E501

        :return: The version of this QueryDto.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QueryDto.

        The version of the current representation of the entity  # noqa: E501

        :param version: The version of this QueryDto.  # noqa: E501
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
        if issubclass(QueryDto, dict):
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
        if not isinstance(other, QueryDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryDto):
            return True

        return self.to_dict() != other.to_dict()