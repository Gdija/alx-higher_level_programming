#!/usr/bin/python3
'''
lists all cities in a state from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM cities \
            INNER JOIN states ON states.id = cities.state_id \
            ORDER BY cities.id")
    print(", ".join([i[2] for i in cursor.fetchall() if i[4] == argv[4]]))
