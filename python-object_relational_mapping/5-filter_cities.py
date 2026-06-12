#!/usr/bin/python3
"""
Lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to the DB the command line arguments"""
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    states_searched = sys.argv[4]

    cur = db.cursor()

    query = ("""SELECT cities.name
            FROM cities JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC""")

    cur.execute(query, (states_searched,))

    query_rows = cur.fetchall()

    print(", ".join([row[0] for row in query_rows]))

    cur.close()
    db.close()
