#!/usr/bin/python3
'''
avoid sql injection
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    [print(item) for item in cursor.fetchall() if item[1] == argv[4]]
