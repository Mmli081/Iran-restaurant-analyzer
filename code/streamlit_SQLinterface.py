from operator import and_
from crawl_SQLinterface import *
from datetime import datetime
from sqlalchemy import and_


#filters
def filter_by_city(city):
    return set_table('cafe').city == city

def filter_by_province(province):
    return set_table('cafe').province == province

def match_feature(feature):
    ind = db_feat.index(feature)
    match ind:
        case 0: return CafeFeatures.hookah
        case 1: return CafeFeatures.internet
        case 2: return CafeFeatures.delivery
        case 3: return CafeFeatures.smoking
        case 4: return CafeFeatures.open_space
        case 5: return CafeFeatures.live_music
        case 6: return CafeFeatures.parking
        case 7: return CafeFeatures.pos

def has_features(features: list):
    f = db.session.query(CafeFeatures)
    for i in features:
        feature = match_feature(i)
        f = f.filter(feature == 1)
    f = pd.read_sql(f.statement, db.session.bind)
    cafe = read("cafe")
    return cafe[cafe.cafe_id.isin(f.cafe_id)]

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
