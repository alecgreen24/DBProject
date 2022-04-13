from .connector import *
def createStudent(username, password):
    tuple = connect("INSERT INTO student VALUES (DEFAULT, '{}', '{}')".format(username, password))
    if tuple:
        print(f"*********** TUPLE *******\n{tuple}")