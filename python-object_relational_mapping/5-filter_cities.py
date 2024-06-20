#!/usr/bin/python3
"""Module listing all cities of a state from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         port=argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query with parameterized input to prevent SQL injection
    cur.execute("""SELECT name
                FROM cities
                 WHERE cities.state_id = (SELECT id
                    FROM states
                    WHERE name = %(state)s)
                ORDER BY cities.id ASC""", {"state": argv[4]})

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    city_names = ', '.join([row[0] for row in query_rows])
    print(city_names)
    # Close the cursor and connection
    cur.close()
    db.close()
