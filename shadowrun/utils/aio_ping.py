import aiohttp
from .get_host import _host

async def ping():
    try:
        async with aiohttp.request("GET", _host()) as r:
            if r.status == 200:
                print("online")
            else:
                print("offline")
    except Exception:
         print("Can't Connect")
        
