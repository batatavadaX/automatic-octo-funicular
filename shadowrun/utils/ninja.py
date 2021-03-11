from .aio_ping import run 

async def shadow_run():
    if await run.ping() == 200:
        print("online")
    else:
        print("offline")
