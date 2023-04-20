#!/usr/bin/python3


'''
 the previous task? Did you test "Arizona'; TRUNCATE 
 TABLE states ; SELECT * FROM states WHERE name = '" as an input?
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        (argv[4],)
        )
    db = cursor.fetchall()
    for x in db:
        print(x)
