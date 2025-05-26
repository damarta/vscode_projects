class GymMember:
    total_member = 0

    def __init__(self, name, age, membership_tier):
        self.name = name
        self.age = age
        self.membership_tier = membership_tier

        GymMember.total_member +=1

    # -- String Representations --
    def __str__(self):
        return f"{self.name} ({self.age}y, {self.membership_tier} tier) is part of the gym community 💪"

    def __repr__(self):
        return f"GymMember(name='{self.name}', age={self.age}, tier='{self.membership_tier}')"
    
    # -- Length Behaior --
    def __len__(self):
        return len(self.name)
    
    # -- Instance Method --
    def introduce(self):
        print(f"👋 Hi, my name is {self.name}!")
    
    # -- Class Method --
    @classmethod
    def get_total_members(cls):
        print(f"📊 Total members: {cls.get_total_members}")

    # -- Static Method --
    @staticmethod
    def calories_burned(minutes, intensity =1.0, name="Someone"):
        calories = minutes * 5 * intensity
        return f"🔥 {name} burned {calories} calories in {minutes} mins with instensity {intensity}"

# --- Usage Example ---

# Create two gym members:
m1 = GymMember("Da marta", 29, "Gold")
m2 = GymMember("Luis", 29, "Bronce")

# Call regular method: -> (need an object)
m1.introduce()
m2.introduce()

#  String:
print(m1) 
print(m2)

# Repesentatio:
print(repr(m1))
print(repr(m2))

# Length of member names:
print(len(m1))
print(len(m2))

# Total members: (Call @classmethod)
GymMember.get_total_members()

# Using Static method with custom message:
msg = GymMember.calories_burned(20, 1.4, name="Luis")
print(msg)