import pandas as pd

df = pd.read_csv("data/raw/bookings_jan_may_2026.csv")

print("Original Shape:", df.shape)

print("Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

df["property"] = df["property"].str.strip().str.title()

df["booking_channel"] = df["booking_channel"].str.strip().str.title()

df["booking_channel"] = df["booking_channel"].replace({
    "Ota-Mmt": "OTA-MMT",
    "Ota-Booking": "OTA-Booking",
    "Walk-In": "Walk-in"
})

df["status"] = df["status"].str.strip().replace({
    "confirmed": "Confirmed",
    "CHECKED OUT": "Checked-out",
    "Checked-Out": "Checked-out",
    "checked-out": "Checked-out",
    "No-Show": "No-show",
    "no-show": "No-show"
})

missing_channel = df["booking_channel"].isna().sum()
df["booking_channel"] = df["booking_channel"].fillna("Unknown")
print("Missing Booking Channels Filled:", missing_channel)

missing_rate = df["nightly_rate_inr"].isna().sum()

df["nightly_rate_inr"] = df.groupby("room_type")["nightly_rate_inr"].transform(
    lambda x: x.fillna(x.median())
)

print("Missing Nightly Rates Filled:", missing_rate)

expected_total = df["nightly_rate_inr"] * df["nights"]

wrong_total = (
    df["total_amount_inr"].isna() |
    (df["total_amount_inr"] != expected_total)
)

print("Incorrect Total Amount Fixed:", wrong_total.sum())

df.loc[wrong_total, "total_amount_inr"] = expected_total[wrong_total]

removed_nights = (df["nights"] <= 0).sum()
print("Rows Removed (Invalid Nights):", removed_nights)
df = df[df["nights"] > 0]

removed_rate = (df["nightly_rate_inr"] <= 0).sum()
print("Rows Removed (Invalid Nightly Rate):", removed_rate)
df = df[df["nightly_rate_inr"] > 0]

removed_total = (df["total_amount_inr"] <= 0).sum()
print("Rows Removed (Invalid Total Amount):", removed_total)
df = df[df["total_amount_inr"] > 0]

df["check_in_date"] = pd.to_datetime(
    df["check_in_date"],
    format="mixed",
    errors="coerce"
)

print("Invalid Dates:", df["check_in_date"].isna().sum())

df["check_in_date"] = df["check_in_date"].dt.strftime("%Y-%m-%d")

print("Final Shape:", df.shape)

df.to_csv("data/cleaned/cleaned_bookings.csv", index=False)

print("\nCleaned dataset saved successfully.")

print("\nCleaning Summary")
print("-" * 40)
print(f"Original Rows : 238")
print(f"Cleaned Rows  : {len(df)}")
print(f"Rows Removed  : {238 - len(df)}")
print(f"Properties    : {df['property'].nunique()}")
print(f"Channels      : {df['booking_channel'].nunique()}")
print(f"Statuses      : {df['status'].nunique()}")