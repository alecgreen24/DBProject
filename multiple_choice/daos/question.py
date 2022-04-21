import json
class Question():
    def __init__(self, content, correct_answer_id = None):
        self.id = None
        self.content = content
        self.correct_answer_id = correct_answer_id
        self.answers = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)