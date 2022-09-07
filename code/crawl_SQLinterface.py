import json
from CRUD import Database
from crawl import scrape

result = json.load(scrape())
db = Database()


def time_format(time):
    return f"{int(time):02}:00" if ":" not in time else time

def prep_features(features):
    db_feat = ['قلیان','اینترنت رایگان','ارسال رایگان (Delivery)','سیگار','فضای باز','موسیقی زنده','پارکینگ', 'دستگاه کارت خوان']
    return tuple(1 if f in features else 0 for f in db_feat)

def insert_cafe():
    att_cafe = ["name","city","province","price_class","work_start","work_end"]
    for row in result:
        data = []
        for att in att_cafe:
            data.append(row[att])
        data = tuple(data)
        db.insert('cafe',data)

def insert_cafe_address():
    for row in result:
        db.insert('cafe_address',(row['address'],))


