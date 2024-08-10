import unittest
from unittest.mock import AsyncMock, patch
from russelCache.russel import RusselClient
from russelCache.russelExceptions import CacheClientError


class TestRusselClient(unittest.TestCase):
    def setUp(self):
        self.client = RusselClient(base_url="http://localhost:8000")

    @patch('aiohttp.ClientSession.post', new_callable=AsyncMock)
    async def test_set(self, mock_post):
        mock_post.return_value.__aenter__.return_value.json = AsyncMock(return_value={'is_success': True, 'data': None})
        response = await self.client.set("my_cluster", "my_key", "my_value")
        self.assertTrue(response.is_success)

    @patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
    async def test_get(self, mock_get):
        mock_get.return_value.__aenter__.return_value.json = AsyncMock(return_value={'is_success': True, 'data': "my_value"})
        response = await self.client.get("my_cluster", "my_key")
        self.assertEqual(response.data, "my_value")

    @patch('aiohttp.ClientSession.delete', new_callable=AsyncMock)
    async def test_delete(self, mock_delete):
        mock_delete.return_value.__aenter__.return_value.json = AsyncMock(return_value={'is_success': True, 'data': None})
        response = await self.client.delete("my_cluster", "my_key")
        self.assertTrue(response.is_success)

    @patch('aiohttp.ClientSession.post', new_callable=AsyncMock)
    async def test_set_cluster(self, mock_post):
        mock_post.return_value.__aenter__.return_value.json = AsyncMock(return_value={'is_success': True, 'data': None})
        response = await self.client.set_cluster("my_cluster")
        self.assertTrue(response.is_success)

