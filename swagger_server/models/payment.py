# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.buyer_info import BuyerInfo
from swagger_server.models.credit_card_info import CreditCardInfo
from swagger_server import util


class Payment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, buyer_info: BuyerInfo=None, checkout_id: str=None, credit_card_info: CreditCardInfo=None, payment_orders: List[str]=None, seller_account: str=None, amount: str=None, currency: str=None, payment_order_id: str=None):  # noqa: E501
        """Payment - a model defined in Swagger

        :param buyer_info: The buyer_info of this Payment.  # noqa: E501
        :type buyer_info: BuyerInfo
        :param checkout_id: The checkout_id of this Payment.  # noqa: E501
        :type checkout_id: str
        :param credit_card_info: The credit_card_info of this Payment.  # noqa: E501
        :type credit_card_info: CreditCardInfo
        :param payment_orders: The payment_orders of this Payment.  # noqa: E501
        :type payment_orders: List[str]
        :param seller_account: The seller_account of this Payment.  # noqa: E501
        :type seller_account: str
        :param amount: The amount of this Payment.  # noqa: E501
        :type amount: str
        :param currency: The currency of this Payment.  # noqa: E501
        :type currency: str
        :param payment_order_id: The payment_order_id of this Payment.  # noqa: E501
        :type payment_order_id: str
        """
        self.swagger_types = {
            'buyer_info': BuyerInfo,
            'checkout_id': str,
            'credit_card_info': CreditCardInfo,
            'payment_orders': List[str],
            'seller_account': str,
            'amount': str,
            'currency': str,
            'payment_order_id': str
        }

        self.attribute_map = {
            'buyer_info': 'buyer_info',
            'checkout_id': 'checkout_id',
            'credit_card_info': 'credit_card_info',
            'payment_orders': 'payment_orders',
            'seller_account': 'seller_account',
            'amount': 'amount',
            'currency': 'currency',
            'payment_order_id': 'payment_order_id'
        }

        self._buyer_info = buyer_info
        self._checkout_id = checkout_id
        self._credit_card_info = credit_card_info
        self._payment_orders = payment_orders
        self._seller_account = seller_account
        self._amount = amount
        self._currency = currency
        self._payment_order_id = payment_order_id

    @classmethod
    def from_dict(cls, dikt) -> 'Payment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Payment of this Payment.  # noqa: E501
        :rtype: Payment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def buyer_info(self) -> BuyerInfo:
        """Gets the buyer_info of this Payment.


        :return: The buyer_info of this Payment.
        :rtype: BuyerInfo
        """
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, buyer_info: BuyerInfo):
        """Sets the buyer_info of this Payment.


        :param buyer_info: The buyer_info of this Payment.
        :type buyer_info: BuyerInfo
        """
        if buyer_info is None:
            raise ValueError("Invalid value for `buyer_info`, must not be `None`")  # noqa: E501

        self._buyer_info = buyer_info

    @property
    def checkout_id(self) -> str:
        """Gets the checkout_id of this Payment.


        :return: The checkout_id of this Payment.
        :rtype: str
        """
        return self._checkout_id

    @checkout_id.setter
    def checkout_id(self, checkout_id: str):
        """Sets the checkout_id of this Payment.


        :param checkout_id: The checkout_id of this Payment.
        :type checkout_id: str
        """
        if checkout_id is None:
            raise ValueError("Invalid value for `checkout_id`, must not be `None`")  # noqa: E501

        self._checkout_id = checkout_id

    @property
    def credit_card_info(self) -> CreditCardInfo:
        """Gets the credit_card_info of this Payment.


        :return: The credit_card_info of this Payment.
        :rtype: CreditCardInfo
        """
        return self._credit_card_info

    @credit_card_info.setter
    def credit_card_info(self, credit_card_info: CreditCardInfo):
        """Sets the credit_card_info of this Payment.


        :param credit_card_info: The credit_card_info of this Payment.
        :type credit_card_info: CreditCardInfo
        """

        self._credit_card_info = credit_card_info

    @property
    def payment_orders(self) -> List[str]:
        """Gets the payment_orders of this Payment.


        :return: The payment_orders of this Payment.
        :rtype: List[str]
        """
        return self._payment_orders

    @payment_orders.setter
    def payment_orders(self, payment_orders: List[str]):
        """Sets the payment_orders of this Payment.


        :param payment_orders: The payment_orders of this Payment.
        :type payment_orders: List[str]
        """

        self._payment_orders = payment_orders

    @property
    def seller_account(self) -> str:
        """Gets the seller_account of this Payment.


        :return: The seller_account of this Payment.
        :rtype: str
        """
        return self._seller_account

    @seller_account.setter
    def seller_account(self, seller_account: str):
        """Sets the seller_account of this Payment.


        :param seller_account: The seller_account of this Payment.
        :type seller_account: str
        """

        self._seller_account = seller_account

    @property
    def amount(self) -> str:
        """Gets the amount of this Payment.


        :return: The amount of this Payment.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount: str):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.
        :type amount: str
        """

        self._amount = amount

    @property
    def currency(self) -> str:
        """Gets the currency of this Payment.


        :return: The currency of this Payment.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this Payment.


        :param currency: The currency of this Payment.
        :type currency: str
        """

        self._currency = currency

    @property
    def payment_order_id(self) -> str:
        """Gets the payment_order_id of this Payment.


        :return: The payment_order_id of this Payment.
        :rtype: str
        """
        return self._payment_order_id

    @payment_order_id.setter
    def payment_order_id(self, payment_order_id: str):
        """Sets the payment_order_id of this Payment.


        :param payment_order_id: The payment_order_id of this Payment.
        :type payment_order_id: str
        """

        self._payment_order_id = payment_order_id
