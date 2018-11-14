# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.entity import Entity  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_decreeses_post(self):
        """Test case for decreeses_post

        Получение похожих приказов
        """
        text = null()
        response = self.client.open(
            '/api/decreeses',
            method='POST',
            data=json.dumps(text),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_extract_post(self):
        """Test case for extract_post

        Извлечение меток из заявления
        """
        text = null()
        response = self.client.open(
            '/api/extract',
            method='POST',
            data=json.dumps(text),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
