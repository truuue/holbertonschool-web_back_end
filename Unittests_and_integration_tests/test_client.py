#!/usr/bin/env python3
"""Test client module."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "test_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, {"login": "test_org"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url."""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"}
            client = GithubOrgClient("test_org")
            result = client._public_repos_url
            self.assertEqual(
                result, "https://api.github.com/orgs/test_org/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos."""
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
            client = GithubOrgClient("test_org")
            result = client.public_repos

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
