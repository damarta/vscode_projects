# Base Class:
    #Exercise -> name, sets, reps.

# SubClasses:
    # StrengthExercises -> + weight
    # CardioExercise -> + duration, distance

# Wrapper Class:
    # Workout -> date, list of exercises, get_summary()

""" ----  🧠 Step 1: Build the Class System --- """

from datetime import datetime

# Base Exercises Class (Abstraction + Encapsulation)
class Exercise:

    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps

    def get_summary(self):
        return f"{self.name}: {self.sets} sets x {self.reps} reps"
    
# Strength Exercise (inheritance):
class StrengthExercise(Exercise):

    def __init__(self, name, sets, reps, weight):
        super().__init__(name, sets, reps)
        self.weight = weight

    def get_summary(self):  # Polymorphism -> custom summary
        return f"{self.name}: {self.sets} x {self.reps} @ {self.weight}kg"
    
# CardioExercises (inheritance):
class CardioExercise(Exercise):

    def __init__(self, name, duration, distance):
        super().__init__(name, sets=1, reps=1)  # dummy base values
        self.duration = duration    # in minutes
        self.distance = distance    # in km

    def get_summary(self):
        return f"{self.name}: {self.duration} mins, {self.distance} km"
    
# Workout class: groups exercises + date (composition)
class Workout:

    def __init__(self):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.exercises = []

    def add_exercises(self, exercise):
        self.exercises.append(exercise)

    def get_summary(self):
        print(f"\nWorkout Summary - {self.date}")

        for ex in self.exercises:
            print(f"• {ex.get_summary()}")


""" --- Step 2: Add Dummy Test Code --- """

# Simulate using the app
my_workout = Workout()

# Add some Exercises
my_workout.add_exercise(StrengthExercise("Bench Press", 6, 10, 60))
my_workout.add_exercise(StrengthExercise("Squat", 6, 10, 80))
my_workout.add_exercise(CardioExercise("Running", 20, 3.0))

# Show summary
my_workout.get_summary()