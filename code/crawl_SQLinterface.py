import json
from operator import and_
from CRUD import Cafe, CafeAddress, CafeFeatures, CafeRating,Database, set_table, and_
from crawl import scrape
import pandas as pd
from datetime import datetime

# result = json.load(scrape())
# db = Database('127.0.0.1:3306','sobhan','$Gh9170392008','group4')

# test
import json
with open("../data/crawlSample.json") as f:
    result = json.load(f)
db = Database('localhost','mml','$Mml09357528086','group4Local')

# define some function to help inserting
def time_format(time):
    return f"{int(time):02}:00" if ":" not in time else time
def prep_features(features):
    db_feat = ['قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان']
    return tuple(1 if f in features else 0 for f in db_feat)
def last_id(tablename):
        tablename = set_table(tablename)
        if db.session.query(tablename.cafe_id).count()>0:
                return db.session.query(tablename).order_by(tablename.cafe_id.desc()).first().cafe_id
        else: return 0
# defining insert for each table
def insert_cafe(result):
    obj_list = []
    for record in result:
        data= {"cafe_name":record['name'],"city":record['city'],
        "province":record['province'],'phone_number':record['phone'],
        "cost":record['price_class'],"work_start":record['work_start'],"work_end":record['work_end']}
        obj_list.append(Cafe(**data))
    db.insert(obj_list)

def insert_cafe_address(result):
    obj_list = []
    # Loop through each object in the list
    LastID = last_id('cafe_address')+1
    for record in result:
        data = {'cafe_id': LastID ,'cafe_address':record['address']}
        obj_list.append(CafeAddress(**data))
        LastID+=1
    db.insert(data=obj_list)

def insert_cafe_rating(result):
    obj_list = []
    LastID = last_id('cafe_rating')+1
    for record in result:
        data = {'cafe_id':LastID,'food_quality':record["food_quality"],'service_quality':record["service"],
        'cost':record["price_class"],'cost_value':record["cost_value"],
        'environment': record["environment"]}
        obj_list.append(CafeRating(**data))
        LastID+=1
    db.insert(obj_list)

def insert_cafe_features(result):
    obj_list = []
    LastID = last_id('cafe_features')+1
    cafe_columns_features = ['cafe_id', 'hookah', 'internet', 'delivery',
                         'smoking', 'open_space', 'live_music', 'parking', 'pos']
    for record in result:
        data = dict(zip(cafe_columns_features,prep_features(record['feature_list'])))
        data['cafe_id']=LastID
        obj_list.append(CafeFeatures(**data))
        LastID+=1
    db.insert(obj_list)

#filters
def filter_by_city(city):
    return set_table('cafe').city == city

def filter_by_province(province):
    return set_table('cafe').province == province

# def filter_by_has_features(features: list):

def filter_by_range_work_time(work_start: str, work_end="00:00"):
    work_start = datetime.strptime(work_start, '%H:%M').time()
    if work_end == "00:00":
        return set_table("cafe").work_start >= work_start
    work_end = datetime.strptime(work_end, '%H:%M').time()
    return and_(set_table("cafe").work_start >= work_start,
                set_table("cafe").work_end <= work_end)

def filter_by_range_cost(_from: int=0, _to: int=5):
    return and_(set_table('cafe').cost >= _from,
                set_table('cafe').cost <= _to,)


def read(tablename, filter=None, order=None, n=0):
    return pd.read_sql(*db.read(tablename, filter, order, n))


if __name__ == "__main__":
    insert_cafe(result)
    insert_cafe_address(result)
    insert_cafe_features(result)
    insert_cafe_rating(result)