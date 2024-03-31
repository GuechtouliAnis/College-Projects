import streamlit as st
import pandas as pd
import numpy as np


def gen_cases(size):
    cases = []
    for i in range(size):
        binary_string = bin(i)
        binary_string_without_prefix = binary_string[2:]
        cases.append(binary_string_without_prefix)
    for pos in range(len(cases)):
        length = len(cases[-1]) - len(cases[pos])
        if length !=0:
            for i in range(length):
                cases[pos] = "0"+cases[pos]
        else:
            break
    return cases

def zo(df_01,sack_size):
    size = 2 ** len(df_01.columns)
    cases = gen_cases(size)
    cpt = 1
    for poss in cases:
        f = []
        for n in poss:
            f.append(int(n))
            s = str(cpt)
        df_01.loc["pos"+s]=f
        cpt +=1
    sums = [df_01.loc['values'].sum(),df_01.loc['weights'].sum()]
    weight = [df_01.loc['values'].sum(),df_01.loc['weights'].sum()]
    for i in range(1,len(df_01)-1):
        s = 0
        w = 0
        for col in df_01.columns:
            s += df_01.loc['pos'+str(i),col] * df_01.loc['values',col]
            w += df_01.loc['pos'+str(i),col] * df_01.loc['weights',col]
        sums.append(s)
        weight.append(w)
    df_01['Total Values'] = sums
    df_01['Total Weights'] = weight
    dfs_01 = df_01.drop(["values","weights"])
    dfs_01 = dfs_01[dfs_01["Total Weights"]<= sack_size]
    order = ["Total Values","Total Weights"]
    asc = [False,True]
    dfs_01=dfs_01.sort_values(by=order,ascending=asc).head()
    return dfs_01

def visuals(dfs_01):
    im1,im2,im3,im4,im5=st.columns([1,1,1,1,1])
    if "Hammer" in dfs_01:
        if dfs_01.iloc[0]["Hammer"]>0:
            im1.image("Optimisation/icons/on_Hammer.png")
            im1.caption("""<div style="text-align:center"><H1 style="color:#00ff00;">1</H1></div>""", unsafe_allow_html=True)
        else:
            im1.image("Optimisation/icons/off_Hammer.png")
            im1.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    else:
        im1.image("Optimisation/icons/off_Hammer.png")
        im1.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    if "Screw" in dfs_01:
        if dfs_01.iloc[0]["Screw"]>0:
            im2.image("Optimisation/icons/on_Screw.png")
            im2.caption("""<div style="text-align:center"><H1 style="color:#00ff00;">1</H1></div>""", unsafe_allow_html=True)
        else:
            im2.image("Optimisation/icons/off_Screw.png")
            im2.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    else:
        im2.image("Optimisation/icons/off_Screw.png")
        im2.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    if "Towel" in dfs_01:
        if dfs_01.iloc[0]["Towel"]>0:
            im3.image("Optimisation/icons/on_Towel.png")
            im3.caption("""<div style="text-align:center"><H1 style="color:#00ff00;">1</H1></div>""", unsafe_allow_html=True)
        else:
            im3.image("Optimisation/icons/off_Towel.png")
            im3.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)    
    else:
        im3.image("Optimisation/icons/off_Towel.png")
        im3.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    if "Wrench" in dfs_01:
        if dfs_01.iloc[0]["Wrench"]>0:
            im4.image("Optimisation/icons/on_Wrench.png")
            im4.caption("""<div style="text-align:center"><H1 style="color:#00ff00;">1</H1></div>""", unsafe_allow_html=True)
        else:
            im4.image("Optimisation/icons/off_Wrench.png")
            im4.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    else:
        im4.image("Optimisation/icons/off_Wrench.png")
        im4.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    if "Screwdriver" in dfs_01:
        if dfs_01.iloc[0]["Screwdriver"]>0:
            im5.image("Optimisation/icons/on_Screwdriver.png")
            im5.caption("""<div style="text-align:center"><H1 style="color:#00ff00;">1</H1></div>""", unsafe_allow_html=True)
        else:
            im5.image("Optimisation/icons/off_Screwdriver.png")
            im5.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)
    else:
            im5.image("Optimisation/icons/off_Screwdriver.png")
            im5.caption(f"""<div style="text-align:center"><H1>0</H1></div>""", unsafe_allow_html=True)

