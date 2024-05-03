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

insert_data = """
    INSERT INTO phonebook2 (name, surname, phone)
    VALUES (%s, %s, %s);
"""

update_data = '''
    UPDATE phonebook2 SET {} = %s WHERE id = %s;
'''

method1 = input("Do you want to insert data or update? ")

if method1 == "insert":
    name = input("Please enter the name: ")
    surname = input("Please enter the surname: ")
    phone = input("Please enter the phone: ")
    cursor.execute(insert_data, (name, surname, phone))
elif method1 == "update":
    id = input('Enter the id: ')
    column = input('Enter the column: ')
    update_query = update_data.format(column)
    change_data = input('Enter the new element: ')
    cursor.execute(update_query, (change_data, id))
else:
    print('Invalid input')

all_table = '''
    SELECT * FROM phonebook2 
    ORDER BY id ASC
'''
cursor.execute(all_table)
data = [row for row in cursor.fetchall()]
dataframe = pd.DataFrame(data, columns=['id', 'name', 'surname', 'phone'])
dataframe = dataframe.set_index('id')
connection.commit()

cursor.close()

connection.close()
dataframe.head(25)   