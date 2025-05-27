from habit import Habit

habits = [
    Habit("Walk dog", True),
    Habit("Stretch", False),
    Habit("Read", False)
]
incomplete = [h for h in habits if not h.done]
# 💬 What this means:
# - “Loop over all habits, and only keep the ones where done is False.”

for h in incomplete:
    print(h.name)
