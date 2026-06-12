#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the DB the command line arguments"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    state_to_find = sys.argv[4]

    cur = db.cursor()

    query = ("""SELECT * FROM states
                WHERE states.name = %s
                ORDER BY states.id ASC;""")
    cur.execute(query, (state_to_find,))

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
