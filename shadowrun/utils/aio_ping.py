import aiohttp
from .get_host import _host

async def ping():
    async with aiohttp.request("GET", _host()) as r:
        return int(r.status)
        
