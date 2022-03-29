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
    name = 'голландской розы'
    price = 385
    info = 'Голландские розы — лидеры продаж среди многочисленных цветочных композиций. Даже букет с простым ' \
           'оформлением, отсутствием декоративных элементов и других представителей ароматного мира ' \
           'флоры выглядит идеальным!'
    name_of_photo = '/static/roses.jpg'
    return render_template("flowers.html",
                           title=title, head=head, price=price, info=info, photo=name_of_photo, name=name)

@app.route('/chrys')
def chrys():
    title = "Хризантемы"
    head = "Хризантемы"
    name = 'хризантемы'
    price = 385
    info = 'Цветы хризантемы – небольшие цветки декоративно-овощного растения. Эти милые цветы впишутся в любой ' \
           'интерьер и станут прелестным подарком.'
    name_of_photo = '/static/chrys.png'
    return render_template("flowers.html",
                           title=title, head=head, price=price, info=info, photo=name_of_photo, name=name)


@app.route('/pions')
def pions():
    title = "Пионы"
    head = "Пионы Гардения"
    name = 'пиона Гардения'
    price = 490
    info = 'Пионы гардения - прекрасные и пышные цветы так излюбленные многими людьми. Белые лепестки задорно ' \
           'искрятся в солнечных лучах благодаря нежному розовому отливу. Они впишутся в любой праздничный букет!'
    name_of_photo = '/static/chrys.jpg'
    return render_template("flowers.html",
                           title=title, head=head, price=price, info=info, photo=name_of_photo, name=name)

@app.route('/gvozdiki')
def gvoz():
    title = "Гвоздики"
    head = "Гвоздики Дон Педро"
    name = 'гвоздики Дон Педро'
    price = 430
    info = 'Гвоздики Дон Педро - самые красные и популярные гвоздики. Являются символом любви и будут ' \
           'лучшим выбором для подарка любимому человеку!'
    name_of_photo = '/static/gvozdiki.jpg'
    return render_template("flowers.html",
                           title=title, head=head, price=price, info=info, photo=name_of_photo, name=name)

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
