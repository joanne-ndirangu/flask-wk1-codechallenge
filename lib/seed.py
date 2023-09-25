from faker import Faker
from random import choice as rc
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

# db.init_app(app)
fake = Faker()

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()

# restaurants table data
    restaurants = []
    for _ in range(40):
        restaurant = Restaurant(name=fake.name(), address=fake.address())
        restaurants.append(restaurant)

    db.session.add_all(restaurants)
    db.session.commit()
    print("Restaurants successfully added to the database.")

# pizza table data
    pizzas = []
    for _ in range(40):
        ingredients = ', '.join(fake.words())
        pizza = Pizza(
            name=fake.word(),
            ingredients=ingredients,
            created_at=fake.past_datetime(),
            updated_at=fake.past_datetime()
            )
        pizzas.append(pizza)

    db.session.add_all(pizzas)
    db.session.commit()
    print("Pizzas successfully added to the database.")

# restaurant pizzas table data
    restaurant_pizzas = []
    for restaurant_pizza in restaurant_pizzas:
        for _ in range(10):
            pizza = rc(pizzas)
            price = fake.random_int(min=1, max=30)
            restaurant_pizza = RestaurantPizza(
                restaurant_id=restaurant.id,
                pizza_id=pizza.id,
                price=price
            )
            restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    print("Restaurant-Pizza relationships successfully added to the database.")


print("DONE")