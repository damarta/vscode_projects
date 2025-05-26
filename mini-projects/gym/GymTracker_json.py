#🔹 -> means new info added


from datetime import datetime

# Base Exercise Class (Abstraction + Encapsulation)
class Exercises:

    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps
    
    #🔹 Add to Exercise (base class):
    def to_dict(self):
        return {
            "type": "Exercise",
            "name": self.name,
            "sets": self.sets,
            "reps": self.reps,
        }

    def get_summary(self):
        return f"{self.name}: {self.sets} sets x {self.reps} reps"

# Strength Exercise (Inheritance):
class StrengthExercise(Exercises):

    def __init__(self, name, sets, reps, weight):
        super().__init__(name, sets, reps)
        self.weight = weight

    #🔹 Add to StrengthExercise:
    def to_dict(self):
        base = super().to_dict()
        base["type"] = "StrengthExercise"
        base["weight"] = self.weight
        return base

    def get_summary(self):  # Polymorphism -> Custom Summary
        return f"{self.name}: {self.sets} x {self.reps} @ {self.weight} kg"
    

# Cardio Exercises (Inheritance):
class CardioExercise(Exercises):

    def __init__(self, name, duration, distance):
        super().__init__(name, sets=1, reps=1)
        self.duration = duration # in mins
        self.distance = distance # in km


    #🔹 Add to CardioExercise:
    def to_dict(self):
        return {
            "type": "CardioExercise",
            "name": self.name,
            "duration": self.duration,
            "distance": self.distance,
        }

    def get_summary(self):
        return f"{self.name}: {self.duration} mins, {self.distance} km"

# Workout class
class Workout:
    
    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
    
    #🔹 add to Workout class:
    def to_dict(self):
        return {
            "date": self.date,
            "exercises": [ex.to_dict() for ex in self.exercises]
        }


    def get_summary(self):
        print(f"\nWorkout Summary - {self.date}")

        for ex in self.exercises:
            print(f"• {ex.get_summary()}")


    #🔹 Add a function to save your workout to JSON
import json

def save_workout_to_json(workout, filename="gym_workouts.json"):

    try:
        with open(filename, "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        data = []

    data.append(workout.to_dict())

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

# Simulate using the app
my_workout = Workout()

# Add some Exercises
my_workout.add_exercise(StrengthExercise("Bench Press", 6, 10, 60))
my_workout.add_exercise(StrengthExercise("Squat", 6, 10, 80))
my_workout.add_exercise(CardioExercise("Running", 20, 3.0))

# Show summary
my_workout.get_summary()

#🔹 Call the function to save your workout
save_workout_to_json(my_workout)
print("✅ Workout saved to gym_workouts.json")