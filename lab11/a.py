import psycopg2 as sql
import pandas as pd 
import csv 

connection = sql.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Adil$notlove',
                  port = '5432' 
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE phonebook2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
);
""") 

print("Hurray! Table is created")

connection.commit()

cursor.close()

connection.close