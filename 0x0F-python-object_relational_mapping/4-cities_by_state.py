#!/usr/bin/python3
'''
lists all cities from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id ASC")
    for i in cursor.fetchall():
        print(i)
