from turtle import title


class Test():
    def __init__(self, creator_id, title, active=True):
        self.id = None
        self.creator_id = creator_id
        self.title = title
        self.active = active
        self.updated_at = None

