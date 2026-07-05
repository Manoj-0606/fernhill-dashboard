import streamlit as st
import pandas as pd
from PIL import Image
import base64
import os
import plotly.express as px
import plotly.graph_objects as go

def format_inr(num):
    num = int(round(num))
    s = str(num)

    if len(s) <= 3:
        return s

    last3 = s[-3:]
    rest = s[:-3]

    while len(rest) > 2:
        last3 = rest[-2:] + "," + last3
        rest = rest[:-2]

    if rest:
        last3 = rest + "," + last3

    return last3


def get_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

st.set_page_config(
    page_title="Fernhill Hotels Dashboard",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

css_path = os.path.join(os.path.dirname(__file__), "styles.css")

with open(css_path) as f:
    css = f.read()

background_path = os.path.join(os.path.dirname(__file__), "background.jpg")

bg = get_base64(background_path)

css = css.replace(
    "BACKGROUND_IMAGE",
    f"data:image/jpg;base64,{bg}"
)

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .main .block-container{
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)

data = pd.read_csv("data/cleaned/cleaned_bookings.csv")
health = pd.read_csv("data/cleaned/property_health_score.csv")


base_dir = os.path.dirname(__file__)

logo = Image.open(os.path.join(base_dir, "logo.jpg"))

st.sidebar.image(logo, width=180)

st.sidebar.markdown(
    """
<div class="logo-title">FERNHILL</div>
<div class="logo-sub">HOTELS</div>
""",
    unsafe_allow_html=True,
)

st.sidebar.markdown("---")

property_filter = st.sidebar.multiselect(
    "Property",
    sorted(data["property"].unique()),
    default=sorted(data["property"].unique())
)

channel_filter = st.sidebar.multiselect(
    "Booking Channel",
    sorted(data["booking_channel"].unique()),
    default=sorted(data["booking_channel"].unique())
)

status_filter = st.sidebar.multiselect(
    "Status",
    sorted(data["status"].unique()),
    default=sorted(data["status"].unique())
)

filtered = data[
    (data["property"].isin(property_filter))
    &
    (data["booking_channel"].isin(channel_filter))
    &
    (data["status"].isin(status_filter))
]

st.markdown(
"""
<div class="main-title">
 Fernhill Hotels
</div>

<div class="sub-title">
Luxury Hotel Performance Dashboard • Quantum Global Assignment
</div>
""",
unsafe_allow_html=True
)

total_revenue = filtered["total_amount_inr"].sum()

total_bookings = len(filtered)

avg_stay = filtered["nights"].mean()

cancel_rate = (
    (filtered["status"] == "Cancelled").sum()
    / total_bookings
) * 100 if total_bookings > 0 else 0

overall_health = health["health_score"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-icon"></div>
        <div class="kpi-title">Revenue</div>
        <div class="kpi-value">₹{format_inr(total_revenue)}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-icon"></div>
        <div class="kpi-title">Bookings</div>
        <div class="kpi-value">{total_bookings}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-icon"></div>
        <div class="kpi-title">Average Stay</div>
        <div class="kpi-value">{avg_stay:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-icon"></div>
        <div class="kpi-title">Cancellation %</div>
        <div class="kpi-value">{cancel_rate:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="kpi-box">
        <div class="kpi-icon"></div>
        <div class="kpi-title">Health Score</div>
        <div class="kpi-value">{overall_health:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

left, right = st.columns(2)

with left:

    st.subheader(" Revenue by Property")

    revenue = (
        filtered.groupby("property")["total_amount_inr"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        revenue,
        x="property",
        y="total_amount_inr",
        color="property",
        text=revenue["total_amount_inr"].apply(lambda x: f"₹{format_inr(x)}"),
        template="plotly_dark"
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Revenue: ₹%{customdata}<extra></extra>",
        customdata=revenue["total_amount_inr"].apply(format_inr)
    )

    fig.update_yaxes(
        tickprefix="₹",
        separatethousands=True
    )


    fig.update_layout(
        height=450,
        showlegend=False,
        margin=dict(l=20,r=20,t=40,b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Revenue by Booking Channel")

    channel = (
        filtered.groupby("booking_channel")["total_amount_inr"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        channel,
        values="total_amount_inr",
        names="booking_channel",
        hole=0.6,
        template="plotly_dark"
    )

    fig2.update_traces(
        textinfo="percent",
        customdata=channel["total_amount_inr"].apply(format_inr),
        hovertemplate="<b>%{label}</b><br>"
                      "Revenue: ₹%{customdata}<br>"
                      "Share: %{percent}<extra></extra>"
    )

    fig2.update_layout(
        height=450,
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    fig2.update_traces(
        textinfo="label+percent",
        textposition="inside"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )


st.markdown("---")

st.subheader(" Health Score by Property")

health_sorted = health.sort_values(
    "health_score",
    ascending=False
)

health_display = health_sorted[
    [
        "property",
        "revenue",
        "bookings",
        "avg_stay",
        "health_score"
    ]
]

health_display = health_display.rename(
    columns={
        "property": "Property",
        "revenue": "Revenue",
        "bookings": "Bookings",
        "avg_stay": "Avg Stay",
        "health_score": "Health Score"
    }
)

health_display["Revenue"] = health_display["Revenue"].apply(
    lambda x: f"₹{format_inr(x)}"
)

health_display["Avg Stay"] = health_display["Avg Stay"].round(2)

st.dataframe(
    health_display,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")
st.subheader(" Property Performance Summary")

summary = (
    filtered.groupby("property")
    .agg(
        Revenue=("total_amount_inr", "sum"),
        Bookings=("booking_id", "count"),
        Avg_Stay=("nights", "mean")
    )
    .reset_index()
)

summary = summary.merge(
    health[["property", "health_score"]],
    on="property",
    how="left"
)

summary["Avg_Stay"] = summary["Avg_Stay"].round(2)

summary = summary.sort_values(
    "health_score",
    ascending=False
)

summary = summary.rename(
    columns={
        "property": "Property",
        "health_score": "Health Score",
        "Avg_Stay": "Avg Stay"
    }
)

summary["Revenue"] = summary["Revenue"].apply(
    lambda x: f"₹{format_inr(x)}"
)

summary_display = summary.copy()


st.dataframe(
    summary_display,
    use_container_width=True,
    hide_index=True
)

# Convert summary to CSV
csv = summary.to_csv(index=False).encode("utf-8")

st.download_button(
    label=" Download Property Performance Report",
    data=csv,
    file_name="Fernhill_Property_Report.csv",
    mime="text/csv"
)


st.markdown("---")
st.subheader(" Business Insights")

if summary.empty:
    st.warning("No data available for the selected filters.")
else:

    best_property = summary.iloc[0]
    lowest_property = summary.iloc[-1]

    channel_summary = (
        filtered.groupby("booking_channel")["total_amount_inr"]
        .sum()
    )

    if not channel_summary.empty:
        best_channel = channel_summary.idxmax()
    else:
        best_channel = "N/A"

st.info(f"""
🏆 **Best Performing Property:** {best_property['Property']}

⚠️ **Needs Attention:** {lowest_property['Property']}

💰 **Best Revenue Channel:** {best_channel}

📉 **Overall Cancellation Rate:** {cancel_rate:.1f}%

These insights are generated from the cleaned dataset and help management identify the best performing properties and channels.
""")
    
st.markdown("---")

st.markdown("""
<hr style="margin-top:40px;margin-bottom:30px;border:1px solid rgba(255,255,255,.1);">

<div class="footer">

<div class="footer-title">
Fernhill Hotels Analytics Dashboard
</div>

<div class="footer-sub">
Built using Python • Streamlit • Plotly
</div>

<div class="footer-note">
Prepared for Quantum Global Technical Assessment
</div>

<div class="footer-note" style="margin-top:12px;">
Created by <span class="footer-name">Manoj J</span>
</div>

</div>
""", unsafe_allow_html=True)