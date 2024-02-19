#!/usr/bin/python3
"""This script lists all cities of that state, using database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    base = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    iterator = base.cursor()
    match = sys.argv[4]
    iterator.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = iterator.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    iterator.close()
    base.close()
