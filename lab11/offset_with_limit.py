import psycopg2 as sql
import pandas as pd

connection = sql.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='Adil$notlove',
    port='5432'
)

cursor = connection.cursor()
query_data = '''
    SELECT * FROM phonebook2
    OFFSET %s
    LIMIT %s
'''

offset_size = int(input("Size of the offset :"))
limit_size = int(input("Size of the limit :")) 

cursor.execute(query_data , (offset_size,limit_size)) 

data = [row for row in cursor.fetchall()]
dataframe = pd.DataFrame(data, columns=['id', 'name', 'surname', 'phone'])
dataframe = dataframe.set_index('id')
connection.commit()

cursor.close()

connection.close()
dataframe.head(100) 