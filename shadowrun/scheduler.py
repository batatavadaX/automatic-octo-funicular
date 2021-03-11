from .utils import shadow_run
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class schedule:
    @staticmethod
    async def sh():
        scheduler = AsyncIOScheduler()
        scheduler.add_job(shadow_run, "interval", seconds=600)
        scheduler.start()
