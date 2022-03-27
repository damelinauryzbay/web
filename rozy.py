from flask import Flask
from flask import render_template
from data import db_session
import requests
# import sqlalchemy
app = Flask(__name__)
colors = ['red', 'blue']
number_of_roses = 0
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


class ShopImage():
    def show_map(self, address):
        self.map_request = f"http://static-maps.yandex.ru/1.x/?ll=52.268104,76.947450&l=map"


@app.route('/')
@app.route('/rozy')
def index():
    return render_template("design.html")


@app.route('/roses')
def roses():
    title = "Розы"
    head = "Голландские розы"
    price = 385
    return render_template("roses.html",
                           title=title, head=head, price=price)

#
# def main():
#     db_session.global_init("db/blogs.db")
#     app.run()

#
# class Order:
#     __tablename__ = "orders"
#     name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#     email = sqlalchemy.Column(sqlalchemy.String,
#                               index=True, unique=True, nullable=True)
#     address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
#     phonenumber = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
#     numberofroses = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
#
#
# order = Order()
# number_of_roses += order.numberofroses


if __name__ == '__main__':
    app.run()