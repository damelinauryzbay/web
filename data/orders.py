import sqlalchemy
from data.db_session import SqlAlchemyBase


class Order(SqlAlchemyBase):
    __tablename__ = "orders"
    type_of_flower = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=True)
    type_of_wrapper = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    number_of_flowers = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)