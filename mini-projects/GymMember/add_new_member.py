
import streamlit as st

class GymMember:
    total_member = 0

    # -- Initiallize a new gym member --
    def __init__(self, name, age, membership_tier):
        self.name = name
        self.age = age
        self.membership_tier = membership_tier

        GymMember.total_member += 1
    
    # -- Display --
    def display (self):
        st.markdown("---")
        st.subheader(f"🏋️‍♂️ {self.name}")
        st.write(f"🎂 Age: {self.age}")
        st.write(f"💳 Tier: {self.membership_tier}")
        st.markdown(f"---")

    # -- @Staticmethod
    def calories_burned(minutes, intensity=1.0, name="Someone"):
        calories = minutes * 5 *intensity
        return f"🔥 {name} burned {calories:1.f} calories in {minutes} mins with intensity {intensity}"
    
# -- Streamlit App --
st.set_page_config(page_title="Gym Member Tracker", page_icon="💪")
st.title("🏋🏾‍♂️ Gym Member Tracker 🏋🏾‍♂️")

# -- Session state setup --
if "member" not in st.session_state:
    st.session_state.members = []

# -- Member Creation Form --
st.subheader("➕ Add New Gym Member")

with st.form("member_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    tier = st.selectbox("Membership Tier", ["Bronce", "Silver", "Gold", "Black"])

    submitted = st.form_submit_button("Add Member")
    if submitted:
        new_member = GymMember(name, age, tier)
        st.session_state.members.append(new_member)
        st.success(f"{name} was added successfully! 🫡")

# -- Display All Members -- 
st.subheader("📋 Current Member")

if st.session_state.members:
    for member in st.session_state.members:
        member.display()
else:
    st.info("No member added yet :(")

# -- Calories Calculator -- 
st.header(f"🔥 Calories Burned Calculator")

with st.form("calories_form"):
    name = st.text_input("Your name", key="cal_name")
    minutes = st.slider("Workout Duration (min)", 0, 120, 30)
    intensity = st.slider("Workout Intensity", 0.5, 2.0, 1.0)

    calculate = st.form_submit_button("Calculate")
    if calculate:
        result = GymMember.calories_burned(minutes, intensity, name)
        st.success(result)

