__version__ = "0.1.0"

import optparse
import os
import json

from flask import Flask

# from .. import models
from . import views

app = Flask(__name__)


def create_app():

    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "dev-key"

    # views.register_blueprint(app)
    app.register_blueprint(views.module)

    return app


def get_program_options(default_host="127.0.0.1", default_port="8080"):

    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", default=default_host)
    parser.add_option("-P", "--port", default=default_port)
    parser.add_option("-d", "--debug", action="store_true", dest="debug")

    options, _ = parser.parse_args()
    return options
