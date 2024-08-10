import aiohttp
import asyncio

class ApiResponse:
    def __init__(self, is_success, data):
        self.is_success = is_success
        self.data = data

    @staticmethod
    def from_dict(data):
        return ApiResponse(
            is_success=data.get('is_success'),
            data=data.get('data')
        )

    def decode_data(self):
        if isinstance(self.data, list):
            return bytes(self.data).decode('utf-8')
        return self.data

class RusselClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def _handle_response(self, response):
        if response.status != 200:
            data = await response.json()
            raise Exception(data.get("data", "Unknown error"))
        data = await response.json()
        return ApiResponse.from_dict(data)

    async def set(self, cluster, key, value):
        url = f"{self.base_url}/api/set"
        payload = {"cluster": cluster, "key": key, "value": value}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                return await self._handle_response(response)

    async def get(self, cluster, key):
        url = f"{self.base_url}/api/get/{cluster}/{key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await self._handle_response(response)

    # Other methods like delete, clear_cluster, etc., would follow the same pattern
