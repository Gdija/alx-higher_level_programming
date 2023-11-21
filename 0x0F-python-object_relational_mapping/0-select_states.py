#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":
    db=_mysql.connect(host='localhost',port=3306,username=sys.argv[1],password=sys.argv[2],database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in cursor.fetchall():
        print(i)

