"""SSOT FOR ENV VARIABLES"""

import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True, verbose=True)


class ENV():
    """ Class to store all env variables used in app """

    # String properties
    DB_HOST: Optional[str] = os.getenv("DB_HOST")
    DB_DIALECT: Optional[str] = os.getenv("DB_DIALECT")
    DB_USERNAME: Optional[str] = os.getenv("DB_USERNAME")
    DB_PASSWORD: Optional[str] = os.getenv("DB_PASSWORD")
    DB_DATABASE: Optional[str] = os.getenv("DB_DATABASE")
    BASE_HREF: Optional[str] = os.getenv("BASE_HREF")

    # Numeric properties
    LIVE_GUNICORN_INSTANCES: int = int(
        os.getenv("LIVE_GUNICORN_INSTANCES") or -1)
    API_PORT: int = int(
        os.getenv("API_PORT") or 5004)
    MAX_RESULTS: int = int(
        os.getenv("MAX_RESULTS") or 15)

    # Boolean Properties
    IS_DAEMON: bool = os.getenv("IS_DAEMON") == 'TRUE'


# Debugging block
# print("=========================")
# print(ENV.LIVE_GUNICORN_INSTANCES)
# print(ENV.LIVE_WORKER_INSTANCES)
# print(ENV.DEPLOYMENT_TIER)
# print(ENV.DB_DATABASE)
# print(ENV.DB_PASSWORD)
# print(ENV.DB_USERNAME)
# print()
# print(ENV.CATCH_LOG)
# print(ENV.CATCH_ARCHIVE_PATH)
# print(ENV.CATCH_CUTOUT_PATH)
# print(ENV.CATCH_THUMBNAIL_PATH)
# print(ENV.IS_DAEMON)
# print("=========================")
