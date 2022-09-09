from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Time , ForeignKey ,TEXT
from sqlalchemy import Sequence, select, and_

Base = declarative_base()

# https://docs.sqlalchemy.org/en/14/orm/tutorial.html

# saving columns' name of table to wrtie functions
cafe_columns = ('cafe_name', 'city', 'province',
                'phone_number', 'cost', 'work_start', 'work_end')
cafe_columns_address = ['cafe_id', 'cafe_address']
cafe_columns_features = ['cafe_id', 'hookah', 'internet', 'delivery',
                         'smoking', 'open_space', 'live_music', 'parking', 'pos']
cafe_columns_rating = ['cafe_id', 'food_quality',
                       'service_quality', 'cost', 'cost_value', 'environment']


class Cafe(Base):
    __tablename__ = 'cafe'

    cafe_id = Column(Integer, Sequence('cafe_id_seq'), primary_key=True)
    cafe_name = Column(String)
    city = Column(String)
    province = Column(String)
    phone_number = Column(String)
    cost = Column(Integer)
    work_start = Column(Time)
    work_end = Column(Time)

    def __repr__(self) -> str:
        return f"{self.cafe_name}"

class CafeAddress(Base):
    __tablename__ = 'cafe_address'
    cafe_id = Column(Integer,ForeignKey("cafe.cafe_id"),primary_key=True)
    cafe_address = Column(TEXT)

class CafeFeatures(Base):
    __tablename__ = 'cafe_features'
    cafe_id = Column(Integer,ForeignKey("cafe.cafe_id"),primary_key=True)
    hookah = Column(Integer)
    internet = Column(Integer)
    delivery = Column(Integer)
    smoking = Column(Integer)
    open_space = Column(Integer)
    live_music = Column(Integer)
    parking = Column(Integer)
    pos = Column(Integer)

class CafeRating(Base):
    __tablename__ = 'cafe_rating'
    cafe_id = Column(Integer,ForeignKey("cafe.cafe_id"),primary_key=True)
    food_quality = Column(Integer)
    service_quality = Column(Integer)
    cost = Column(Integer)
    cost_value = Column(Integer)
    environment = Column(Integer)

def set_table(tablename: str):
    tablename = tablename.title()
    match tablename:
        case "Cafe": return Cafe
        case "Cafe_Address": return CafeAddress
        case "Cafe_Features": return CafeFeatures
        case "Cafe_Rating": return CafeRating


class Database:

    def __init__(self, host, user, password, db) -> None:
        self.engine = create_engine(
            f'mysql+pymysql://{user}:{password}@{host}/{db}')
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()

    def read(self, tablename: str, filter=None, order=None, n=0):
        tablename = set_table(tablename)
        query = self.session.query(tablename)
        if filter is not None:
            query = query.filter(filter)
        if order is not None:
            query = query.order_by(order)
        if n > 0:
            query = query.limit(n)
        return query.statement, self.session.bind

    # insert function
    def insert(self, tablename: str(), data):
        tbname = tablename.lower()
        if tbname == 'cafe':
            tbcolumns = cafe_columns
        elif tbname == 'cafe_address':
            tbcolumns = cafe_columns_address
        elif tbname == 'cafe_rating':
            tbcolumns = cafe_columns_rating
        else:
            tbcolumns = cafe_columns_features
        sql = f"INSERT INTO {tbname} " + \
            '(' + ','.join(tbcolumns) + ')' + f" VALUES {data};"
        try:
            self.engine.execute(sql)
        except Exception as e:
            return e

    # delete function
    def delete(self, tablename: str(), id):
        tbname = tablename.lower()
        sql = f"DELETE FROM {tbname} WHERE cafe_id = {id}"
        try:
            self.engine.execute(sql)
        except Exception as e:
            return e

    # update functions
    # for cafe table
    def update_Cafe(self, id, data):
        sql = 'UPDATE cafe SET cafe_name = \'{}\', city = \'{}\' , province = \'{}\' ,phone_number = \'{}\' , cost = {} , work_start = {}, work_end = {}' + f' WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

    # for cafe_address table
    def update_Cafe_address(self, id, data):
        sql = 'UPDATE cafe_address SET cafe_address = \'{}\' ' + f'WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

    # for cafe_rating table
    def update_Cafe_rating(self, id, data):
        sql = 'UPDATE cafe_rating SET food_quality = {},service_quality = {},cost = {},cost_value = {},environment = {} ' + f'WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

    # for cafe_features table
    def update_Cafe_features(self, id, data):
        sql = 'UPDATE cafe SET hookah = {},internet = {},delivery = {},smoking = {},open_space = {},live_music = {},parking = {},pos = {}' + f' WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

    # truncate function
    def truncate(self, tablename: str()):
        tbname = tablename.lower()
        sql1, sql2, sql3 = ['SET FOREIGN_KEY_CHECKS = 0;',
                            f'truncate table {tbname};', 'SET FOREIGN_KEY_CHECKS = 1;']
        try:
            self.engine.execute(sql1)
            self.engine.execute(sql2)
            self.engine.execute(sql3)
        except Exception as e:
            return e

        return True
