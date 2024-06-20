#!/usr/bin/python3
"""Module listing all cities of a state from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect("localhost",argv[1],argv[2], argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()


    # Execute the SQL query with parameterized input to prevent SQL injection
    cur.execute("""SELECT name
                FROM cities
                 WHERE cities.state_id = (SELECT id
                    FROM states
                    WHERE name = %(state)s)
                ORDER BY cities.id ASC""",
        {"state": argv[4]})

    # Fetch all the rows returned by the query
    query_rows = list(cur.fetchall())

    # Print each row
    for row in range(len(query_rows)):
        print(row)
        query_rows[row] = str(query_rows[row][0])
        print(', '.join(query_rows))
    # Close the cursor and connection
    cur.close()
    db.close()
