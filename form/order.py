from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class OrderForm(FlaskForm):
    type_of_flower = StringField('Вид цветка', validators=[DataRequired()])
    type_of_wrapper = StringField('Тип обертки', validators=[DataRequired()])
    number_of_flowers = IntegerField('Количество цветов', validators=[DataRequired()])
    submit = SubmitField('Войти')