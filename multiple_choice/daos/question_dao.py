from .connector import *
import numpy as np
from .question import Question
from .question_answer import QuestionAnswer
from .test_question import TestQuestion




class QuestionDAO():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def createQuestion(self, question):
        sql = f"""INSERT INTO question VALUES(default, '{question.content}', '{question.correct_answer_id}') RETURNING id;"""
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

    def deleteQuestion(self, question):
        sql = f"""DELETE FROM question_answer WHERE question_id = '{question.id}';
                  DELETE FROM test_question WHERE question_id = '{question.id}';
                  DELETE FROM question WHERE id = '{question.id}';"""
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
            
            print(question.id)
            # Returns the status of the commit if the change was successful.
            return "success"

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()


    # def deleteQuestionFromID(self, id):
    #         sql = f"""DELETE FROM question WHERE id = '{id}'"""
    #         conn = None
    #         try:
    #             # Establishing the connection
    #             conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
    #             # Create a cursor
    #             cur = conn.cursor()
    #             # Execute a statement.
    #             cur.execute(sql)
    #             # Commit the changes on the table.
    #             conn.commit()
    #             # Close the communication with the PostgreSQL
    #             cur.close()
    #             # Returns the status of the commit if the change was successful.
    #             return "success"

    #         except (Exception, psycopg2.DatabaseError) as error:
    #             print(error)
    #             return error
    #         finally:
    #             if conn is not None:
    #                 conn.close()

    # def updateQuestion(self, question):
    
    #     sql = f"""UPDATE question SET content = '{question.content}, correct_answer_id = '{question.id}"""
    #     conn = None
    #     try:
    #         # Establishing the connection
    #         conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
    #         # Create a cursor
    #         cur = conn.cursor()
    #         # Execute a statement.
    #         cur.execute(sql)
    #             # Fetch the id of the student created.
    #         id = cur.fetchone()
    #         # Close the communication with the PostgreSQL
    #         cur.close()
    #         # Returns the status of the commit if the change was successful.
    #         return id[0]

    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print("ERROR", error)
    #         return None
    #     finally:
    #         if conn is not None:
    #             conn.close()
                
    def getAllQuestions(self):
        sql = "SELECT * FROM question"
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Commit the changes on the table.
            rows = np.array(cur.fetchall())

            # Returns the status of the commit if the change was successful.
            questions = []
            for row in rows:
                question = Question(content = row[1], correct_answer_id = row[2])
                question.id = row[0]
                questions.append(question)
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the instances of Test.
            return questions

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()
