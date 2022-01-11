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


class BaseResponseOfRefreshBatchDto(object):
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
        'body': 'RefreshBatchDto',
        'code': 'int'
    }

    attribute_map = {
        'body': 'body',
        'code': 'code'
    }

    def __init__(self, body=None, code=None, _configuration=None):  # noqa: E501
        """BaseResponseOfRefreshBatchDto - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._body = None
        self._code = None
        self.discriminator = None

        if body is not None:
            self.body = body
        if code is not None:
            self.code = code

    @property
    def body(self):
        """Gets the body of this BaseResponseOfRefreshBatchDto.  # noqa: E501


        :return: The body of this BaseResponseOfRefreshBatchDto.  # noqa: E501
        :rtype: RefreshBatchDto
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BaseResponseOfRefreshBatchDto.


        :param body: The body of this BaseResponseOfRefreshBatchDto.  # noqa: E501
        :type: RefreshBatchDto
        """

        self._body = body

    @property
    def code(self):
        """Gets the code of this BaseResponseOfRefreshBatchDto.  # noqa: E501


        :return: The code of this BaseResponseOfRefreshBatchDto.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this BaseResponseOfRefreshBatchDto.


        :param code: The code of this BaseResponseOfRefreshBatchDto.  # noqa: E501
        :type: int
        """

        self._code = code

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
        if issubclass(BaseResponseOfRefreshBatchDto, dict):
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
        if not isinstance(other, BaseResponseOfRefreshBatchDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseResponseOfRefreshBatchDto):
            return True

        return self.to_dict() != other.to_dict()
