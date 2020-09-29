# SBN Name Resolution Service

## What's This?

This repo houses scripts and code to build REST API services that enable a user to carry out cross-identification tasks. For example, if you want the official designation for "Halley's Comet" in order to perform a query on some astronomical-data service but do not know it ahead of time, then this service will allow you to perform a "fuzzy word search" (i.e. submit arbitrary text) and receive back candidate matches with meta data describing, e.g., in what domain a particular technical designation would be used.

## Code Features

- PostgresDB
- Flask API layer
- Connexion used to generate swagger interface
- Gunicorn/Apache used for production deployment

## Development

### Common Steps

This repo has code for:

- Building the indexed postgresdb
- Running a flask-connexion API
- Testing

The following steps are needed to set up the code base whatever aspect you want to work on:

- The codebase is operated using bash scripts that begin with the `\_` underscore character
- Prerequisites for local development:
  - Running postgresql server with credentials to read/write
  - python (& pip) v3.5+
- Clone the repo locally:
  ```
      git clone https://github.com/Small-Bodies-Node/sbn-name-resolution
      cd sbn-name-resolution
  ```
- Run `cp .env-template .env` and edit the variables therein
- Always begin by `source _init_setup.sh`. This will:
  - Create/activate a python virtual environment
  - Install dependencies to virtual env
  - Make available to your shell the variables `.env`

### Name-Search-Build

- To build the indexed tables in your postgresql database, you need to to have the `pg_trgm` extension made available to your system.
  - If you are on a Mac, then the postgresql installed via homebrew will have this already available
  - If youre on linux, then you'll need to have the `postgresql-contrib` installed
- Log into your database and run the following query to enable the relevant indexing: `CREATE EXTENSION pg_trgm;`
- You can now run a pipeline using the `_name_search_build` script to download the files from MPC, clean the data, and load into the postgresql db.

### APIs

- If you have nodemon globally installed, then you can develop your api code and have it automatically update on changes by running `_develop_apis`. Otherwise, just run `python src/api/app.py`

## Deployment

A script is supplied called `_gunicorn_manager` that takes the arguments `start|stop|status|restart` to launch the app as a background process with the gunicorn WSGI server for production serving. The number of workers is controlled with the env variable `LIVE_GUNICORN_INSTANCES`. If you have trouble getting gunicorn to work, you can run the manager with 0 as the 2nd argument to start it off in non-daemon mode.

It is recommended that you make the gunicorn-powered server accesible to the outside world by proxy-passing requests through an https-enabled web server like apache. Contact me if you need assistance setting that up.
