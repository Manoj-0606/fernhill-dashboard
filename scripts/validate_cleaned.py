import pandas as pd

df = pd.read_csv("data/cleaned/cleaned_bookings.csv")

print("Shape:", df.shape)
print()

print("Missing Values")
print(df.isnull().sum())
print()

print("Duplicate Rows:", df.duplicated().sum())
print()

print("Duplicate Booking IDs:", df["booking_id"].duplicated().sum())
print()

print("Properties")
print(sorted(df["property"].unique()))
print()

print("Booking Channels")
print(sorted(df["booking_channel"].unique()))
print()

print("Status")
print(sorted(df["status"].unique()))
print()

print("Negative Total Amount:", (df["total_amount_inr"] < 0).sum())
print("Zero Nights:", (df["nights"] <= 0).sum())

expected = df["nightly_rate_inr"] * df["nights"]

print("Revenue Mismatch:",
      (expected != df["total_amount_inr"]).sum())