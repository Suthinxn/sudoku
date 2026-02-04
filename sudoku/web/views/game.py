from flask import Blueprint

module = Blueprint("game", __name__, url_prefix="/")


@module.route("/")
def index():
    return "<h1>This is Game Page (Auto Discovered!)</h1>"
