import streamlit as st
import pandas as pd
import numpy as np

def zero_one_knap(max_weight):
    zo_col1, zo_col2 = st.columns([1,1],gap="large")
    with zo_col1.container(height=620,border=False).form("zo"):
        c1,c2=st.columns([1,1])
        zo_ham_w = c1.number_input("Hammer Weight",min_value=0,max_value=max_weight)
        zo_ham_v = c2.number_input("Hammer Value",min_value=0,max_value=40)

        zo_scr_w = c1.number_input("Screw Weight",min_value=0,max_value=max_weight)
        zo_scr_v = c2.number_input("Screw Value",min_value=0,max_value=40)

        zo_tow_w = c1.number_input("Towel Weight",min_value=0,max_value=max_weight)
        zo_tow_v = c2.number_input("Towel Value",min_value=0,max_value=40)

        zo_wre_w = c1.number_input("Wrench Weight",min_value=0,max_value=max_weight)
        zo_wre_v = c2.number_input("Wrench Value",min_value=0,max_value=40)

        zo_sd_w = c1.number_input("Screwdriver Weight",min_value=0,max_value=max_weight)
        zo_sd_v = c2.number_input("Screwdriver Value",min_value=0,max_value=40)
        st.caption("""<div style="text-align:center">
                    <p>Click submit to calculate the best case</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        zo_submit = co2.form_submit_button("submit",use_container_width=True)

    with zo_col2.container(height=620,border=False):
        if zo_submit:
            st.title("Visualization")

def Unbound_knap(max_weight):
    unb_col1, unb_col2 = st.columns([1,1],gap="large")
    with unb_col1.container(height=620,border=False).form("unbound_form"):
        c1,c2=st.columns([1,1])

        unb_ham_w = c1.number_input("Hammer Weight",min_value=0,max_value=max_weight)
        unb_ham_v = c2.number_input("Hammer Value",min_value=0,max_value=40)

        unb_scr_w = c1.number_input("Screw Weight",min_value=0,max_value=max_weight)
        unb_scr_v = c2.number_input("Screw Value",min_value=0,max_value=40)

        unb_tow_w = c1.number_input("Towel Weight",min_value=0,max_value=max_weight)
        unb_tow_v = c2.number_input("Towel Value",min_value=0,max_value=40)

        unb_wre_w = c1.number_input("Wrench Weight",min_value=0,max_value=max_weight)
        unb_wre_v = c2.number_input("Wrench Value",min_value=0,max_value=40)

        unb_sd_w = c1.number_input("Screwdriver Weight",min_value=0,max_value=max_weight)
        unb_sd_v = c2.number_input("Screwdriver Value",min_value=0,max_value=40)
        st.caption("""<div style="text-align:center">
                    <p>Click submit to calculate the best case</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        unb_submit = co2.form_submit_button("submit",use_container_width=True)

    with unb_col2.container(height=620,border=False):
        if unb_submit:
            st.title("Visualization")

def Custom_knap(max_weight):
    cu_col1, cu_col2 = st.columns([1,1],gap="large")
    with cu_col1.container(height=620,border=False).form("Custom_K"):
        c1,c2,c3=st.columns([1,1,1])
        cu_ham_w = c1.number_input("Hammer Weight",min_value=0,max_value=max_weight)
        cu_ham_v = c2.number_input("Hammer Value",min_value=0,max_value=40)
        cu_ham_q = c3.number_input("Hammer Quantity",min_value=0,max_value=15)

        cu_scr_w = c1.number_input("Screw Weight",min_value=0,max_value=max_weight)
        cu_scr_v = c2.number_input("Screw Value",min_value=0,max_value=40)
        cu_scr_q = c3.number_input("Screw Quantity",min_value=0,max_value=15)

        cu_tow_w = c1.number_input("Towel Weight",min_value=0,max_value=max_weight)
        cu_tow_v = c2.number_input("Towel Value",min_value=0,max_value=40)
        cu_tow_q = c3.number_input("Towel Quantity",min_value=0,max_value=15)

        cu_wre_w = c1.number_input("Wrench Weight",min_value=0,max_value=max_weight)
        cu_wre_v = c2.number_input("Wrench Value",min_value=0,max_value=40)
        cu_wre_q = c3.number_input("Wrench Quantity",min_value=0,max_value=15)

        cu_sd_w = c1.number_input("Screwdriver Weight",min_value=0,max_value=max_weight)
        cu_sd_v = c2.number_input("Screwdriver Value",min_value=0,max_value=40)
        cu_sd_q = c3.number_input("Screwdriver Quantity",min_value=0,max_value=15)

        st.caption("""<div style="text-align:center">
                    <p>Click submit to visualize</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        cu_submit = co2.form_submit_button("submit",use_container_width=True)

    with cu_col2.container(height=620,border=False):
        if cu_submit:
            st.title("Visualization")

