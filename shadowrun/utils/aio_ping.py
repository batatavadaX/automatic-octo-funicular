import aiohttp
from .get_host import host

async def ping():
    masync with aiohttp.request("GET", host.host_()) as r:
        return int(r.status)
        
