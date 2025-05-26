class GymMember:
    total_member = 0 # class variable

    def __init__(self, name):
        self.name = name
        GymMember.total_member += 1

    def __str__(self):
        return f"{self.name} is part of the gym community :)"
        
    def __repr__(self):
        return f"GymMember(name='{self.name}')"

    def introduce(self):
        print(f"👋 Hello, my name is {self.name}")

    @classmethod
    def get_total_members(cls):
        print(f"📊 Total members: {cls.total_member}")

    @staticmethod
    def calories_burned(minutes, intensity=1.0):
        return minutes * 5 * intensity
    
# Create two gym members:
m1 = GymMember("Da Marta")
m2 = GymMember("Luis")

# Call regular method: (need an object)
m1.introduce()   # -> introduces herself, print the message.

# Call @classmethod: (you don't need an object)
GymMember.get_total_members() # -> output

# Call @staticmethod:
burned = GymMember.calories_burned(30,1.2)
print(f"🔥 Calories burned: {burned}")

print(m1)    # Triggers __str__()
print(m2)    # Triggers __str__()

# Just writing the variable shows __repr__ in many environments
m1

# =======================================================
""" --- 🧠 EXPLANATION --- """

    # ✅ 1. Regular method — .introduce()
    # 	•	Needs self
    # 	•	Works on an object
    # 	•	Accesses the object’s data (self.name)

                # ✅ Good for: personal actions → “What does THIS object do?”
#-------------------------------------------------------------------

    # ✅ 2. @classmethod — .get_total_members()
    # 	•	Needs cls → refers to the class itself
    # 	•	Used to access or update class variables
    # 	•	Does not need an object — works on the class

                # ✅ Good for: anything shared by all members
#-------------------------------------------------------------------

    # ✅ 3. @staticmethod — .calories_burned()
    #     •	No self, no cls
    #     •	Doesn’t access object or class data
    #     •	Just a utility function that logically lives inside the class

                # ✅ Good for: pure calculations