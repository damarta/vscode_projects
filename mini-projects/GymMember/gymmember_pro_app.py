

import streamlit as st
import json
from PIL import Image
import io

# ========== Class Definition ==========
class GymMember:
    total_members = 0

    def __init__(self, name, age, tier, image_bytes=None):
        self.name = name
        self.age = age
        self.tier = tier
        self.image_bytes = image_bytes
        GymMember.total_members += 1

    def display(self):
        col1, col2 = st.columns([1, 3])
        with col1:
            if self.image_bytes:
                st.image(Image.open(io.BytesIO(self.image_bytes)), width=100)
            else:
                st.image("https://via.placeholder.com/100", width=100)

        with col2:
            st.subheader(f"{self.name}")
            st.write(f"🎂 Age: {self.age}")
            st.write(f"💳 Tier: {self.tier}")
            st.markdown("---")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "tier": self.tier
        }

    @staticmethod
    def calories_burned(minutes, intensity=1.0, name="Someone"):
        calories = minutes * 5 * intensity
        return f"🔥 {name} burned {calories:.1f} calories in {minutes} minutes at intensity {intensity}"

# ========== Streamlit Page Config ==========
st.set_page_config(page_title="GymMember Pro App", page_icon="💪", layout="wide")
st.title("💪 GymMember Pro App")

# ========== Session State ==========
if "members" not in st.session_state:
    st.session_state.members = []

# ========== Sidebar Navigation ==========
st.sidebar.title("📂 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "➕ Add Member", "📋 View Members", "📊 Stats", "🔥 Calories Calculator"])

# ========== Add Member Page ==========
if page == "➕ Add Member":
    st.header("➕ Add New Gym Member")

    with st.form("add_member_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", 0, 120, step=1)
        tier = st.selectbox("Membership Tier", ["Bronce", "Silver", "Gold", "Platinum"])
        image_file = st.file_uploader("Upload Profile Photo", type=["jpg", "jpeg", "png"])
        if image_file:
            st.image(image_file, caption="Preview", width=150)
        submitted = st.form_submit_button("Add Member")

        if submitted:
            image_bytes = image_file.read() if image_file else None
            new_member = GymMember(name, age, tier, image_bytes)
            st.session_state.members.append(new_member)
            st.success(f"{name} added successfully! 💪")

# ========== View Members Page ==========
elif page == "📋 View Members":
    st.header("📋 Current Members")

    # Search and Filter
    search = st.text_input("🔍 Search by name")
    tier_filter = st.selectbox("🎯 Filter by Tier", ["All", "Bronce", "Silver", "Gold", "Platinum"])

    filtered = []
    for m in st.session_state.members:
        match_name = search.lower() in m.name.lower()
        match_tier = tier_filter == "All" or m.tier == tier_filter
        if match_name and match_tier:
            filtered.append(m)

    if filtered:
        for member in filtered:
            member.display()
    else:
        st.info("No matching members found.")

    # Export to JSON
    if st.button("💾 Export Members to JSON"):
        data = [m.to_dict() for m in st.session_state.members]
        with open("members.json", "w") as f:
            json.dump(data, f, indent=4)
        st.success("Members exported to members.json!")

# ========== Stats Page ==========
elif page == "📊 Stats":
    st.header("📊 Membership Stats")

    total = len(st.session_state.members)
    tiers = {"Bronce": 0, "Silver": 0, "Gold": 0, "Platinum": 0}
    ages = []

    for m in st.session_state.members:
        tiers[m.tier] += 1
        ages.append(m.age)

    st.write(f"🔢 Total Members: {total}")
    st.write(f"📈 Average Age: {sum(ages)/len(ages):.1f}" if ages else "📈 Average Age: N/A")

    st.bar_chart(tiers)

# ========== Calories Page ==========
elif page == "🔥 Calories Calculator":
    st.header("🔥 Calories Burned Calculator")

    with st.form("calorie_form"):
        name = st.text_input("Your name")
        minutes = st.slider("Workout Duration (min)", 0, 120, 30)
        intensity = st.slider("Workout Intensity", 0.5, 2.0, 1.0)
        submitted = st.form_submit_button("Calculate")

        if submitted:
            result = GymMember.calories_burned(minutes, intensity, name)
            st.success(result)

# ========== Home ==========
else:
    st.subheader("Welcome to the GymMember Pro App!")
    st.write("Track your gym members, manage their profiles, and calculate calories burned — all in one place.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Gym_Icon.svg/1024px-Gym_Icon.svg.png", width=300)