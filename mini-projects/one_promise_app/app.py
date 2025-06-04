import streamlit as st
import json
import os
from datetime import datetime

# File to store data
DATA_FILE = "data/promise_data.json"

# Load or initialize data


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {"promise": "", "start_date": "", "checkins": []}
    else:
        return {"promise": "", "start_date": "", "checkins": []}


# Save data


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# App UI
st.title("🎯 One Promise")
data = load_data()

if not data["promise"]:
    st.subheader("Set your 21-day promise:")
    promise = st.text_input("What's the one thing you’ll commit to?")
    if st.button("Lock in my promise"):
        data["promise"] = promise
        data["start_date"] = datetime.now().strftime("%Y-%m-%d")
        data["checkins"] = []
        save_data(data)
        st.success("Promise saved! Come back daily to check in.")
else:
    st.success(f"Your Promise: *{data['promise']}* (Day 1 of 21)")
