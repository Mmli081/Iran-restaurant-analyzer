from CRUD import Database
from crawl import scrape

result = scrape()
db = Database()


def time_format():
    pass

def prep_features():
    pass

def insert_cafe(result):
    att_cafe = ["name","city","province",'phone',"price_class","work_start","work_end"]
    for row in result:
        data = []
        for att in att_cafe:
            data.append(row[att])
        data = tuple(data)
        db.insert('cafe',data)

def insert_cafe_address(result):
    for row in result:
        db.insert('cafe_address',(row['address'],))

# def insert_cafe_rating():
#     att_rating = ["price_class","food_quality","service","cost_value","environment"]
#     for row in result:
