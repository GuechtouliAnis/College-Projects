import streamlit as st
import pandas as pd
import altair as alt

# Load data
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

# Title and description
st.title("Tips dataset")
st.markdown("This dashboard shows the tips dataset from the seaborn library.")

# Histogram of tips by day
hist_values = data["tip"].groupby(data["day"]).sum()
st.bar_chart(hist_values)

# Scatter plot of tips vs. total bill
scatter_data = alt.Chart(data).mark_circle().encode(
    x='total_bill',
    y='tip',
    color='day',
    tooltip=['total_bill', 'tip', 'day']
).properties(
    width=800,
    height=400
).interactive()
st.altair_chart(scatter_data)

# Box plot of tips by time and sex
box_data = data[['tip', 'time', 'sex']]
box_plot = alt.Chart(box_data).mark_boxplot().encode(
    x='time',
    y='tip',
    color='sex'
).properties(
    width=800,
    height=400
).interactive()
st.altair_chart(box_plot)
