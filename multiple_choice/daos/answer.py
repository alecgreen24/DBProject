
import json

class Answer():
    def __init__(self, content, id = None):
        self.id = None
        self.content = content

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)