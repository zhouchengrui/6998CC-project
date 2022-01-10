# coding: utf-8

"""
    AYLIEN News API

    The AYLIEN News API is the most powerful way of sourcing, searching and syndicating analyzed and enriched news content. It is accessed by sending HTTP requests to our server, which returns information to your client.   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Contact: support@aylien.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from aylien_news_api.configuration import Configuration


class Error(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'str',
        'detail': 'str',
        'id': 'str',
        'links': 'ErrorLinks',
        'status': 'str',
        'title': 'str'
    }

    attribute_map = {
        'code': 'code',
        'detail': 'detail',
        'id': 'id',
        'links': 'links',
        'status': 'status',
        'title': 'title'
    }

    def __init__(self, code=None, detail=None, id=None, links=None, status=None, title=None, local_vars_configuration=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._detail = None
        self._id = None
        self._links = None
        self._status = None
        self._title = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if detail is not None:
            self.detail = detail
        if id is not None:
            self.id = id
        if links is not None:
            self.links = links
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title

    @property
    def code(self):
        """Gets the code of this Error.  # noqa: E501


        :return: The code of this Error.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Error.


        :param code: The code of this Error.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def detail(self):
        """Gets the detail of this Error.  # noqa: E501


        :return: The detail of this Error.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.


        :param detail: The detail of this Error.  # noqa: E501
        :type detail: str
        """

        self._detail = detail

    @property
    def id(self):
        """Gets the id of this Error.  # noqa: E501


        :return: The id of this Error.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Error.


        :param id: The id of this Error.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def links(self):
        """Gets the links of this Error.  # noqa: E501


        :return: The links of this Error.  # noqa: E501
        :rtype: ErrorLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Error.


        :param links: The links of this Error.  # noqa: E501
        :type links: ErrorLinks
        """

        self._links = links

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501


        :return: The status of this Error.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.


        :param status: The status of this Error.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def title(self):
        """Gets the title of this Error.  # noqa: E501


        :return: The title of this Error.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error.


        :param title: The title of this Error.  # noqa: E501
        :type title: str
        """

        self._title = title

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Error):
            return True

        return self.to_dict() != other.to_dict()
