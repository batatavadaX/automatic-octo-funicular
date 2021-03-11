import aiohttp
from .get_host import host

class run:
    @staticmethod
    async def ping():
        async with aiohttp.request(
            "GET", host.host_()) as r:
            return int(r.status)
        
