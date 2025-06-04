import streamlit as st
import json
import os
from datetime import datetime, timedelta
import random
import requests


def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            return response.json()[0]['q'] + " — " + response.json()[0]['a']
        else:
            return random.choice(QUOTES)  # fallback to local
    except:
        return random.choice(QUOTES)


QUOTES = [
    "Keep going, you're doing great!",
    "Discipline beats motivation every time.",
    "A promise to yourself is the most powerful kind.",
    "Small steps every day lead to big results.",
    "Stay consistent. You're building a new identity.",
    "You kept your word today. That's powerful.",
    "Today you chose growth. Respect.",
    "Win the day. That's all it takes.",
    "Brick by brick, you're building the new you.",
    "One day at a time. You’ve got this."
]

DATA_FILE = "data/promise_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            return_data = None
            with open(DATA_FILE, "r") as f:
                return_data = json.load(f)
            if "quote_history" not in return_data:
                return_data["quote_history"] = []
            return return_data
        except json.JSONDecodeError:
            return {"promise": "", "start_date": "", "checkins": [], "reset_count": 0, "quote_history": []}
    else:
        return {"promise": "", "start_date": "", "checkins": [], "reset_count": 0, "quote_history": []}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


# Load data
st.title("🎯 One Promise")
data = load_data()

if "quote" not in st.session_state:
    st.session_state.quote = ""

if not data["promise"]:
    st.subheader("Set your 30-day promise:")
    promise = st.text_input("What's the one thing you’ll commit to?")
    if st.button("Lock in my promise"):
        data["promise"] = promise
        data["start_date"] = datetime.now().strftime("%Y-%m-%d")
        data["checkins"] = []
        data["reset_count"] = data.get("reset_count", 0)
        data["quote_history"] = data.get("quote_history", [])
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
            st.session_state.quote = fetch_quote()
            if "quote_history" not in data:
                data["quote_history"] = []
            data["quote_history"].append({
                "date": today.strftime("%Y-%m-%d"),
                "quote": st.session_state.quote
            })
            save_data(data)

    if today.strftime("%Y-%m-%d") in data["checkins"] and st.session_state.quote:
        st.subheader("💬 Motivation of the Day")
        st.info(f"**{st.session_state.quote}**")
    else:
        st.subheader("💬 Motivation of the Day")
        st.info(
            "📝 No quote yet. Click '✅ I did it today!' to unlock today’s motivation.")

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

    # Check if user completed all 30 days
    if completed_days == total_days:
        st.balloons()
        st.success("🎉 Congratulations! You've completed your 30-day promise.")

    # Quote History Display
    st.subheader("📚 Quote History")
    if data.get("quote_history"):
        for item in reversed(data["quote_history"][-5:]):
            st.markdown(f"**{item['date']}** — _{item['quote']}_")
    else:
        st.info("No quote history yet.")

    # Reset Option
    st.subheader("🔁 Reset Your Promise")
    st.caption(f"Resets used: {data.get('reset_count', 0)} / 4")
    if st.button("Start Over"):
        if data.get("reset_count", 0) < 4:
            data = {"promise": "", "start_date": "", "checkins": [],
                    "reset_count": data.get("reset_count", 0) + 1, "quote_history": []}
            save_data(data)
            st.warning("Your promise has been reset. Please refresh the page.")
        else:
            st.error("❌ You have reached the maximum number of restarts (4).")
