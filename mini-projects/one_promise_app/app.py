import streamlit as st
import json
import os
from datetime import datetime, timedelta

DATA_FILE = "data/promise_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"promise": "", "start_date": "", "checkins": []}
    else:
        return {"promise": "", "start_date": "", "checkins": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# Load and setup
st.title("🎯 One Promise")
data = load_data()

if not data["promise"]:
    st.subheader("Set your 30-day promise:")
    promise = st.text_input("What's the one thing you’ll commit to?")
    if st.button("Lock in my promise"):
        data["promise"] = promise
        data["start_date"] = datetime.now().strftime("%Y-%m-%d")
        data["checkins"] = []
        save_data(data)
        st.success("Promise saved!")
else:
    # Show progress
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
    today = datetime.now().date()
    days_passed = (today - start_date.date()).days + 1
    st.success(f"Your Promise: *{data['promise']}* (Day {days_passed} of 30)")

    # Check-in section
    if today.strftime("%Y-%m-%d") not in data["checkins"]:
        if st.button("✅ I did it today!"):
            data["checkins"].append(today.strftime("%Y-%m-%d"))
            save_data(data)
            st.success("Check-in saved!")

    # Show Calendar Grid
    st.subheader("📅 Your 30-Day Promise Calendar")
    cols = st.columns(6)
    for i in range(30):
        day = start_date + timedelta(days=i)
        label = day.strftime("%d %b")
        if day.strftime("%Y-%m-%d") in data["checkins"]:
            cols[i % 6].success(f"✔️ {label}")
        elif day < today:
            cols[i % 6].error(f"❌ {label}")
        elif day == today:
            cols[i % 6].warning(f"🔸 {label}")
        else:
            cols[i % 6].info(f"⬜ {label}")
