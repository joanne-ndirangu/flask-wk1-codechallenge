from flask import Flask
from flask_migrate import Migrate
from models import db, Restaurant


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)
db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555)
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Hello there</h1>'

# @app.route('/restaurants')

# @app.route('/restaurants/<int:id>')