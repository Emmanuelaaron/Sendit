from flask import Flask, request, jsonify, json
from api.models import orders, Orders, Users, users


app = Flask(__name__)


@app.route("/")
def index():
    return "Do you wanna send it?, if yes send it"


@app.route("/api/v1/users/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    for user in Users.all_users():
        if user['username'] == username:
            return jsonify({
                "message": "Username already exists!"
            }), 400
        if user['email'] == email:
            return jsonify({
                "message": "Email already exists!"
            }), 400
      
    my_account = Users(username, email, password)
    message = my_account.signup()
    return jsonify(message), 201


@app.route("/api/v1/users/login", methods=["POST"])
def login():
    data = request.get_json()
    password = data.get("password")
    email = data.get("email")
    for user in users:
        if user["password"] == password and user["email"] == email:
            return jsonify({
                "message": "sucessfully logged in"
            })
        else:
            return jsonify({
                "message": "Incorrect Loggib credentials!"
            })


@app.route("/api/v1/parcels", methods=["POST"])
def create_parcel_delivery_order():
            data = request.get_json()
            item = data.get("item")
            pickup_location = data.get("pickup_location")
            destination = data.get("destination")
            user_id = data.get("user_id")
            print(Users.all_users())
            for user in Users.all_users():
                if user["user_id"] != user_id:
                    return jsonify({
                        "message": "Invalid user Id"
                    }), 400
 
            my_orders = Orders(item, pickup_location, destination)
            message = my_orders.create_parcel_delivery_order(user_id)
            return jsonify(message), 201


@app.route("/api/v1/parcels", methods=["GET"])
def get_all_orders():
    return jsonify({
        "message": Orders.get_all_orders()
    }), 201


@app.route("/api/v1/parcels/<int:parcel_id>", methods=["GET"])
def get_specific_order(parcel_id):
    for order in orders:
        if order["parcel_id"] == parcel_id:
            return jsonify(
                order
            ), 201
    return jsonify({
                "message": "Parcel ID does not exist!"
            }), 400


@app.route("/api/v1/users/<int:user_id>/parcels")
def get_all_orders_specific_user_(user_id):
    users_orders = []
    for order in orders:
        if order["user_id"] == user_id:
            users_orders.append(order)
    if len(users_orders) == 0:
        return jsonify({
            "message": "User does not have any orders"
        }), 400
    return jsonify(
                users_orders
            ), 201
    
@app.route("/api/v1/parcels/<int:parcel_id>/cancel", methods=['PUT'])
def cancel_order(parcel_id):
    for order in orders:
        if order["parcel_id"] == parcel_id:
            if order["status"] == "pending":
                order["status"] = "cancelled"
                return jsonify({
                    "message": "sucessfully cancelled!"
                }), 201
        return jsonify({
            "message": "Order can not be cancelled! Already delivered"
        }), 400
    return jsonify({
        "message": "No Orders Yet!"
    }), 400