import psycopg2 as sql
import pandas as pd
import csv

connection = sql.connect(host='localhost',
                         dbname='postgres',
                         user='postgres',
                         password='Adil$notlove',
                         port='5432')

cursor = connection.cursor()

insert_data = """
    INSERT INTO phonebook2 (name, surname, phone)
    VALUES (%s, %s, %s);"""
all_table = '''
    SELECT id, name, surname, phone FROM phonebook2'''
base_query = '''
    SELECT * FROM phonebook2
    WHERE '''

def File():
    with open(r'C:\Users\user\Downloads\data.csv', "r") as file:
        data = csv.reader(file, delimiter=',')
        for row in data:
            name, surname, phone = row
            cursor.execute(insert_data, (name, surname, phone))

method = input("Do you want to work with data Y/n?")

if method == "Y":
    File()
    method3 = input('By what kind of pattern do you whant to query [name/surname/phone]?')

    if method3 == 'name':
        base_query += '''name '''
        string = input("Enter string")
        method4 = int(input('''
        1-name is equal to ...
        2-name starts with the ...
        3-name ends with the ...
        4-name contains the ...
        '''))
        if method4 == 1: base_query += f"='{string}'"
        elif method4 == 2: base_query += f" iLIKE '{string}%'"
        elif method4 == 3: base_query += f" iLIKE '%{string}'"
        elif method4 == 4: base_query += f" iLIKE '%{string}%'"
        else: print("Something went wrong")

    elif method3 == 'surname':
        base_query += '''surname '''
        string = input("Enter string")
        method4 = int(input('''
        1-surname is equal to ...
        2-surname starts with the ...
        3-surname ends with the ...
        4-surname contains the ...
        '''))
        if method4 == 1: base_query += f"='{string}'"
        elif method4 == 2: base_query += f" iLIKE '{string}%'"
        elif method4 == 3: base_query += f" iLIKE '%{string}'"
        elif method4 == 4: base_query += f" iLIKE '%{string}%'"
        else: print("Something went wrong")

    elif method3 == 'phone':
        base_query += '''phone '''
        integ = input("Enter the pattern phone")
        method4 = int(input('''
        1-phone is equal to ...
        2-phone starts with the ...
        3-phone ends with the ...
        4-phone contains the ...
        '''))
        if method4 == 1: base_query += f"='{integ}'"
        elif method4 == 2: base_query += f" iLIKE '{integ}%'"
        elif method4 == 3: base_query += f" iLIKE '%{integ}'"
        elif method4 == 4: base_query += f" iLIKE '%{integ}%'"
        else: print("Something went wrong")

    cursor.execute(base_query)
    data = [row for row in cursor.fetchall()]
    dataframe = pd.DataFrame(data, columns=['id', 'Name', 'Surname', 'Phone'])

    print(dataframe)

else:
    print("Ok . Goodluck!")

connection.commit()

cursor.close()

connection.close()

