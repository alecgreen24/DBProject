-- Get the questions and thier answers for one test.
SELECT 
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
WHERE test_id = 62)