from flask import Flask, redirect
from flask import render_template
from data import db_session
from data.db_session import SqlAlchemyBase
import sqlalchemy
from user import RegisterForm

# import sqlalchemy
app = Flask(__name__)
colors = [('blue', 'white'), ('white', 'red'), ('yellow', 'orange')]
number_of_roses = 0
API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)


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
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/')
def index():
    # iage = adds
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
    name_of_photo = '/static/gvordiki.jpg'
    return render_template("flowers.html",
                           title=title, head=head, price=price, info=info, photo=name_of_photo, name=name)


@app.route('/wrapper')
def wrapper():
    return render_template("wrappers.html")


def main():
    db_session.global_init("db/blogs.db")
    app.run()


class Order:
    __tablename__ = "orders"
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    phonenumber = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    numberofroses = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


order = Order()
number_of_roses += order.numberofroses

if __name__ == '__main__':
    app.run()
