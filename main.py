import psycopg2
import json

# Establish connection to PostgreSQL
connection = psycopg2.connect(
    database="testDB",
    user="postgres",
    password="August082303!",
    host="localhost",
    port=5432
)

cursor = connection.cursor()


create_table = '''CREATE TABLE IF NOT EXISTS employee (
        id    int PRIMARY KEY, 
        name   varchar(40) NOT NULL,
        salary  int  )'''
cursor.execute(create_table)

insert_table = 'INSERT INTO employee(id, name, salary, tag_json) VALUES (%s, %s, %s, %s)'

with open('testData.json', 'r') as f:
    json_data = json.load(f)

print(json.dumps(json_data))
insert_values = (4, 'Matt', 120000, json.dumps(json_data))

cursor.execute(insert_table, insert_values)
#cursor.execute('INSERT INTO employee(id, name, salary, tag_json) VALUES(?,?,?,?)', 3, 'Matt', 120000, json.dumps(json_data))

connection.commit()

cursor.close()
connection.close()

