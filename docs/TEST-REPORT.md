# TEST REPORT

## Objective

The goal of testing was to make sure the cleaned dataset, health score calculation and dashboard were working correctly before deployment.

I tested the complete workflow starting from the cleaned CSV file through to the final Streamlit dashboard.

---

## Environment

- OS: Windows 11
- IDE: Visual Studio Code
- Python: 3.x
- Dashboard: Streamlit
- Libraries: Pandas, Plotly, Pillow

---

## What I Tested

### 1. Data Loading

Verified that the dashboard loads the cleaned dataset successfully without using the raw dataset.

**Result:** Passed

---

### 2. Dashboard Launch

Started the dashboard using:

```bash
streamlit run dashboard/app.py
```

The application loaded successfully without any runtime errors.

**Result:** Passed

---

### 3. KPI Cards

Checked that the dashboard correctly displays:

- Total Revenue
- Total Bookings
- Average Stay
- Cancellation Percentage
- Overall Health Score

I manually compared these values with the cleaned dataset.

**Result:** Passed

---

### 4. Revenue by Property

Verified that revenue for every property matches the cleaned dataset after filtering.

The chart updates correctly whenever filters are changed.

**Result:** Passed

---

### 5. Booking Channel Analysis

Checked that revenue is grouped correctly by booking channel.

I also verified that standardised channel names (Direct, OTA-MMT, Corporate, Walk-in, Unknown) appear correctly.

**Result:** Passed

---

### 6. Health Score

Compared the Health Score table with the generated health score CSV to ensure values were displayed correctly.

The ranking of properties also matched the calculated scores.

**Result:** Passed

---

### 7. Filters

Tested all dashboard filters.

- Property
- Booking Channel
- Booking Status

Each filter updated all KPIs, charts and tables correctly.

I also tested multiple filter combinations.

**Result:** Passed

---

### 8. Empty Results

I tested cases where the selected filters returned no matching records.

Instead of crashing, the dashboard displays a message indicating that no data is available.

**Result:** Passed

---

### 9. Download Report

Verified that the Property Performance Summary can be downloaded successfully as a CSV file.

Downloaded data matched the values shown in the dashboard.

**Result:** Passed

---

## Manual Validation

After the dashboard was complete, I manually verified a few important calculations.

- Revenue totals
- Booking counts
- Average stay
- Cancellation percentage
- Property Health Score

The displayed values matched the cleaned dataset.

---

## Limitations

This project uses a CSV file as its data source.

With more time, I would connect the dashboard to a live database so that metrics update automatically as new bookings are added.

I would also extend the dashboard with occupancy trends and revenue forecasting.

---

## Final Result

After testing, the dashboard was able to answer all three client questions:

- How each property is performing.
- Which booking channels generate the most value.
- The Health Score of every property.

The dashboard runs using only the cleaned dataset and all tested functionality worked as expected.