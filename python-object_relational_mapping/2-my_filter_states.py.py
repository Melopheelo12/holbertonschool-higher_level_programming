#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # créer un curseur
    cur = db.cursor()

    # requête SQL avec format (demandé par l'exercice)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cur.execute(query)

    # afficher les résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # fermer connexion
    cur.close()
    db.close()
