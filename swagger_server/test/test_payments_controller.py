# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_return import ApiReturn  # noqa: E501
from swagger_server.models.payment import Payment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPaymentsController(BaseTestCase):
    """PaymentsController integration test stubs"""

    def test_make_payments(self):
        """Test case for make_payments

        Request payments
        """
        body = Payment()
        response = self.client.open(
            '/resource/payments',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
