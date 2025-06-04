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


# Load data
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
    # Show promise + day count
    start_date = datetime.strptime(data["start_date"], "%Y-%m-%d")
    today = datetime.now().date()
    days_passed = (today - start_date.date()).days + 1
    st.success(f"Your Promise: *{data['promise']}* (Day {days_passed} of 30)")

    # Check-in button
    if today.strftime("%Y-%m-%d") not in data["checkins"]:
        if st.button("✅ I did it today!"):
            data["checkins"].append(today.strftime("%Y-%m-%d"))
            save_data(data)
            st.success("Check-in saved!")

    # Calendar tracker
    st.subheader("📅 Your 30-Day Promise Calendar")
    cols = st.columns(6)

    for i in range(30):
        day = start_date + timedelta(days=i)
        label = day.strftime("%d %b")
        day_str = day.strftime("%Y-%m-%d")

        if day_str in data["checkins"]:
            cols[i % 6].success(f"✔️ {label}")
        elif day.date() < today:
            cols[i % 6].error(f"❌ {label}")
        elif day.date() == today:
            cols[i % 6].warning(f"🔸 {label}")
        else:
            cols[i % 6].info(f"⬜ {label}")

    # Progress Summary
    st.subheader("📊 Progress Summary")
    total_days = 30
    completed_days = len(data["checkins"])
    st.progress(completed_days / total_days)
    st.info(f"✅ {completed_days} / {total_days} days completed")

    # Reset Option
    st.subheader("🔁 Reset Your Promise")
    if st.button("Start Over"):
        data = {"promise": "", "start_date": "", "checkins": []}
        save_data(data)
        st.warning("Your promise has been reset. Please refresh the page.")
