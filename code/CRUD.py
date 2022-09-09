from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

# https://docs.sqlalchemy.org/en/14/orm/tutorial.html

# connecting to data base
class Database:
    def __init__(self, host, user, password, db):
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
        # saving columns' name of table to wrtie functions
        self.cafe_columns = ('cafe_name','city','province','phone_number','cost','work_start','work_end')
        self.cafe_columns_address = ['cafe_id','cafe_address']
        self.cafe_columns_features = ['cafe_id','hookah','internet','delivery','smoking','open_space','live_music','parking','pos']
        self.cafe_columns_rating = ['cafe_id','food_quality','service_quality','cost','cost_value','environment']

# use engine interact with data base
# CRUD operations are written for all tables include read,insert,delete,truncate
# But each table has a specific update function
# read will give you a dataframe output of a specific in database
    def read(self,tablename):
        tbname = tablename.lower()
        tbcolumns = ['cafe_id']
        if tbname == 'cafe':
            for i in self.cafe_columns:
                tbcolumns.append(i)
        elif tbname == 'cafe_address':
            tbcolumns = self.cafe_columns_address
                
        elif tbname == 'cafe_rating':
            tbcolumns = self.cafe_columns_rating
        else : tbcolumns = self.cafe_columns_features
        sql = f"SELECT * from {tbname}"
        try:
            return pd.DataFrame(self.engine.execute(sql),columns=tbcolumns)
        except Exception as e:
            return e     

# insert function 
    def insert(self,tablename : str() ,data):
        tbname = tablename.lower()
        if tbname == 'cafe':
            tbcolumns = self.cafe_columns
        elif tbname == 'cafe_address':
            tbcolumns = self.cafe_columns_address
        elif tbname == 'cafe_rating':
            tbcolumns = self.cafe_columns_rating
        else: tbcolumns=self.cafe_columns_features
        sql = f"INSERT INTO {tbname} " + '('+ ','.join(tbcolumns) + ')' + f" VALUES {data};"
        try:
            self.engine.execute(sql)
        except Exception as e:
            return e

# delete function
    def delete(self,tablename : str() ,id):
        tbname = tablename.lower()
        sql = f"DELETE FROM {tbname} WHERE cafe_id = {id}"
        try:
            self.engine.execute(sql)
        except Exception as e:
            return e
            
# update functions
# for cafe table
    def update_Cafe(self,id, data):
        sql = 'UPDATE cafe SET cafe_name = \'{}\', city = \'{}\' , province = \'{}\' ,phone_number = \'{}\' , cost = {} , work_start = {}, work_end = {}'+ f' WHERE cafe_id = {id}'       
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e
# for cafe_address table
    def update_Cafe_address(self,id, data):
        sql = 'UPDATE cafe_address SET cafe_address = \'{}\' ' + f'WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e
# for cafe_rating table
    def update_Cafe_rating(self,id, data):
        sql = 'UPDATE cafe_rating SET food_quality = {},service_quality = {},cost = {},cost_value = {},environment = {} ' + f'WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

# for cafe_features table  
    def update_Cafe_features(self,id, data):
        sql = 'UPDATE cafe SET hookah = {},internet = {},delivery = {},smoking = {},open_space = {},live_music = {},parking = {},pos = {}' + f' WHERE cafe_id = {id}'
        try:
            self.engine.execute(sql.format(*data))

        except Exception as e:
            return e

# truncate function
    def truncate(self,tablename : str()):
        tbname = tablename.lower()
        sql1,sql2,sql3 = ['SET FOREIGN_KEY_CHECKS = 0;',f'truncate table {tbname};','SET FOREIGN_KEY_CHECKS = 1;']
        try:
            self.engine.execute(sql1)
            self.engine.execute(sql2)
            self.engine.execute(sql3)
        except Exception as e:
            return e

        return True