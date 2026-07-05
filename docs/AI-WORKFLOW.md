# AI-WORKFLOW.md

# AI Workflow

## Overview

AI was used throughout this assignment as a productivity tool rather than as a replacement for engineering judgement.

I used AI to speed up repetitive coding tasks, brainstorm implementation approaches, review code, and improve the dashboard UI. Every AI-generated suggestion was manually reviewed before being added to the project.

Whenever AI suggestions conflicted with the actual dataset or produced incorrect logic, I verified the results against the data and corrected them.

---

# AI Tools Used

During this project I primarily used:

- ChatGPT (GPT-5.5)
    - Python code generation
    - Data cleaning logic
    - Streamlit dashboard development
    - Plotly visualisations
    - Documentation review

- VS Code
    - Development
    - Debugging
    - Running scripts
    - Testing

---

# Where AI Helped

## Dataset Audit

AI helped generate an initial audit script that checked:

- Missing values
- Duplicate rows
- Duplicate Booking IDs
- Invalid revenue
- Date formats
- Numerical outliers

I then reviewed the audit output manually to identify the actual issues present in the dataset.

---

## Data Cleaning

AI suggested approaches for:

- Standardising categorical values
- Removing duplicate records
- Revenue validation
- Date parsing
- Missing value handling

I modified the cleaning logic where necessary based on the audit findings rather than accepting every suggestion directly.

---

## Dashboard Development

AI helped generate:

- Streamlit layout
- Plotly charts
- KPI cards
- CSS styling
- Business insight section
- Download report functionality

The final dashboard layout and visualisations were refined manually.

---

# Example Prompts

## Prompt 1

"Audit this hotel booking dataset and identify all possible data quality issues before cleaning."

Result:

Generated an audit script that highlighted missing values, duplicate records, inconsistent categories and revenue validation checks.

---

## Prompt 2

"Create a Streamlit dashboard that answers these three business questions:
How is each property performing?
Which booking channels are most valuable?
What is the health score of each property?"

Result:

Produced the initial dashboard layout, which I later customised with additional KPIs, charts and business insights.

---

## Prompt 3

"Help improve the dashboard UI using custom CSS while keeping the code maintainable."

Result:

Generated glassmorphism-inspired KPI cards, improved layout spacing and sidebar styling.

---

# Example of AI Making a Mistake

One example occurred while building the Property Performance Summary.

AI initially suggested sorting the dataframe using:

summary.sort_values("Health Score")

However, the dataframe still contained the original column name:

health_score

This caused a KeyError during execution.

Instead of accepting the generated code, I inspected the dataframe, identified the incorrect column reference and corrected the sorting logic before renaming the column.

This reinforced the importance of validating AI-generated code rather than assuming it is always correct.

---

# Validation Process

Every AI-generated suggestion was verified by:

- Running the code locally
- Comparing calculations against the cleaned dataset
- Checking dashboard outputs manually
- Testing filters
- Verifying revenue calculations
- Confirming Health Score values

Only validated code was included in the final solution.

---

# Reflection

AI significantly reduced development time by generating boilerplate code and suggesting implementation ideas.

However, the correctness of the final solution depended on manually auditing the dataset, validating every important calculation and correcting AI-generated mistakes when they occurred.

Throughout the project, AI was used as an engineering assistant rather than as an autonomous developer.