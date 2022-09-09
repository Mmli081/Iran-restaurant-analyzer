import json
from operator import and_
from CRUD import Database, set_table, and_
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


def time_format(time):
    return f"{int(time):02}:00" if ":" not in time else time

def prep_features(features):
    db_feat = ['قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان']
    return tuple(1 if f in features else 0 for f in db_feat)

def insert_cafe(result):
    att_cafe = ["name","city","province",'phone',"price_class","work_start","work_end"]
    for row in result:
        data = []
        for att in att_cafe:
            if att in ('work_start','work_end'):
                data.append(time_format(row[att]))
            else: data.append(row[att])
        data = tuple(data)
        db.insert('cafe',data)

def insert_cafe_address(result):
    for i,row in enumerate(result):
        ad = row['address']
        data = f'({i+1},\" {ad} \")'
        db.insert('cafe_address',data)

def insert_cafe_rating(result):
    att_rating = ["food_quality","service","price_class","cost_value","environment"]
    for i,row in enumerate(result):
        data = [i+1]
        for att in att_rating:
            data.append(row[att])
        data = tuple(data)
        db.insert('cafe_rating',data)
        
def insert_cafe_features(result):
    for i,row in enumerate(result):
        data = [i+1]
        for f in prep_features(row['feature_list']):
            data.append(f)
        data = tuple(data)
        db.insert('cafe_features',data)

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