#!/usr/bin/python3

""" script takes name of state and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    state_name = sys.argv[4]
    query = """SELECT cities.name from cities INNER JOIN states ON
    cities.state_id = states.id WHERE states.name LIKE %s"""

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    cur.close()
    db.close()
