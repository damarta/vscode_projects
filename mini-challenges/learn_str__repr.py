class GymMember:
    total_member = 0

    def __init__(self, name):
        self.name = name
        GymMember.total_member += 1

    def __str__(self):
        return f"{self.name} is part of the gym community 💪"

    def __repr__(self):
        return f"GymMember(name='{self.name}')"
    
# -  Usage:  -

# Create the object:
m = GymMember("Da Marta")

print(m)       # 🟢 Calls __str__() → Da Marta is part of the gym community 💪
m              # 🔵 Calls __repr__() → GymMember(name='Da Marta')