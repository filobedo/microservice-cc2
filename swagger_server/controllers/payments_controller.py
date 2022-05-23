import connexion
import six

from swagger_server.models.api_return import ApiReturn  # noqa: E501
from swagger_server.models.payment import Payment  # noqa: E501
from swagger_server import util


def make_payments(body):  # noqa: E501
    """Request payments

     # noqa: E501

    :param body: Request a payments
    :type body: dict | bytes

    :rtype: ApiReturn
    """
    if connexion.request.is_json:
        body = Payment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
