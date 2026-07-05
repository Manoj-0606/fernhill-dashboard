import pandas as pd

df = pd.read_csv("data/raw/bookings_jan_may_2026.csv")

print(df.shape)
print()

print(df.info())
print()

print(df.isnull().sum())
print()

print("Duplicate Rows:", df.duplicated().sum())
print()

print("Duplicate Booking IDs:")
print(df[df["booking_id"].duplicated(keep=False)])
print()

print("Properties")
print(df["property"].value_counts(dropna=False))
print()

print("Booking Channels")
print(df["booking_channel"].value_counts(dropna=False))
print()

print("Status")
print(df["status"].value_counts(dropna=False))
print()

print("Nights")
print(df["nights"].describe())
print()

print(df[df["nights"] <= 0])
print()

print("Guests")
print(df["guests"].describe())
print()

print(df[df["guests"] <= 0])
print()

print("Nightly Rate")
print(df["nightly_rate_inr"].describe())
print()

print(df[df["nightly_rate_inr"] < 0])
print()

print("Total Amount")
print(df["total_amount_inr"].describe())
print()

print(df[df["total_amount_inr"] < 0])
print()

expected = df["nightly_rate_inr"] * df["nights"]

wrong_total = df[
    (df["nightly_rate_inr"].notna()) &
    (df["total_amount_inr"].notna()) &
    (expected != df["total_amount_inr"])
]

print("Rows with wrong total amount")
print(wrong_total[["booking_id", "nightly_rate_inr", "nights", "total_amount_inr"]])
print()

dates = pd.to_datetime(df["check_in_date"], errors="coerce", dayfirst=True)

print("Invalid Dates:", dates.isna().sum())
print(df[dates.isna()])