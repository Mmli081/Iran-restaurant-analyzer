from operator import and_
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Time , ForeignKey ,TEXT
from sqlalchemy import Sequence, select, and_

Base = declarative_base()

# https://docs.sqlalchemy.org/en/14/orm/tutorial.html

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

    def read(self, tablename: str, filter=None, order=None):
        tablename = set_table(tablename)
        query = self.session.query(tablename)
        if filter is not None:
            query = query.filter(filter)
        if order is not None:
            query = query.order_by(order)
        return query.statement, self.session.bind

    # insert function
    def insert(self,data):
        self.session.add_all(data)
        self.session.commit()

    # delete function
    def delete(self, tablename: str(), id):
        tbname = tablename.lower()
        sql = f"DELETE FROM {tbname} WHERE cafe_id = {id}"
        try:
            self.engine.execute(sql)
        except Exception as e:
            return e

    # update functions
    def update(self,tablename,id,data):
        tn = set_table(tablename)
        self.session.query(tn).where(tn.cafe_id==id).update(data, synchronize_session='fetch')
        self.db.session.commit()

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
