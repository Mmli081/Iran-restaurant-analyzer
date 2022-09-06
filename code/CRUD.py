from sqlalchemy import create_engine
import pandas as pd
# connecting to data base
class Database:
    def __init__(self):
        global engine ,cafe,cafe_address,cafe_features,cafe_rating
        host = '127.0.0.1:3306'
        user  = 'sobhan'
        password = '$Gh9170392008'
        db='group4'
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
        # saving columns' name of table to wrtie functions
        cafe = ('cafe_name','city','province','phone_number','cost','work_start','work_end')
        cafe_address = ['cafe_address']
        cafe_features = ['hookah','internet','delivery','smoking','open_space','live_music','parking','pos']
        cafe_rating = ['food_quality','service_quality','cost','cost_value','environment']

# use engine interact with data base
# CRUD operations are written for all tables include read,insert,delete,truncate
# But each table has a specific update function
# read will give you a dataframe output of a specific in database
    def read(self,tablename):
        tbname = tablename.lower()
        tbcolumns = ['cafe_id']
        if tbname == 'cafe':
            for i in cafe:
                tbcolumns.append(i)
        elif tbname == 'cafe_address':
            for i in cafe_address:
                tbcolumns.append(i)
        elif tbname == 'cafe_rating':
            for i in cafe_rating:
                tbcolumns.append(i)
        else: 
            for i in cafe_features:
                tbcolumns.append(i)
        sql = f"SELECT * from {tbname}"
        try:
            return pd.DataFrame(engine.execute(sql),columns=tbcolumns)
        except Exception as e:
            return e         
# insert function 
    def insert(self,tablename : str() ,data):
        tbname = tablename.lower()
        if tbname == 'cafe':
            tbcolumns = cafe
        elif tbname == 'cafe_address':
            tbcolumns = cafe_address
        elif tbname == 'cafe_rating':
            tbcolumns = cafe_rating
        else: tbcolumns=cafe_features
        sql = f"INSERT INTO {tbname}" + '('+ ','.join(tbcolumns) + ')' + f"VALUES {data}"
        try:
            engine.execute(sql)
        except Exception as e:
            return e
# delete function
    def delete(self,tablename : str() ,id):
        tbname = tablename.lower()
        sql = f"DELETE FROM {tbname} WHERE cafe_id = {id}"
        try:
            engine.execute(sql)
        except Exception as e:
            return e
# update functions
# for cafe table
    def update_Cafe(self,id, data):
        sql = 'UPDATE cafe SET cafe_name = \'{}\', city = \'{}\' , province = \'{}\' ,phone_number = \'{}\' , cost = {} , work_start = {}, work_end = {}'+ f' WHERE cafe_id = {id}'       
        try:
            engine.execute(sql.format(*data))

        except Exception as e:
            return e
# for cafe_address table
    def update_Cafe_address(self,id, data):
        sql = 'UPDATE cafe_address SET cafe_address = \'{}\' ' + f'WHERE cafe_id = {id}'
        try:
            engine.execute(sql.format(*data))

        except Exception as e:
            return e
# for cafe_rating table
    def update_Cafe_rating(self,id, data):
        sql = 'UPDATE cafe_rating SET food_quality = {},service_quality = {},cost = {},cost_value = {},environment = {} ' + f'WHERE cafe_id = {id}'
        try:
            engine.execute(sql.format(*data))

        except Exception as e:
            return e
# for cafe_features table  
    def update_Cafe_features(self,id, data):
        sql = 'UPDATE cafe SET hookah = {},internet = {},delivery = {},smoking = {},open_space = {},live_music = {},parking = {},pos = {}' + f' WHERE cafe_id = {id}'
        try:
            engine.execute(sql.format(*data))

        except Exception as e:
            return e
# truncate function
    def truncate(self,tablename : str()):
        tbname = tablename.lower()
        sql1,sql2,sql3 = ['SET FOREIGN_KEY_CHECKS = 0;',f'truncate table {tbname};','SET FOREIGN_KEY_CHECKS = 1;']
        try:
            engine.execute(sql1)
            engine.execute(sql2)
            engine.execute(sql3)
        except Exception as e:
            return e

        return True