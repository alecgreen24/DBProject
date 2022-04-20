from .connector import *
import numpy as np
from .test import Test

class TestDAO():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def createTest(self, test):
        sql = f"""INSERT INTO test VALUES (DEFAULT, '{test.creator_id}', '{test.title}', NOW(), TRUE, NULL) RETURNING id;"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Fetch the id of the test created.
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


    def getAllTests(self):
        sql = f"""SELECT * FROM test WHERE active = 'true'"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Fetch the id of the test created.
            rows = np.array(cur.fetchall())
            # Create the test objects in order to return the data in a more structured way
            test_objs = []
            for row in rows:
                test = Test(row[1], row[2], row[3])
                test_objs.append(test)
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the instances of Test.
            return test_objs

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()


    def getTestTitle(self, test_id):
        sql = f"""SELECT test.title FROM test WHERE test.id  = '{test_id}'"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Fetch the id of the test created.
            test_id = cur.fetchone()
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the status of the commit if the change was successful.
            return test_id[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()
