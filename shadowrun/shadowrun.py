from shadowrun import scheduler
from .ninja import shadow_run

def add_job(func=shadow_run, seconds=600):
    scheduler.add_job(func, "interval", seconds=seconds
