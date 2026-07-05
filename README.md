# Fernhill Hotels Analytics Dashboard

## Overview

This project was developed as part of the Quantum Global Forward Deployed Engineer technical assessment.

The objective was to clean and validate a hotel booking dataset, define a Property Health Score, and build an interactive dashboard that answers the following business questions:

- How is each property performing?
- Which booking channels generate the most revenue?
- What is the health score of each property?

The dashboard is built using the cleaned dataset generated during the preprocessing stage and does not rely on the raw data.

---

## Features

The dashboard includes:

- Overall business KPIs
  - Total Revenue
  - Total Bookings
  - Average Stay
  - Cancellation Rate
  - Overall Health Score

- Revenue analysis by property

- Revenue analysis by booking channel

- Property Health Score table

- Property Performance Summary

- Business Insights

- Interactive filters for:
  - Property
  - Booking Channel
  - Booking Status

- Downloadable Property Performance Report

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- NumPy

---

## Project Structure

```
fernhill-dashboard/
│
├── dashboard/
│   ├── app.py
│   ├── styles.css
│   ├── logo.jpg
│   └── background.jpg
│
├── data/
│
├── scripts/
│
├── README.md
├── requirements.txt
├── DECISIONS.md
├── AI-WORKFLOW.md
├── TEST-REPORT.md
└── .gitignore
```

---

## Running the Project

Clone the repository.

```bash
git clone https://github.com/Manoj-0606/fernhill-dashboard.git
```

Move into the project folder.

```bash
cd fernhill-dashboard
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the dashboard.

```bash
streamlit run dashboard/app.py
```

---

## Notes

The dashboard uses only the cleaned dataset produced during preprocessing.

The Property Health Score is a custom metric designed for this assessment and combines revenue, booking volume, average stay, and cancellation rate into a single score to compare overall property performance.

Details about the data cleaning decisions, assumptions, and health score calculation are documented in `DECISIONS.md`.

Information about the use of AI during development is available in `AI-WORKFLOW.md`.

Testing performed on the project is documented in `TEST-REPORT.md`.

---

## Future Improvements

Given additional time, I would extend the project by adding:

- Monthly trend analysis
- Occupancy analysis
- Revenue forecasting
- Natural language dashboard queries
- Live database integration
- PDF report generation

---

## Author

Manoj J

This project was completed as part of the Quantum Global Forward Deployed Engineer technical assessment.