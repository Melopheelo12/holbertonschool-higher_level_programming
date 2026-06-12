#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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

    query = ("""SELECT id, name FROM states
                WHERE states.name LIKE BINARY '{}'
                ORDER BY states.id ASC;""").format(state_to_find)
    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
