class Habit:
    def __init__(self, name, done=False, priority="green"):
        self.name = name.strip().title()
        self.done = done
        self.priority = priority

    def to_dict(self):
        return {"name": self.name, "done": self.done, "priority": self.priority}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["done"], data.get("priority", "green"))


class DailyGoal:
    def __init__(self, date, habits=None):
        self.date = date  # e.g., "2025-05-29"
        self.habits = habits if habits else []

    def to_dict(self):
        return {
            "date": self.date,
            "habits": [h.to_dict() for h in self.habits]
        }

    @classmethod
    def from_dict(cls, data):
        habits = [Habit.from_dict(h) for h in data.get("habits", [])]
        return cls(data["date"], habits)


class WeeklyGoal:
    def __init__(self, week_number, daily_goals=None):
        self.week_number = week_number  # e.g., 22
        self.daily_goals = daily_goals if daily_goals else []

    def to_dict(self):
        return {
            "week_number": self.week_number,
            "daily_goals": [dg.to_dict() for dg in self.daily_goals]
        }

    @classmethod
    def from_dict(cls, data):
        daily_goals = [DailyGoal.from_dict(dg)
                       for dg in data.get("daily_goals", [])]
        return cls(data["week_number"], daily_goals)


class MonthlyGoal:
    def __init__(self, month, year, weekly_goals=None):
        self.month = month  # e.g., 5 for May
        self.year = year    # e.g., 2025
        self.weekly_goals = weekly_goals if weekly_goals else []

    def to_dict(self):
        return {
            "month": self.month,
            "year": self.year,
            "weekly_goals": [wg.to_dict() for wg in self.weekly_goals]
        }

    @classmethod
    def from_dict(cls, data):
        weekly_goals = [WeeklyGoal.from_dict(
            wg) for wg in data.get("weekly_goals", [])]
        return cls(data["month"], data["year"], weekly_goals)
