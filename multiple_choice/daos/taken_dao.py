import psycopg2
from group_project.settings import *


class TakenDAO():
    def __init__(self, host, database, test_id, student_id):
        self.host = host
        self.database = database
        self.test_id = test_id
        self.student_id = student_id

    def createTaken(self, taken):
        sql = f"""INSERT INTO taken VALUES(DEFAULT,'{taken.test_id}', '{taken.student_id}')  RETURNING id;"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Fetch the id of the question created.
            id = cur.fetchone()
            # Commit the changes on the table.
            conn.commit()
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the status of the commit if the change was successful.
            return id[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()