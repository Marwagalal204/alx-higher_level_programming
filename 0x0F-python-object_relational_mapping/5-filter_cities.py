#!/usr/bin/python3

""" script takes name of state and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor
    method = sys.argv[4]
    query = """SELECT name from cities INNER JOIN states ON
    cities.states.id = states.id WHERE states.id LIKE %s"""(method, )

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
