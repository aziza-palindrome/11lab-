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

names = []
surnames = []
phones = []
temp = ""
method = 'name'
all_data = input('Enter data in the order of name->surname->phone->name.. :')
all_data += " "
for index , item in enumerate(all_data):
    if item == " ":
        if method == 'name' : 
            names.append(temp)
            method = 'surname'
            temp = ""
        elif method == 'surname' :
            surnames.append(temp)
            method = 'phone'
            temp = ""
        elif method == 'phone' :
            phones.append(temp)
            method = 'name'
            temp = ""

    else: temp+=item
if len(names) == len(surnames) == len(phones) : 
    print("All done !")   
if len(names) > len(surnames) : 
    print(f'name - {names[len(names)-1]} didnot inserted') 
if len(names) == len(surnames) and len(surnames) > len(phones) : 
    print(f'name - {names[len(names)-1]} and surname - {surnames[len(surnames)-1]} didnot inserted') 


for index in range(len(phones)):
    cursor.execute(insert_data, (names[index], surnames[index], phones[index])) 

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
dataframe.head(100)
#Arya Stark 657-2343 Tirion Lannister 837-9566 Renli Baratheon 373-9542 Taywin Lannister 342-9432 Daeneris Targarien 234-4621