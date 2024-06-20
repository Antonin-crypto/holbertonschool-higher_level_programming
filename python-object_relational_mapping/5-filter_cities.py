#!/usr/bin/python3
"""Module listing all cities of a state from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=argv[1],
          passwd=argv[2],
          db=argv[3]
          )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Create the SQL query to sele all citi of the given state orde by their ID
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the SQL query with parameterized input to prevent SQL injection
    cur.execute(query, (argv[4],))

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
