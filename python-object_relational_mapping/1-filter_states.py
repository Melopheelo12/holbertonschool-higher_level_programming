#!/usr/bin/python3
"""
Lists all states with a name starting
with N from the database hbtn_0e_0_usa
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
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("""SELECT id, name
                FROM states WHERE BINARY states.name LIKE 'N%'
                ORDER BY states.id ASC;""")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    db.close()
