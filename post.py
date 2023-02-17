
import sqlite3
from sqlite3 import Error
from flask import Flask, request

app = Flask(__name__)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return cursor   

@app.route('/', methods=['GET'])
def hello():
    conn = create_connection('test.sqlite')

    query = "CREATE TABLE nama (name TEXT PRIMARY KEY);"
    execute_query(conn, query)

    return 'DB successfully created!'

@app.route('/insert', methods=['POST'])
def insert():
    conn = create_connection('test.sqlite')
    body = request.json

    query = f'INSERT INTO nama VALUES ("{body["name"]}");'
    execute_query(conn, query)

    return 'DB inserted successfully!'

@app.route('/get', methods=['GET'])
def get():
    conn = create_connection('test.sqlite')

    query = 'SELECT * FROM nama;'
    cursor = execute_query(conn, query)

    res = cursor.fetchall()

    return res 

app.run(host='0.0.0.0', port=3000)