def zero_one_knap(kd):
    weights = []
    values = []
    zo_col1, zo_col2 = st.columns([1,1])
    with zo_col1.container(height=620,border=True).form("zero_one",border=False):
        c1,c2=st.columns([1,1])

        values.append(c1.number_input("Hammer Value",min_value=0,max_value=40,value=11))
        values.append(c1.number_input("Screw Value",min_value=0,max_value=40,value=4))
        values.append(c1.number_input("Towel Value",min_value=0,max_value=40,value=8))
        values.append(c1.number_input("Wrench Value",min_value=0,max_value=40,value=3))
        values.append(c1.number_input("Screwdriver Value",min_value=0,max_value=40,value=6))

        weights.append(c2.number_input("Hammer Weight",min_value=0,max_value=100,value=3))
        weights.append(c2.number_input("Screw Weight",min_value=0,max_value=100,value=2))
        weights.append(c2.number_input("Towel Weight",min_value=0,max_value=100,value=5))
        weights.append(c2.number_input("Wrench Weight",min_value=0,max_value=100,value=7))
        weights.append(c2.number_input("Screwdriver Weight",min_value=0,max_value=100,value=4))

        sack_size = st.number_input("Enter sack size",min_value=1,max_value=100,value=15)
        st.caption("""<div style="text-align:center">
                    <p>Click submit to calculate the best case</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        zo_submit = co2.form_submit_button("submit",use_container_width=True)

    torem = []
    for j in range(len(weights)):
        if weights[j] == 0 or values[j] == 0 or weights[j]>sack_size:
            torem.append(j)
    hea = 5
    if len(torem) <5:
        p = 0
        for s in torem:
            weights.pop(s-p)
            values.pop(s-p)
            kd['Tools'].pop(s-p)
            p +=1
    else:
        hea = 1
    kd["weights"] = weights
    kd["values"] = values

    kd = pd.DataFrame(kd,index=kd['Tools'])
    kd.drop('Tools', axis=1, inplace=True)
    df_01 = kd.transpose().copy()
    dfs_01 = zo(df_01,sack_size)    

    with zo_col2.container(height=620):
        if hea ==1:
            st.error("All weights (and/or) values are null or larger than the sack's size, re-enter acceptable values")
        else:
            st.dataframe(dfs_01,use_container_width=True)
            visuals(dfs_01)
            max_value = dfs_01['Total Values'].max()
            count_max_value = dfs_01['Total Values'].eq(max_value).sum()
            if count_max_value == 1:
                st.write(f"""<div style="text-align:center">
                    <p>There is only {count_max_value} optimal solution.</p>
                    </div>""", unsafe_allow_html=True)
            else:
                st.write(f"""<div style="text-align:center">
                    <p>There are {count_max_value} optimal solutions, the visualization shows one of them.</p>
                    </div>""", unsafe_allow_html=True)

def Unbound_knap():
    unb_col1, unb_col2 = st.columns([1,1],gap="large")
    with unb_col1.container(height=620,border=False).form("unbound_form"):
        c1,c2=st.columns([1,1])

        unb_ham_w = c1.number_input("Hammer Weight",min_value=0,max_value=100)
        unb_ham_v = c2.number_input("Hammer Value",min_value=0,max_value=40)

        unb_scr_w = c1.number_input("Screw Weight",min_value=0,max_value=100)
        unb_scr_v = c2.number_input("Screw Value",min_value=0,max_value=40)

        unb_tow_w = c1.number_input("Towel Weight",min_value=0,max_value=100)
        unb_tow_v = c2.number_input("Towel Value",min_value=0,max_value=40)

        unb_wre_w = c1.number_input("Wrench Weight",min_value=0,max_value=100)
        unb_wre_v = c2.number_input("Wrench Value",min_value=0,max_value=40)

        unb_sd_w = c1.number_input("Screwdriver Weight",min_value=0,max_value=100)
        unb_sd_v = c2.number_input("Screwdriver Value",min_value=0,max_value=40)
        unb_sack_weight = st.number_input("Enter sack size",min_value=1,max_value=100)

        st.caption("""<div style="text-align:center">
                    <p>Click submit to calculate the best case</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        unb_submit = co2.form_submit_button("submit",use_container_width=True)

    with unb_col2.container(height=620,border=False):
        if unb_submit:
            st.title("Visualization")

def Custom_knap():
    cu_col1, cu_col2 = st.columns([1,1],gap="large")
    with cu_col1.container(height=620,border=False).form("Custom_K"):
        c1,c2,c3=st.columns([1,1,1])
        cu_ham_w = c1.number_input("Hammer Weight",min_value=0,max_value=100)
        cu_ham_v = c2.number_input("Hammer Value",min_value=0,max_value=40)
        cu_ham_q = c3.number_input("Hammer Quantity",min_value=0,max_value=15)

        cu_scr_w = c1.number_input("Screw Weight",min_value=0,max_value=100)
        cu_scr_v = c2.number_input("Screw Value",min_value=0,max_value=40)
        cu_scr_q = c3.number_input("Screw Quantity",min_value=0,max_value=15)

        cu_tow_w = c1.number_input("Towel Weight",min_value=0,max_value=100)
        cu_tow_v = c2.number_input("Towel Value",min_value=0,max_value=40)
        cu_tow_q = c3.number_input("Towel Quantity",min_value=0,max_value=15)

        cu_wre_w = c1.number_input("Wrench Weight",min_value=0,max_value=100)
        cu_wre_v = c2.number_input("Wrench Value",min_value=0,max_value=40)
        cu_wre_q = c3.number_input("Wrench Quantity",min_value=0,max_value=15)

        cu_sd_w = c1.number_input("Screwdriver Weight",min_value=0,max_value=100)
        cu_sd_v = c2.number_input("Screwdriver Value",min_value=0,max_value=40)
        cu_sd_q = c3.number_input("Screwdriver Quantity",min_value=0,max_value=15)

        cu_sack_weight = st.number_input("Enter sack size",min_value=1,max_value=100)

        st.caption("""<div style="text-align:center">
                    <p>Click submit to visualize</p>
                    </div>""", unsafe_allow_html=True)
        co1,co2,co3 = st.columns([1.5,1,1.5])
        cu_submit = co2.form_submit_button("submit",use_container_width=True)

    with cu_col2.container(height=620,border=False):
        if cu_submit:
            st.title("Visualization")