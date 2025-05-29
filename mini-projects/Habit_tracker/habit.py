# Habit model & logic
class Habit:
    def __init__(self, name, done=False, priority="🟢"):
        self.name = name.strip().title()
        self.done = done
        self.priority = priority  # red, orange, green

    def to_dict(self):
        return {"name": self.name, "done": self.done, "priority": self.priority}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["done"], data.get("priority", "green"))
