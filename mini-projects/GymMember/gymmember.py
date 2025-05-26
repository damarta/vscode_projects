
import streamlit as st

class GymMember:
    total_member = 0

    # -- Initiallize a new gym member --
    def __init__(self, name, age, membership_tier):
        self.name = name
        self.age = age
        self.membership_tier = membership_tier

        GymMember.total_member += 1

    # -- String --
    def __str__(self):
        return f"{self.name} ({self.age}y, {self.membership_tier}tier)"
    
    # -- Display --
    def display (self):
        st.markdown("---")
        st.subheader(f"🏋️‍♂️ {self.name}")
        st.write(f"🎂 Age: {self.age}")
        st.write(f"💳 Membership Tier: {self.membership_tier}")
        st.markdown(f"---")

    # -- @Staticmethod
    def calories_burned(minutes, intensity=1.0, name="Someone"):
        calories = minutes * 5 *intensity
        return f"🔥 {name} burned {calories} calories in {minutes} mins with intensity {intensity}"
    
# -- Streamlit App --
st.title("🏋🏾‍♂️ Gym Member Tracker 🏋🏾‍♂️")

# Create members:
m1 = GymMember("Benthe", 27, "Gold")
m2 = GymMember("Da marta", 29, "Black")

# Display members:
m1.display()
m2.display()

# Calories calculator:
st.header("🔥 Calories Burned Calculator")

name = st.text_input("Name", "Benthe")
minutes = st.slider("Minutes Exercised", 0, 120,30)
intensity = st.slider("Intensity", 0.5, 2.0, 1.0)

if st.button("Calculate"):
    result = GymMember.calories_burned(minutes, intensity, name)
    st.success(result)