from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Welcome to Pizza Restaurants</h1>'

# GET /restaurants
@app.route('/restaurants')
def getrestaurants():

    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurants.append(restaurant_dict)

    response = make_response(
        jsonify(restaurants),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

from flask import request

# GET /restaurants/:id, DELETE /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def get_or_delete_restaurant(id):
    ourrestaurant = Restaurant.query.filter_by(id=id).first()

    if ourrestaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404

    if request.method == 'GET':
        restaurantobj = {
            "id": ourrestaurant.id,
            "name": ourrestaurant.name,
            "address": ourrestaurant.address
        }
        resp = make_response(jsonify(restaurantobj), 200)
        return resp

# DELETE /restaurants/:id
    elif request.method == 'DELETE':
        restaurant_pizzas = RestaurantPizza.query.filter_by(restaurant_id=id).all()
        for restaurant_pizza in restaurant_pizzas:
            db.session.delete(restaurant_pizza)

        db.session.delete(ourrestaurant)
        db.session.commit()

        response_body = {
            # "delete_successful": True,
            "message": "Restaurant deleted."
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response

# GET /pizzas
@app.route('/pizzas')
def getpizzas():

    pizzas = []
    for pizza in Pizza.query.all():
        pizza_dict = {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
            "created at": pizza.created_at,
            "updated at": pizza.updated_at
        }
        pizzas.append(pizza_dict)

    response = make_response(
        jsonify(pizzas),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

# POST /restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def post_restaurant_pizzas():
    new_restaurant_pizza = RestaurantPizza(
            id=request.form.get("pizza_id"),
            pizza_id=request.form.get("pizza_id"),
            restaurant_id=request.form.get("restaurant_id"),
            price=request.form.get("price"),
            created_at=request.form.get("created_at"),
            updated_at=request.form.get("updated_at")
        )

    db.session.add(new_restaurant_pizza)
    db.session.commit()

    restaurant_pizza_dict = new_restaurant_pizza.to_dict()

    response = make_response(
        jsonify(restaurant_pizza_dict),
        201
        )

    return response