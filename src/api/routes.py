"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Product, Cart
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    serializer = list(map( lambda product : product.serialize() , products))
    if serializer is None:
        return jsonify({"msg" : "no products to get"}), 400
    return jsonify({"results": serializer , "msg": "all products got"}), 200

#quiero el carts del user que te paso como param 
@api.route("/carts/<int:user_id>", methods=["GET"])
def get_carts_user(user_id):
    carts = Cart.query.filter_by(user_id=user_id)
    serializer = list(map(lambda product: product.serialize(), carts))
    return jsonify({"results": serializer, "msg": "pericopalote"}), 200

@api.route("/newProduct", methods=["POST"])
def create_product():
    new_product_name = request.json.get("name")
    new_product_price = request.json.get("price")
    new_product = Product(
        product_name = new_product_name,
        product_price=new_product_price
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"msg":"new product created", "results": new_product.serialize()}),200