from .connector import *

class TestQuestionDAO():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def createTestQuestion(self, test_question):
        sql = f"""INSERT INTO test_question VALUES('{test_question.test_id}', '{test_question.question_id}')"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Commit the changes on the table.
            conn.commit()
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the status of the commit if the change was successful.
            return "success"

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()

    def deleteTestQuestion(self, test_question):
        sql = f"""DELETE FROM test_question WHERE username = '{test_question.test_id} AND {test_question.question_id}'"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Commit the changes on the table.
            conn.commit()
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the status of the commit if the change was successful.
            return "success"

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()

    def selectTestQuestions(self, test_question):
                sql = f"""SELECT q.id as question_id, 
                        q.content as question_content,  
                        qa.answer_id, 
                        answer.content as answer_content 
                        FROM question q
                        JOIN question_answer qa
                        ON q.id = qa.question_id
                        JOIN answer
                        ON qa.answer_id =  answer.id
                        WHERE q.id IN (SELECT question_id
                        FROM test_question
                        WHERE test_id = '{test_question.id}');"""
                conn = None
                try:
                    # Establishing the connection
                    conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
                    # Create a cursor
                    cur = conn.cursor()
                    # Execute a statement.
                    cur.execute(sql)
                    # Fetch the id of the test created.
                    id = cur.fetchall()
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

    def updateTestQuestion(self, test_question):
        
        sql = f"""UPDATE question SET content = '{test_question.content}, correct_answer_id = '{test_question.answer}"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
             # Fetch the id of the student created.
            id = cur.fetchone()
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the status of the commit if the change was successful.
            return id[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print("ERROR", error)
            return None
        finally:
            if conn is not None:
                conn.close()
