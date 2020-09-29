# SBN Name Resolution Service

## What's This?

This repo houses scripts and code to build REST API services that enable a user to carry out cross-identification tasks. For example, if you want the official designation for "Halley's Comet" in order to perform a query on some astronomical-data service but do not know it ahead of time, then this service will allow you to perform a "fuzzy word search" (i.e. submit arbitrary text) and receive back candidate matches with meta data describing, e.g., in what domain a particular technical designation would be used.

## Code Features

- PostgresDB
- Flask API layer
- Connexion used to generate swagger interface
- Gunicorn/Apache used for producton deployment

## Live Site

## Development

- The codebase is operated using bash scripts that begin with the `\_` underscore character
- Clone the repo locally: `git clone XXX YYY; cd YYY`
- Run `cp .env-template .env` and edit the variables therein
- Always begin by `source _init_setup.sh`. This will:
  - Create/activate a python virtual environment
  - Install dependencies to virtual env
  - Make available to your shell the variables `.env`
- Run `./_dev_servers` to start the development servers locally; you can then view the swagger interface at `XXX`

## TODOs
