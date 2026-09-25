import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Analysis Dashboard")

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

data = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{data['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"₹{data['Profit'].sum():,.0f}")
col3.metric("Total Orders", len(data))

st.subheader("Sales by Category")

category_sales = data.groupby("Category")["Sales"].sum().reset_index()

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sales by Region")

region_sales = data.groupby("Region")["Sales"].sum().reset_index()

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("Sales Trend")

fig3 = px.line(
    data,
    x="Date",
    y="Sales",
    title="Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader("Sales Data")

st.dataframe(data)