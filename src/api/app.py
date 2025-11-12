"""
Entry point to Flask-Connexion API
"""

from typing import Dict
from connexion import FlaskApp
from flask import wrappers as FLW, jsonify
from flask_cors import CORS
from env import ENV
from services import database_provider
from services.name_search import name_search


def get_name_search(name: str) -> FLW.Response:
    """
    Controller for main name-search
    """
    top_matches: Dict = name_search(name)
    res: FLW.Response = jsonify(
        {
            "name": name,
            "matches": top_matches
        }
    )
    res.status_code = 200
    return res


###########################################
# BEGIN API
###########################################


app = FlaskApp(__name__)
# app.add_api('openapi.yaml', base_path=ENV.BASE_HREF)
app.add_api('openapi.yaml')
CORS(app.app)
application = app.app


@application.get('/hello')
def hello_world() -> FLW.Response:
    """Simple route to confirm server is alive"""
    response = jsonify({"message": "hello"})
    response.status_code = 200
    return response


@application.teardown_appcontext
def shutdown_session(exception: Exception = None) -> None:
    """ Boilerplate connexion code """
    database_provider.db_session.remove()


if __name__ == '__main__':
    app.run(port=ENV.API_PORT)
