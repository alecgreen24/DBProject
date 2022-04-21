import json
class Test():
    def __init__(self, creator_id, title, created_at=None, id=None, active=True, updated_at=None):
        self.creator_id = creator_id
        self.title = title
        self.created_at = created_at
        self.id = id
        self.active = active
        self.updated_at = updated_at
        self.questions = []

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
