from flask import Blueprint, jsonify, request
from handlers import db_handler

api = Blueprint('base', __name__)


@api.route("/")
def home():

    return jsonify(
        {"message": "Welcome to Flood Backend"}
    )


@api.route("/product", methods=['GET', 'POST'])
def product():

    keyword = request.json.get('product')

    product_data = db_handler.get_product(keyword)

    return jsonify({
        "data": product_data
    })
