#!/usr/bin/env python3
"""Generic utilities for github org client."""
import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception):
        """Test access_nested_map function for exception."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


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
