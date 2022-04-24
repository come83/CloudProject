from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

def searchACompany(loc,service,staff):

    print(f"loc={loc}")
    query = "SELECT * FROM tuche WHERE "

    if loc != "None" :
        query += f'agencies LIKE "%{loc}%" AND'

    if service != "None":
        query += f' service_focus LIKE "%{service}%" AND'

    if staff != "None":
        query += f' staff LIKE "%{staff}%" AND'

    if query[(len(query)-3):] == 'AND':

        query=query[:(len(query)-3)]

    query += ";"

    return query


def exec_query(command, where):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'cse'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT name,website FROM tuche')
    results = [{name: website} for (name, website) in cursor]
    cursor.close()
    connection.close()

    return results



@app.route('/')
def index() -> str:
    return json.dumps({'tuche': test_table()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
