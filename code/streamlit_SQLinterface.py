from operator import and_
from crawl_SQLinterface import *
from datetime import datetime
from sqlalchemy import and_


#filters
def filter_by_city(city):
    return set_table('cafe').city == city

def filter_by_province(province):
    return set_table('cafe').province == province

def filter_by_has_features(features: list):
    f = read("cafe_features")
    #macth with features reutn set_table.features
    return set_table('cafe').cafe_id == f.cafe_id

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
