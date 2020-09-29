"""
STAGE 0 of Pipeline
Perform memoized downloading of raw data files from online sources
"""

# import re
import os
from subprocess import STDOUT
import time
import subprocess as sub
from time import sleep
# from typing import List
# from bs4 import BeautifulSoup, element
# from requests import Response, request
# from models.name_search import NameSearch

###############################
# Setup data dir and file paths
###############################

# Compute dirname of this file
dirname: str = os.path.dirname(os.path.realpath(__file__))

# Define path to data dir
dataDirPath = os.path.realpath(os.path.join(dirname, '..', '..', 'mpcdata'))

# Test data dir exists called 'mpcdata'
isDataDir: bool = os.path.isdir(dataDirPath)


# If data dir does not exist, create it
if not isDataDir:
    print("Data directory %s does not exist. Creating ..." % dataDirPath)
    sleep(1)
    try:
        os.mkdir(dataDirPath)
    except OSError:
        print("Creation of the directory %s failed" % dataDirPath)
    else:
        print("Successfully created the directory %s " % dataDirPath)

# Compute path to raw-html file
comet_html_file: str = dataDirPath + '/raw_mpc.html'

# Path to downloaded json file
asteroid_json_file = dataDirPath + '/cometels.json'

# Path to csv file to be created in next stage
name_search_items_csv_file: str = dataDirPath + "/minor_planets_names.csv"


############################
# Download remote data files
############################


if __name__ == '__main__':

    CMD1 = [
        # Download raw_mpc.html
        "/usr/bin/env", "curl", "-s",
        'https://www.minorplanetcenter.net/iau/lists/MPNames.html',
        '-o', comet_html_file,
    ]

    CMD2 = [
        # Download cometels.json.gz
        "/usr/bin/env", "curl", "-s",
        'https://www.minorplanetcenter.net/Extended_Files/cometels.json.gz',
        '-o', f"{asteroid_json_file}.gz",
    ]

    CMD3 = [
        # Unzip and force overwrite cometels.json.gz
        "/usr/bin/env", "gunzip", "-f", f"{asteroid_json_file}.gz"
    ]

    # Try to perform tasks in parallel
    proc1 = sub.Popen(CMD1)
    sub.Popen(CMD2).wait()
    sub.Popen(CMD3).wait()
    proc1.wait()
