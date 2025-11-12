# SBN Name Resolution Service

## What's This?

This is a REST API to preform a "fuzzy word search" for comet/astroid names (i.e. submit arbitrary text) and receive back candidate matches with meta data describing, e.g., in what domain a particular technical designation would be used.

## Code Features

- PostgresDB
- Flask API layer
- Connexion used to generate swagger interface
- Gunicorn/Docker used for production deployment

## Development

### Name-Search-Build

- Before the REST APIs will work, you need to set up the PostgreSQL database with the indexed tables, and populate them with data that we get by downloading the latest files from the MPC.
- To build the indexed tables in your postgresql database, you need to to have the `pg_trgm` extension made available to your system.
  - If you are on a Mac, then the postgresql installed via homebrew will have this already available
  - If youre on linux, then you'll need to have the `postgresql-contrib` installed
- Log into your database and run the following query to enable the relevant indexing: `CREATE EXTENSION pg_trgm;`
- You can now run a pipeline using the `_name_search_build` script to download the files from MPC, clean the data, and load into the postgresql db.

### APIs

- If you have nodemon globally installed, then you can develop your api code and have it automatically update on changes by running `_develop_apis`. Otherwise, just run `python src/api/app.py`

### Docker

The repo ships with a `Dockerfile` (Python 3.13 slim) and `docker-compose.yml` for running the API in a container in production mode:

1. Ensure your `.env` file contains a valid `API_PORT` (the container no longer sets a default) and any other runtime settings expected by the app.
2. Build and run with `docker compose up --build`.
3. The compose service uses `restart: unless-stopped`, loads the `.env`, and publishes the container port so `${API_PORT}` inside the container is exposed on the same port on the host.

All application dependencies are synced via `uv sync --frozen --no-dev --no-install-project` during the image build so the runtime matches the exact versions pinned in `uv.lock`.

### Connexion 3, Uvicorn, and async readiness

The API now runs on Connexion 3, which exposes an ASGI application. To support that, the gunicorn manager launches `uvicorn.workers.UvicornWorker` instances instead of classic WSGI workers. Each gunicorn worker process embeds a Uvicorn event loop. Synchronous Flask handlers still run exactly as before (each worker behaves like a single blocking Python thread), but whenever you `await` inside a handler, the event loop offloads the async task and continues serving other requests—very similar to Node.js’s event-loop model. In short: gunicorn still supervises `N` worker processes, but each one is powered by Uvicorn so the stack is ready for modern async web development whenever we choose to adopt it.

It is recommended that you make the gunicorn-powered server accesible to the outside world by proxy-passing requests through an https-enabled web server like apache.
