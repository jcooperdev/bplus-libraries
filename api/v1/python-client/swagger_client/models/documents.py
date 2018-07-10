# coding: utf-8

"""
    Paysafe Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Documents(object):
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
        'type': 'str',
        'number': 'str',
        'issuedby': 'str',
        'issued_day': 'str',
        'issued_month': 'str',
        'issued_year': 'str',
        'expires_day': 'str',
        'expires_month': 'str',
        'expires_year': 'str'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number',
        'issuedby': 'issuedby',
        'issued_day': 'issued_day',
        'issued_month': 'issued_month',
        'issued_year': 'issued_year',
        'expires_day': 'expires_day',
        'expires_month': 'expires_month',
        'expires_year': 'expires_year'
    }

    def __init__(self, type=None, number=None, issuedby=None, issued_day=None, issued_month=None, issued_year=None, expires_day=None, expires_month=None, expires_year=None):  # noqa: E501
        """Documents - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._number = None
        self._issuedby = None
        self._issued_day = None
        self._issued_month = None
        self._issued_year = None
        self._expires_day = None
        self._expires_month = None
        self._expires_year = None
        self.discriminator = None

        self.type = type
        self.number = number
        self.issuedby = issuedby
        self.issued_day = issued_day
        self.issued_month = issued_month
        self.issued_year = issued_year
        self.expires_day = expires_day
        self.expires_month = expires_month
        self.expires_year = expires_year

    @property
    def type(self):
        """Gets the type of this Documents.  # noqa: E501


        :return: The type of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Documents.


        :param type: The type of this Documents.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def number(self):
        """Gets the number of this Documents.  # noqa: E501


        :return: The number of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Documents.


        :param number: The number of this Documents.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def issuedby(self):
        """Gets the issuedby of this Documents.  # noqa: E501


        :return: The issuedby of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._issuedby

    @issuedby.setter
    def issuedby(self, issuedby):
        """Sets the issuedby of this Documents.


        :param issuedby: The issuedby of this Documents.  # noqa: E501
        :type: str
        """
        if issuedby is None:
            raise ValueError("Invalid value for `issuedby`, must not be `None`")  # noqa: E501

        self._issuedby = issuedby

    @property
    def issued_day(self):
        """Gets the issued_day of this Documents.  # noqa: E501


        :return: The issued_day of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._issued_day

    @issued_day.setter
    def issued_day(self, issued_day):
        """Sets the issued_day of this Documents.


        :param issued_day: The issued_day of this Documents.  # noqa: E501
        :type: str
        """
        if issued_day is None:
            raise ValueError("Invalid value for `issued_day`, must not be `None`")  # noqa: E501

        self._issued_day = issued_day

    @property
    def issued_month(self):
        """Gets the issued_month of this Documents.  # noqa: E501


        :return: The issued_month of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._issued_month

    @issued_month.setter
    def issued_month(self, issued_month):
        """Sets the issued_month of this Documents.


        :param issued_month: The issued_month of this Documents.  # noqa: E501
        :type: str
        """
        if issued_month is None:
            raise ValueError("Invalid value for `issued_month`, must not be `None`")  # noqa: E501

        self._issued_month = issued_month

    @property
    def issued_year(self):
        """Gets the issued_year of this Documents.  # noqa: E501


        :return: The issued_year of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._issued_year

    @issued_year.setter
    def issued_year(self, issued_year):
        """Sets the issued_year of this Documents.


        :param issued_year: The issued_year of this Documents.  # noqa: E501
        :type: str
        """
        if issued_year is None:
            raise ValueError("Invalid value for `issued_year`, must not be `None`")  # noqa: E501

        self._issued_year = issued_year

    @property
    def expires_day(self):
        """Gets the expires_day of this Documents.  # noqa: E501


        :return: The expires_day of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._expires_day

    @expires_day.setter
    def expires_day(self, expires_day):
        """Sets the expires_day of this Documents.


        :param expires_day: The expires_day of this Documents.  # noqa: E501
        :type: str
        """
        if expires_day is None:
            raise ValueError("Invalid value for `expires_day`, must not be `None`")  # noqa: E501

        self._expires_day = expires_day

    @property
    def expires_month(self):
        """Gets the expires_month of this Documents.  # noqa: E501


        :return: The expires_month of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._expires_month

    @expires_month.setter
    def expires_month(self, expires_month):
        """Sets the expires_month of this Documents.


        :param expires_month: The expires_month of this Documents.  # noqa: E501
        :type: str
        """
        if expires_month is None:
            raise ValueError("Invalid value for `expires_month`, must not be `None`")  # noqa: E501

        self._expires_month = expires_month

    @property
    def expires_year(self):
        """Gets the expires_year of this Documents.  # noqa: E501


        :return: The expires_year of this Documents.  # noqa: E501
        :rtype: str
        """
        return self._expires_year

    @expires_year.setter
    def expires_year(self, expires_year):
        """Sets the expires_year of this Documents.


        :param expires_year: The expires_year of this Documents.  # noqa: E501
        :type: str
        """
        if expires_year is None:
            raise ValueError("Invalid value for `expires_year`, must not be `None`")  # noqa: E501

        self._expires_year = expires_year

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Documents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
