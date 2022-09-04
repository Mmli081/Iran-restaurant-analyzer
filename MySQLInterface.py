from sqlalchemy import create_engine
user  = 'user_group4'
password = 'OnhAeVtaxYca_group4'
host = '45.139.10.138:80'
db = 'group4'
engine  = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')
s = engine.execute('select 1+1')
print(s.first()[0])