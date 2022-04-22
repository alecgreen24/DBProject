import json
class Question():
    def __init__(self, content, correct_answer_id = None, correct_answer = None):
        self.id = None
        self.content = content
        self.correct_answer_id = correct_answer_id
        self.correct_answer = correct_answer
        self.answers = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)