import streamlit as st
import Int_funcs as ins

st.set_page_config("Knapsack",page_icon="Optimisation/icons/backpack.png",layout="wide")

tab0,tab1, tab2 = st.tabs(["Knapsack","0/1 Knapsack", "Unbound Knapsack"])

knap_dict0 = {"Tools":["Hammer","Screw","Towel","Wrench","Screwdriver"]}
knap_dict1 = {"Tools":["Hammer","Screw","Towel","Wrench","Screwdriver"]}
knap_dict2 = {"Tools":["Hammer","Screw","Towel","Wrench","Screwdriver"]}

with tab0:
    ins.knapsack_int(knap_dict0)
with tab1:
    ins.zero_one_knap(knap_dict1)
with tab2:
    ins.Unbound_knap(knap_dict2)
