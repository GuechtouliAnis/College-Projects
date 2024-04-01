import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Int_funcs as ins

st.set_page_config("Knapsack",page_icon="Optimisation/icons/backpack.png",layout="wide")

tab1, tab2 = st.tabs(["0/1 Knapsack", "Unbound Knapsack"])

knap_dict = {"Tools":["Hammer","Screw","Towel","Wrench","Screwdriver"]}
df = pd.DataFrame(knap_dict)

with tab1:
    ins.zero_one_knap(knap_dict)
with tab2:
    ins.Unbound_knap()
