# This file is the blueprint for every habit.

class Habit:

    def __init__(self, name, done=False):
        self.name = name
        self.done = done
        # 💬 What this means:
        # - You create a habit like: Habit("Workout")
        # - done is False by default — we’ll mark it as True later when completed

    def to_dict(self):
        return {"name": self.name, "done": self.done}
        # 💬 What this means:
        # - This method converts your object to a dictionary, so we can save it as JSON.

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["done"])
        # 💬 What this means:
        # - This takes a dictionary and re-creates the object
