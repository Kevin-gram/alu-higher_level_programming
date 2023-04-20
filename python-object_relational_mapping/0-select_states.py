#!/usr/bin/python3


'''
a script that lists all states
from My database
'''
import MySQLdb
from sys import argv

if __Name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    db = cursor.fetchall()
    for x in db:
        print(x)
