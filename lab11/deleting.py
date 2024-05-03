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

delete_data = '''
    DELETE FROM phonebook2 WHERE {} = %s;
'''

method = input('Do you want to delete by name or phone? ')
if method == 'name':
    name = input('Enter the name: ')
    cursor.execute(delete_data.format(method), (name,))
if method == 'phone':
    phone = input('Enter the phone: ')
    cursor.execute(delete_data.format(method), (phone,))

connection.commit()
cursor.close()

connection.close()

print('Data deleted successfully.')

connection2 = sql.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='Adil$notlove',
    port='5432'
)
cursor2 = connection2.cursor()

all_table = '''
    SELECT * FROM phonebook2
    ORDER BY id ASC
'''
cursor2.execute(all_table)
data = [row for row in cursor2.fetchall()]

dataframe = pd.DataFrame(data, columns=['id', 'name', 'surname', 'phone'])
dataframe = dataframe.set_index('id')

cursor2.close()
connection2.close()
dataframe.head(100)