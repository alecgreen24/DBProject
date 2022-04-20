-- Get the question content and correct answer content
SELECT question.content, answer.content FROM
question, question_answer, answer
WHERE question.correct_answer_id = answer.id
AND question.id = question_answer.question_id
AND answer.id = question_answer.answer_id 
