import streamlit as st
import json

# ========== GymMember Class ==========
class GymMember:
    total_member = 0

    def __init__(self, name, age, membership_tier):
        self.name = name
        self.age = age
        self.membership_tier = membership_tier
        GymMember.total_member += 1

    def display(self):
        st.markdown("----")
        st.subheader(f"🏋️‍♂️ {self.name}")
        st.write(f"🎂 Age: {self.age}")
        st.write(f"💳 Tier: {self.membership_tier}")
        st.markdown("----")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "membership_tier": self.membership_tier
        }

    @staticmethod
    def calories_burned(minutes, intensity=1.0, name="Someone"):
        calories = minutes * 5 * intensity
        return f"🔥 {name} burned {calories:.1f} calories in {minutes} mins with intensity {intensity}"

# ========== Streamlit App Setup ==========
st.set_page_config(page_title="Gym Member Tracker", page_icon="💪")
st.title("💪 Gym Member Tracker")

# ========== Session State Setup ==========
if "members" not in st.session_state:
    st.session_state.members = []

# ========== Member Creation Form ==========
st.subheader("➕ Add New Gym Member")

with st.form("member_form"):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    tier = st.selectbox("Membership Tier", ["Bronce", "Silver", "Gold", "Platinum"])

    submitted = st.form_submit_button("Add Member")
    if submitted:
        new_member = GymMember(name, age, tier)
        st.session_state.members.append(new_member)
        st.success(f"{name} was added successfully! 💪")

# ========== Search and Filter ==========
st.subheader("📋 Current Members")

search_name = st.text_input("🔍 Search by name:")
selected_tier = st.selectbox("🎯 Filter by Tier", ["All", "Bronce", "Silver", "Gold", "Platinum"])

filtered_members = []

for member in st.session_state.members:
    name_match = search_name.lower() in member.name.lower()
    tier_match = (selected_tier == "All") or (member.membership_tier == selected_tier)
    
    if name_match and tier_match:
        filtered_members.append(member)

if filtered_members:
    for member in filtered_members:
        member.display()
else:
    st.warning("🚫 No members match your search.")

# ========== Export to JSON ==========
if st.button("💾 Export Members to JSON"):
    with open("members.json", "w") as f:
        data = [member.to_dict() for member in st.session_state.members]
        json.dump(data, f, indent=4)
    st.success("✅ Members exported to members.json!")

# ========== Calories Calculator ==========
st.header("🔥 Calories Burned Calculator")

with st.form("calorie_form"):
    cal_name = st.text_input("Your name", key="cal_name")
    minutes = st.slider("Workout Duration (min)", 0, 120, 30)
    intensity = st.slider("Workout Intensity", 0.5, 2.0, 1.0)

    calculate = st.form_submit_button("Calculate")
    if calculate:
        result = GymMember.calories_burned(minutes, intensity, cal_name)
        st.success(result)