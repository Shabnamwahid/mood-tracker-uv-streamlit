import pandas as pd

# ✅ Load CSV with correct format
df = pd.read_csv("mood_log.csv", encoding="utf-8", on_bad_lines="skip")

# ✅ Remove extra spaces from column names
df.columns = df.columns.str.strip()

# ✅ Fix Date format from MM/DD/YYYY to YYYY-MM-DD
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y", errors="coerce")

# ✅ Drop invalid dates
df = df.dropna()

# ✅ Save back to CSV in correct format
df.to_csv("mood_log.csv", index=False, encoding="utf-8")

print("✅ Mood log fixed successfully!")
