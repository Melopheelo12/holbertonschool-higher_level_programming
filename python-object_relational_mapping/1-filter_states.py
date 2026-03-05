#!/usr/bin/python3
"""Lists all states with a name starting with N from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # Fetch all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        # row[1] is the name column
        if row[1].startswith("N"):
            print(row)

    cur.close()
    db.close()
