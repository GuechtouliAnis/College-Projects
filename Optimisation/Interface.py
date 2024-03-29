import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Int01 as ins

st.set_page_config("Knapsack",page_icon=None,layout="wide")

tab1, tab2, tab3 = st.tabs(["0/1 Knapsack", "Unbound Knapsack","Custom"])

with tab1:
    ins.zero_one_knap(15)
with tab2:
    ins.Unbound_knap(15)
with tab3:
    ins.Custom_knap(15)
