from .utils import shadow_run
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class schedule:
    def __init__() -> None:
        scheduler = AsyncIOScheduler()
        scheduler.add_job(shadow_run, "interval", seconds=600)
        scheduler.start()
