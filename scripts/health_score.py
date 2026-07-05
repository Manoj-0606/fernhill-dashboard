import pandas as pd

df = pd.read_csv("data/cleaned/cleaned_bookings.csv")

property_summary = df.groupby("property").agg(
    revenue=("total_amount_inr", "sum"),
    bookings=("booking_id", "count"),
    cancellations=("status", lambda x: (x == "Cancelled").sum()),
    avg_stay=("nights", "mean")
).reset_index()

property_summary["cancellation_rate"] = (
    property_summary["cancellations"] /
    property_summary["bookings"]
) * 100

property_summary["revenue_score"] = (
    property_summary["revenue"] /
    property_summary["revenue"].max()
) * 100

property_summary["booking_score"] = (
    property_summary["bookings"] /
    property_summary["bookings"].max()
) * 100

property_summary["stay_score"] = (
    property_summary["avg_stay"] /
    property_summary["avg_stay"].max()
) * 100

property_summary["cancellation_score"] = (
    100 - property_summary["cancellation_rate"]
)

property_summary["health_score"] = (
    property_summary["revenue_score"] * 0.40 +
    property_summary["booking_score"] * 0.30 +
    property_summary["cancellation_score"] * 0.20 +
    property_summary["stay_score"] * 0.10
)

property_summary["health_score"] = property_summary["health_score"].round(2)

property_summary = property_summary.sort_values(
    by="health_score",
    ascending=False
)

print(property_summary)

property_summary.to_csv(
    "data/cleaned/property_health_score.csv",
    index=False
)

print("\nHealth score calculated successfully.")