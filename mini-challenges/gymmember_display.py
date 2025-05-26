class GymMember:
    total_member = 0

    def __init__(self, name, age, membership_tier):
        """Initialize a new gym member."""
        self.name = name
        self.age = age
        self.membership_tier = membership_tier
        GymMember.total_member += 1

    # -- String Representations --
    def __str__(self):
        return f"{self.name} ({self.age}y, {self.membership_tier} tier) is part of the gym community 💪"

    def __repr__(self):
        return f"GymMember(name='{self.name}', age={self.age}, tier='{self.membership_tier}')"

    # -- Length Behavior --
    def __len__(self):
        return len(self.name)

    # -- Instance Method --
    def introduce(self):
        print(f"👋 Hi, my name is {self.name}!")

    # -- Class Method --
    @classmethod
    def get_total_members(cls):
        print(f"📊 Total members: {cls.total_member}")

    # -- Static Method --
    @staticmethod
    def calories_burned(minutes, intensity=1.0, name="Someone"):
        """Calculate calories burned with a formatted message."""
        calories = minutes * 5 * intensity
        return f"🔥 {name} burned {calories} calories in {minutes} mins with intensity {intensity}"

    # -- Display Method --
    def display(self):
        print("─" * 40)
        print(f"🏋️‍♂️ Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"💳 Membership Tier: {self.membership_tier}")
        print("─" * 40)

# === Usage Example ===


# ✅ Create gym members:
m1 = GymMember("Da Marta", 29, "Gold")
m2 = GymMember("Luis", 29, "Bronce")

# ✅ Only show the visual display:
m1.display()
m2.display()
# hello
