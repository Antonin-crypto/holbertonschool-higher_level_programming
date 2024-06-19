#!/usr/bin/env python3
"""Module listing all states from the database"""

import MySQLdb
import sys


def list_states(mysql_username, mysql_password, db_name):
    """
    Connect to the MySQL database and list all states ordered by their ID.

    Args:
        mysql_username (str): The username to connect to the MySQL database.
        mysql_password (str): The password to connect to the MySQL database.
        db_name (str): The name of the database to connect to.

    Returns:
        None
    """
    # Connect to the database
    conn = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=mysql_username,
          passwd=mysql_password,
          db=db_name,
          charset="utf8"
          )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the SQL query to select all states ordered by their ID
    cur.execute("""SELECT * FROM states ORDER BY id""")

    # Fetch all the rows returned by the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    # List states from the database
    list_states(mysql_username, mysql_password, db_name)
