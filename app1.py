import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Market Intelligence Tool",
    page_icon="📊",
    layout="wide"
)

# ---------------- BACKGROUND COLOR ----------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f6f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center; color:#1f4ed8;'>AI Market Intelligence Tool</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:gray;'>Market Trend Analysis using Data Science</p>",
    unsafe_allow_html=True
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("C:/Users/radha/OneDrive/Desktop/MarketProject/data.csv.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# ---------------- DATASET PREVIEW ----------------
st.markdown("<h3 style='color:#0f766e;'>📂 Dataset Preview</h3>", unsafe_allow_html=True)
st.dataframe(df.head())

# ---------------- KPI SECTION ----------------
total_orders = df["Order_ID"].nunique()
total_regions = df["Region"].nunique()
total_states = df["State"].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"<div style='background:#e0f2fe; padding:20px; border-radius:10px; text-align:center;'>"
        f"<h2 style='color:#0369a1;'>{total_orders}</h2>"
        f"<p>Total Orders</p></div>",
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"<div style='background:#dcfce7; padding:20px; border-radius:10px; text-align:center;'>"
        f"<h2 style='color:#166534;'>{total_regions}</h2>"
        f"<p>Total Regions</p></div>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"<div style='background:#fef9c3; padding:20px; border-radius:10px; text-align:center;'>"
        f"<h2 style='color:#854d0e;'>{total_states}</h2>"
        f"<p>Total States</p></div>",
        unsafe_allow_html=True
    )

# ---------------- ORDERS OVER TIME ----------------
st.markdown("<h3 style='color:#6d28d9;'>📈 Orders Over Time</h3>", unsafe_allow_html=True)

daily_orders = df.groupby("Order_Date")["Order_ID"].count()
st.line_chart(daily_orders)

# ---------------- REGION-WISE ANALYSIS ----------------
st.markdown("<h3 style='color:#b91c1c;'>🌍 Region-wise Orders</h3>", unsafe_allow_html=True)

region_orders = df["Region"].value_counts()
st.bar_chart(region_orders)

# ---------------- FOOTER ----------------
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>"
    "AI Market Intelligence Tool | Data Science Project</p>",
    unsafe_allow_html=True
)