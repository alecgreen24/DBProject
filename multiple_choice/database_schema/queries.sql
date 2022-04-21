-- Get the questions and thier answers for one test.
SELECT question.id , question.content, answer.id, answer.content
FROM test
JOIN test_question ON test.id = test_question.test_id
JOIN question ON test_question.question_id = question.id
JOIN question_answer ON question.id = question_answer.question_id
JOIN answer ON question_answer.answer_id = answer.id
WHERE test.id = 70
ORDER BY question.id


-- Select the question and their correct answers based on the test.id
SELECT question.id, question.content, answer.id, answer.content
FROM answer JOIN question
ON answer.id = question.correct_answer_id
JOIN test_question 
ON test_question.question_id = question.id
WHERE test_question.test_id = 70