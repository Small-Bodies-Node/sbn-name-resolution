"""
    Gunicorn workers-config file
    Logic to decide how many workers to launch based on .env variable `LIVE_GUNICORN_INSTANCES`
    NOTE: some gunicorn params (e.g. --name) don't seem to work from here so must be called from the command line
"""

import multiprocessing
from env import ENV


def _auto_worker_count() -> int:
    count = multiprocessing.cpu_count() or 1
    return count


configured_workers = ENV.LIVE_GUNICORN_INSTANCES
workers: int = configured_workers if configured_workers > 0 else _auto_worker_count()
