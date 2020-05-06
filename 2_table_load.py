username = 'root'
password = 'Test123!'

from sqlalchemy import create_engine
connection_string = 'mysql://{0}:{1}@localhost/oscres_db'.format(username, password)
engine = create_engine(connection_string)
print(connection_string)
import pandas as pd
data_frame = pd.read_csv('Miscellaneous/university.csv')
# con expect type sqlalchemy.engine.Engine or sqlite3.Connection
try:
    data_frame.to_sql(con=engine, name='recommender_university_course', if_exists='replace')
except: 
    data_frame.to_sql(con=engine, name='Recommender_university_course', if_exists='replace')