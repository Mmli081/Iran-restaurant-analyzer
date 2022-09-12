from operator import and_
from crawl_SQLinterface import *
from datetime import datetime
from sqlalchemy import and_
import matplotlib.pyplot as plt
import seaborn as sns
from Home_Page import *
import numpy as np

#filters
def filter_by_city(city):
    return set_table('cafe').city == city

def filter_by_province(province):
    return set_table('cafe').province.like(f"%{province}%")

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
    _cafe = read_to_df(cafe)
    return _cafe[_cafe.cafe_id.isin(f.cafe_id)]

def filter_by_range_work_time(work_start: str, work_end="00:00"):
    work_start = datetime.strptime(work_start, '%H:%M').time()
    if work_end == "00:00":
        return set_table("cafe").work_start >= work_start
    work_end = datetime.strptime(work_end, '%H:%M').time()
    return and_(set_table("cafe").work_start >= work_start,
                set_table("cafe").work_end <= work_end)

def filter_by_range_cost(c_value):
    if c_value > 0:
        return set_table('cafe').cost == c_value
    return None

def read_to_df(tablename, filter=None, order=None, n=0):
    return pd.read_sql(db.read(tablename, filter, order, n).statement, db.session.bind)


def bar_plot_rate(column):
    if column == 'All':
        value =read_to_df(cafe_rating).iloc[:,1:7].mean(axis=1).value_counts().sort_index()
    else:
        value = read_to_df(cafe_rating)[column].value_counts().sort_index()
    return value

def bar_plot_rate_by_city(column,cities):
    df = read_to_df(cafe)
    ids = df[df.city.isin(cities)].cafe_id
    if column == 'All':
        value =read_to_df(cafe_rating)
        value = value[value.cafe_id.isin(ids)]
        value = value.iloc[:,1:7].mean(axis=1).value_counts().sort_index()
    else:
        value =read_to_df(cafe_rating)
        value = value[value.cafe_id.isin(ids)]
        value = value[column].value_counts().sort_index()
    return value


def bar_plot_rate_by_features(column,Features):
    df = has_features(Features)
    ids = df.cafe_id
    if column == 'All':
        value =read_to_df(cafe_rating)
        value = value[value.cafe_id.isin(ids)]
        value = value.iloc[:,1:7].mean(axis=1).value_counts().sort_index()
    else:
        value =read_to_df(cafe_rating)
        value = value[value.cafe_id.isin(ids)]
        value = value[column].value_counts().sort_index()
    return value

def get_mohalat():
    with open(f'data/mohalat.txt',encoding='utf-8') as f:
        l=f.read().split('\n')
    return l

def isopen(time):
    return and_(set_table("cafe").work_start >= time,
                set_table("cafe").work_end <= time)

def most_features():
    cafe_df = read_to_df(cafe)
    df = read_to_df(cafe_features)
    df["sum_feat"] = df.iloc[:, 1:].sum(axis=1)
    _max = df["sum_feat"].max()
    res = cafe_df[df.sum_feat == _max].iloc[:, :4]
    res["sum_features"] = df[df.sum_feat == _max]["sum_feat"]
    return res.reset_index(drop=True)

def highest_rate():
    cafe_df = read_to_df(cafe)
    rate_df = read_to_df(cafe_rating)
    rate_df["mean_rate"] = rate_df.iloc[:, 1:].mean(axis=1)
    _max = rate_df["mean_rate"].max()
    res = cafe_df[rate_df["mean_rate"] == _max].iloc[:, :4]
    res["mean_rates"] = rate_df[rate_df["mean_rate"] == _max]["mean_rate"]
    return res.sample(10).reset_index(drop=True)

def work_start_p():
    cafe_df = read_to_df(cafe)
    s = cafe_df.groupby("work_start").agg('count')['cafe_id']
    s.index = s.index.astype("str")
    return np.round(s.sort_values(ascending=False)[:5] / s.sum() * 100, 1),\
         s.sort_values(ascending=False)

def work_end_p():
    cafe_df = read_to_df(cafe)
    s = cafe_df.groupby("work_end").agg('count')['cafe_id']
    s.index = s.index.astype("str")
    return np.round(s.sort_values(ascending=False)[:5] / s.sum() * 100, 1),\
         s.sort_values(ascending=False)