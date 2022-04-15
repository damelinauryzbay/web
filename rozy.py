from flask import Flask, redirect, request
from flask import render_template
from data import db_session
from data.users import User
from data.orders import Order
import requests
import shutil
from os.path import abspath
from form.user import RegisterForm
from form.order import OrderForm
from flask_login import LoginManager, login_user, login_required, logout_user
from form.user_enter import SignInForm


app = Flask(__name__)
colors = [('blue', 'white'), ('white', 'red'), ('yellow', 'orange')]
number_of_roses = 0
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(

        )
        user.name = form.name.data
        user.email = form.email.data
        user.about = form.about.data
        user.set_password(form.password.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = OrderForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        order = Order()
        order.type_of_flower = form.type_of_flower.data
        order.type_of_wrapper = form.type_of_wrapper.data
        order.number_of_flowers = form.number_of_flowers.data
        db_sess.add(order)
        db_sess.commit()
        return redirect('/')
    return render_template('order.html', form=form)


@app.route('/', methods=['POST', 'GET'])
def index():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll=76.947450,52.268104&z=18&l=map"
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    filename = abspath('map.png')
    filename1 = filename[:-7] + "static\map.png"
    shutil.move(filename,
                filename1)
    return render_template("design.html", image='static\map.png')


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
    name_of_photo = '/static/pions.jpg'
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


@app.route('/wrapper')
def wrapper():
    return render_template("wrappers.html")


def main():
    db_session.global_init("db/blogs.db")
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
