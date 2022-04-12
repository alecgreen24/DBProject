CREATE TABLE user(
	id MEDIUMINT NOT NULL AUTO_INCREMENT UNIQUE,
	username varchar(255) UNIQUE NOT NULL,
	password varchar(255) NOT NULL,
    PRIMARY KEY (id)
) 

CREATE TABLE test(
    id MEDIUMINT NOT NULL AUTO_INCREMENT UNIQUE,
    creator FOREIGN KEY (id) REFERENCES user(id),
    title varchar(255) NOT NULL,
    created_at DATETIME NOT NULL,
    active BOOLEAN NOT NULL,
    updated_at DATETIME,
    PRIMARY KEY (id)
)

CREATE TABLE taken(
    test_id FOREIGN KEY (id) REFERENCES test,
    user_id FOREIGN KEY (id) REFERENCES user,
    score VARCHAR(20) NOT NULL,
    taken_at DATETIME NOT NULL,
    PRIMARY KEY (test_id, user_id)
)


CREATE TABLE question(
    id MEDIUMINT NOT NULL AUTO_INCREMENT UNIQUE,
    content VARCHAR(255) NOT NULL,
    correct_answer_id MEDIUMINT REFERENCES answer(id),
    PRIMARY KEY (id)
)


CREATE TABLE test_question (
    test_id MEDIUMINT REFERENCES test(id),
    question_id REFERENCES question(id),
    PRIMARY KEY (test_id, question_id)
)


CREATE TABLE answer (
    id MEDIUMINT NOT NULL AUTO_INCREMENT UNIQUE,
    content VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
)


CREATE TABLE question_answer (
    question_id MEDIUMINT REFERENCES question(id),
    answer_id MEDIUMINT REFERENCES answer(id),
    PRIMARY KEY (question_id, answer_id)
)

