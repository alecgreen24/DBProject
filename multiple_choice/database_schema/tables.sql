DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS taken;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS test_questeion;
DROP TABLE IF EXISTS answer;
DROP TABLE IF EXISTS question_answer;

CREATE TABLE student(
	id SERIAL,
	username varchar(255) UNIQUE NOT NULL,
	password varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE test(
    id SERIAL,
    creator_id INTEGER REFERENCES student(id),
    title varchar(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    active BOOLEAN NOT NULL,
    updated_at TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE taken(
    test_id  INTEGER REFERENCES test,
    student_id INTEGER REFERENCES student,
    score VARCHAR(20) NOT NULL,
    taken_at TIMESTAMP NOT NULL,
    PRIMARY KEY (test_id, student_id)
);


CREATE TABLE question(
    id SERIAL,
    content VARCHAR(255) NOT NULL,
    correct_answer_id INTEGER REFERENCES answer(id),
    PRIMARY KEY (id)
);


CREATE TABLE test_question (
    test_id INTEGER REFERENCES test(id),
    question_id INTEGER REFERENCES question(id),
    PRIMARY KEY (test_id, question_id)
);


CREATE TABLE answer (
    id SERIAL,
    content VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE question_answer (
    question_id INTEGER REFERENCES question(id),
    answer_id INTEGER REFERENCES answer(id),
    PRIMARY KEY (question_id, answer_id)
);

