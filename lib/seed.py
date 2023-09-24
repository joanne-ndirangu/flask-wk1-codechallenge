from faker import Faker
from random import choice as rc
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

# db.init_app(app)
fake = Faker()

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()

    restaurants = []
    for _ in range(40):
        restaurant = Restaurant(name=fake.company(), address=fake.address())
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()
    print("Restaurants successfully added to the database.")


    pizzas = []
    for _ in range(40):
        ingredients = ', '.join(fake.words())
        pizza = Pizza(name=fake.word(), ingredients=ingredients, created_at=fake.past_datetime(), updated_at=fake.past_datetime())
        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()
    print("Pizzas successfully added to the database.")


    # restaurant_pizzas = []

    # for restaurant in restaurants:
    #     for pizza in pizzas:
    #         is_available = rc([True, False])

    #         if is_available:
    #             price = fake.random_int(min=1, max=30)
    #         # Create the Pizza instance within the current session context
    #         pizza = Pizza(name=fake.word(), ingredients=ingredients, created_at=fake.past_datetime(), updated_at=fake.past_datetime())
    #         restaurant_pizza = RestaurantPizza(
    #             pizza_id=pizza.id,
    #             restaurant_id=restaurant.id,
    #             price=price,
    #             created_at=fake.past_datetime(),
    #             updated_at=fake.past_datetime()
    #         )
    #         restaurant_pizzas.append(restaurant_pizza)

    # db.session.add_all(restaurant_pizzas)
    # db.session.commit()
    # print("Restaurant-Pizza relationships successfully added to the database.")

print("DONE")