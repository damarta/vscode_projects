class Habit:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def to_dict(self):
        return {"name": self.name, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["done"])
