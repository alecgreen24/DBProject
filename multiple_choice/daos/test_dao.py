from .connector import *
import numpy as np
from .test import Test
from .question import Question
from .answer import Answer

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
                test = Test(id = row[0], creator_id = row[1], title = row[2], created_at = row[3])
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


    def getOneTest(self, test_id):
        sql = f"""SELECT * FROM test WHERE id = '{test_id}' AND active = 'true'"""
        conn = None
        try:
            # Establishing the connection
            conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            # Create a cursor
            cur = conn.cursor()
            # Execute a statement.
            cur.execute(sql)
            # Fetch the id of the test created.
            row = np.array(cur.fetchone())
            # Create a test instance from the data. 
            test = Test(id = row[0], creator_id = row[1], title = row[2], created_at = row[3])
            # Close the communication with the PostgreSQL
            cur.close()
            # Returns the instances of Test.
            return test

    

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            if conn is not None:
                conn.close()

    def getQuestions(self, test):
        sql = f"""SELECT 
            q.id as question_id, 
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
            WHERE test_id = '{test.id}')"""
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
            # Create a test instance from the data. 
            questions = []

            current_q = Question(content = rows[0][1])
            current_q.id = rows[0][0]
            for row in rows:
                if current_q.id == row[0]:
                    answer = Answer(content = row[3])
                    answer.id = row[2]
                    current_q.answers.append(answer)
                else:
                    questions.append(current_q)
                    current_q = Question(content = row[1])
                    answer = Answer(content = row[3])
                    answer.id = row[2]
                    current_q.answers.append(answer)
                    current_q.id = row[0]
            questions.append(current_q)
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


    def getQuestionsAndCorrectAnswer(self, test):
        sql = f"""SELECT question.id, question.content, answer.id, answer.content as correct_answer
FROM answer JOIN question
ON answer.id = question.correct_answer_id
JOIN test_question 
ON test_question.question_id = question.id
WHERE test_question.test_id = {test.id}"""
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
            # Create a test instance from the data. 
            questions = []

            for row in rows:
                answer = Answer(content = row[3])
                answer.id = row[2]
                question = Question(content = row[1], correct_answer = answer)
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

    
