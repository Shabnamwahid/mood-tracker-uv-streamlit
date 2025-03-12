# import streamlit as st  # for creating web interface
# import pandas as pd  # for data manipulation
# import datetime  # for handling dates
# import csv  # for reading and writing CSV files
# import os  # for file operations

# st.markdown(
#     """
#     <style>
#         /* Gradient background */
#         .stApp {
#             background: linear-gradient(to right, #FFDEE9, #B5FFFC);
#             font-family: 'Arial', sans-serif;
#         }

#         /* Title styling */
#         .stApp h1 {
#             color: #4A4A4A;
#             text-align: center;
#             font-size: 36px;
#             font-weight: bold;
#             padding: 10px;
#             text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
#         }

#         /* Subheader styling */
#         .stApp h2 {
#             color: #333333;
#             text-align: center;
#             font-size: 24px;
#         }

#         /* Select box styling */
#         .stSelectbox {
#             border: 2px solid #FF758C;
#             border-radius: 10px;
#             padding: 10px;
#             background-color: white;
#             font-size: 18px;
#         }

#         /* Button styling */
#         .stButton button {
#             background: linear-gradient(to right, #FF758C, #FF7EB3);
#             color: white;
#             border: none;
#             border-radius: 12px;
#             font-size: 18px;
#             padding: 10px 20px;
#             font-weight: bold;
#             transition: 0.3s;
#         }

#         .stButton button:hover {
#             background: linear-gradient(to right, #D84A6F, #FF758C);
#         }

#         /* Success message */
#         .stAlert {
#             background-color: #D4EDDA;
#             color: #155724;
#             border-left: 5px solid #28A745;
#             padding: 10px;
#             border-radius: 5px;
#             font-size: 16px;
#         }

#         /* Footer */
#         .stApp p {
#             text-align: center;
#             font-size: 16px;
#             color: #4A4A4A;
#             font-weight: bold;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )




# MOOD_FILE = "mood_log.csv"  # ✅ Correct spelling

# def load_mood_data():
#     if not os.path.exists(MOOD_FILE):
#         return pd.DataFrame(columns=["Date", "Mood"])  # ✅ Fixed spelling
#     return pd.read_csv(MOOD_FILE)

# def save_mood_data(date, mood):
#     with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:  # ✅ Added encoding="utf-8" to fix emoji issue
#         writer = csv.writer(file)  
#         writer.writerow([date, mood])  # ✅ Moved inside the with block

# st.title("😀 Mood Tracker")

# today = datetime.date.today()

# st.subheader("📝 How are you feeling today?")

# mood = st.selectbox("Select your mood", ["😀 Happy", "😐 Neutral", "😟 Stressed", "😢 Sad", "😡 Angry"])

# if st.button("Log Mood"):
#     save_mood_data(today, mood)  
#     st.success(f"Mood Logged Successfully! {mood}")  # ✅ Fixed f-string issue

# data = load_mood_data()

# if not data.empty:

#     st.subheader("Mood trends over time")

#     data["Date"] = pd.to_datetime(data["Date"])

#     mood_counts = data.groupby("Mood").count()["Date"]

#     st.bar_chart(mood_counts)

#     st.write(" Build with ❤️ by Shabnam Wahid")


import streamlit as st  # Web interface
import pandas as pd  # Data manipulation
import datetime  # Date handling
import csv  # CSV read/write
import os  # File operations

# ✅ Mood log CSV file
MOOD_FILE = "mood_log.csv"

# ✅ CSS for better styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #FFDEE9, #B5FFFC);
            font-family: 'Arial', sans-serif;
        }
        .stApp h1 {
            color: #4A4A4A;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .stApp h2 {
            color: #333333;
            text-align: center;
            font-size: 24px;
        }
        .stButton button {
            background: linear-gradient(to right, #FF758C, #FF7EB3);
            color: white;
            border-radius: 12px;
            font-size: 18px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background: linear-gradient(to right, #D84A6F, #FF758C);
        }
        .stAlert {
            background-color: #D4EDDA;
            color: #155724;
            border-left: 5px solid #28A745;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
        }
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

# ✅ Function to load mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):  
        return pd.DataFrame(columns=["Date", "Mood"])  # Empty DataFrame if file doesn't exist

    try:
        df = pd.read_csv(MOOD_FILE, encoding="utf-8", on_bad_lines="skip")  # ✅ Ignore bad lines
        df = df.drop_duplicates()  # ✅ Remove duplicate entries
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")  # ✅ Convert Date column to datetime
        df = df.dropna()  # ✅ Remove rows with invalid dates
        return df
    except Exception as e:
        st.error(f"⚠ Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])  # Return empty DataFrame on error

# ✅ Function to save mood data
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline="", encoding="utf-8") as file:  
        writer = csv.writer(file)
        writer.writerow([date, mood])  

# ✅ Title
st.title("😀 Mood Tracker")

# ✅ Today's date
today = datetime.date.today()

# ✅ Mood selection
st.subheader("📝 How are you feeling today?")
mood = st.selectbox("Select your mood", ["😀 Happy", "😐 Neutral", "😟 Stressed", "😢 Sad", "😡 Angry"])

# ✅ Log mood button
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success(f"Mood Logged Successfully! {mood}")

# ✅ Load and display mood trends
data = load_mood_data()
if not data.empty:
    st.subheader("📊 Mood Trends Over Time")
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)

st.write("✨ Built with ❤️ by Shabnam Wahid")
 
