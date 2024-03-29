import pandas as pd
import numpy as np
import streamlit as st
from itertools import product
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(layout="wide")

Backpack_size = 15
d = {"Hammer":{ "status":False,    "Value":11,    "Weight":3},
     "Screw" :{ "status":False,    "Value":4,    "Weight":2},
     "Towel" :{ "status":False,    "Value":8,    "Weight":5},
     "Wrench":{ "status":False,    "Value":3,    "Weight":7},
     "Screwdriver":{ "status":False,    "Value":6,    "Weight":4}
    }


col1,col2 = st.columns([1,1])


with col1:
    st.title("Items")
    st.write(" ")
    d["Hammer"]["status"] = st.checkbox("Hammer")
    st.text("Value = 11 - Weight = 3")
    d["Screw"]["status"]  = st.checkbox("Screw")
    st.text("Value = 4  - Weight = 2")
    d["Towel"]["status"]  = st.checkbox("Towel")
    st.text("Value = 8  - Weight = 5")
    d["Wrench"]["status"] = st.checkbox("Wrench")
    st.text("Value = 3  - Weight = 7")
    d["Screwdriver"]["status"] = st.checkbox("Screwdriver")
    st.text("Value = 6 -  Weight = 4")

st.sidebar.write("a")

with col2:
    st.title("Pie Chart")
    # Create DataFrame from dictionary d
    selected_items = {k: v for k, v in d.items()}
    df = pd.DataFrame(selected_items).T.reset_index()

    # Calculate total weight and value of selected items
    total_weight = df[df["status"] == True]["Weight"].sum()
    total_value = df[df["status"] == True]["Value"].sum()
    # Calculate remaining empty space in the backpack
    remaining_space = Backpack_size - total_weight

    # Create labels and values for the pie chart
    labels = ["Selected Items", "Empty Space"]
    values = [total_weight, remaining_space]

    # Set the figure size
    fig, ax = plt.subplots(figsize=(9, 6))  # Adjust the size as needed

    # Create a pie chart
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the figure
    st.pyplot(fig)

    emp = 15
    total_val = 0
    for i in df.index:  # Access the index directly
        if df.loc[i, 'status']:
            emp -= int(df.loc[i, 'Weight'])  # Use .loc to access DataFrame values
            total_val += int(df.loc[i, 'Value'])  # Use .loc to access DataFrame values
    c1,c2 = st.columns([1,1])
    with c1:
        st.write("weight: ", str(emp))
    with c2:
        st.write("total val: ", str(total_val))

