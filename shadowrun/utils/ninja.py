from .aio_ping import ping

async def shadow_run():
    if await ping() == 200:
        print("online")
    else:
        print("offline")
