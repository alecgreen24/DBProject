import psycopg2
from group_project.settings import *


def connect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        
        conn = psycopg2.connect(
            host=DATABASES['default']['HOST'],
            database=DATABASES['default']['NAME'],
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD']
        )
        # Create a cursor
        cur = conn.cursor()
        
	    # Execute a statement
        print('PostgreSQL database version:')
        cur.execute(query)

        # Store the database tuples obtained from the query.
        tuples = cur.fetchone()
       
	    # Close the communication with the PostgreSQL
        cur.close()

        # Return the tuples
        return tuples
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
