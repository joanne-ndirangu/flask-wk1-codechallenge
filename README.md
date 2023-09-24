# PHASE 4 CODE CHALLENGE 1: PIZZA RESTAURANTS
This is a Flask API project that manages Pizza Restaurants and their associated Pizzas. The goal is to build the functionality described in the deliverables below.

## Description
### Models
#### Restaurant
A Restaurant has many Pizzas through RestaurantPizza.
Add validations to the Restaurant model:
Must have a name less than 50 characters in length.
Must have a unique name.

#### Pizza
A Pizza has many Restaurants through RestaurantPizza.

#### RestaurantPizza
A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.
Add validations to the RestaurantPizza model:
Must have a price between 1 and 30.

## Project Setup
### Requirements
Ubuntu

Visual studio code

Stable internet connection

Working web browser

### Installation Process
1. Clone the repository onto your computer by opening your ubuntu terminal and running the instruction below:
``` git clone git@github.com:joanne-ndirangu/flask-wk1-codechallenge.git```
2. Once cloned navigate into your the directory using
``` cd  flask-wk1-codechallenge```
3. Open the code on your visual studio code by typing still on the terminal
``` code .```
4. Install dependencies: ```pipenv install```
5. Open your terminal and enter ```python3 lib/seed.py``` to start add data to you tables.
6. Start the Flask server with ```flask run```

## Author
Joanne Ndirangu.

## license
MIT License

Copyright (c) [2023] [Joanne Ndirangu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.