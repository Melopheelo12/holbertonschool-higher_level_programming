#!/usr/bin/python3
"""Lists all states matching a user input from the database."""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cursor = db.cursor()

    # Query using format (as required)
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(searched_state)

    # Execute query
    cursor.execute(query)

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close resources
    cursor.close()
    db.close()
