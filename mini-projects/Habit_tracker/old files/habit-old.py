# This file is the blueprint for every habit.

# == LOG DECORATOR (must be defined before it's used) ==
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"⚙️ Running {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"✅ Finished {func.__name__}")
        return result
    return wrapper


# == HABIT CLASS ==
class Habit:

    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        clean = value.strip().title()
        if not clean:
            raise ValueError("Name cannot be empty.")
        self._name = clean

    @log_action
    def to_dict(self):
        return {"name": self.name, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["done"])

 # 💬 What this means:
