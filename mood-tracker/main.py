import streamlit as st  # for creating web interface
import pandas as pd  # for data manipulation
import datetime  # for handling dates
import csv  # for reading and writing CSV files
import os  # for file operations

st.markdown(
    """
    <style>
        /* Gradient background */
        .stApp {
            background: linear-gradient(to right, #FFDEE9, #B5FFFC);
            font-family: 'Arial', sans-serif;
        }

        /* Title styling */
        .stApp h1 {
            color: #4A4A4A;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            padding: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Subheader styling */
        .stApp h2 {
            color: #333333;
            text-align: center;
            font-size: 24px;
        }

        /* Select box styling */
        .stSelectbox {
            border: 2px solid #FF758C;
            border-radius: 10px;
            padding: 10px;
            background-color: white;
            font-size: 18px;
        }

        /* Button styling */
        .stButton button {
            background: linear-gradient(to right, #FF758C, #FF7EB3);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 18px;
            padding: 10px 20px;
            font-weight: bold;
            transition: 0.3s;
        }

        .stButton button:hover {
            background: linear-gradient(to right, #D84A6F, #FF758C);
        }

        /* Success message */
        .stAlert {
            background-color: #D4EDDA;
            color: #155724;
            border-left: 5px solid #28A745;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
        }

        /* Footer */
        .stApp p {
            text-align: center;
            font-size: 16px;
            color: #4A4A4A;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)




MOOD_FILE = "mood_log.csv"  # ✅ Correct spelling

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])  # ✅ Fixed spelling
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:  # ✅ Added encoding="utf-8" to fix emoji issue
        writer = csv.writer(file)  
        writer.writerow([date, mood])  # ✅ Moved inside the with block

st.title("😀 Mood Tracker")

today = datetime.date.today()

st.subheader("📝 How are you feeling today?")

mood = st.selectbox("Select your mood", ["😀 Happy", "😐 Neutral", "😟 Stressed", "😢 Sad", "😡 Angry"])

if st.button("Log Mood"):
    save_mood_data(today, mood)  
    st.success(f"Mood Logged Successfully! {mood}")  # ✅ Fixed f-string issue

data = load_mood_data()

if not data.empty:

    st.subheader("Mood trends over time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

    st.write(" Build with ❤️ by Shabnam Wahid")
