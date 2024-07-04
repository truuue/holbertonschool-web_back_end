#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import unittest
from unittest import mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @mock.patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json function."""
        test_url = "http://example.com"
        test_payload = {"payload": True}
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
