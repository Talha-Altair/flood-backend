from flask import Blueprint, jsonify

api = Blueprint('base', __name__)


@api.route("/")
def home():

    return jsonify(
        {"message": "Welcome to Flood Backend"}
    )
