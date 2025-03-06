import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def apply_formula(df, formula):
    try:
        df['Result'] = df.eval(formula)
        return df
    except Exception as e:
        st.error(f"Error in formula: {e}")
        return df

st.title("Financial Data Processor")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Raw Data")
    st.dataframe(df)
    
    formula = st.text_input("Enter Excel-like formula (e.g., 'A + B'):")
    if formula:
        df = apply_formula(df, formula)
        st.write("### Processed Data")
        st.dataframe(df)
    
    st.write("### Data Visualization")
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis column", columns)
    y_axis = st.selectbox("Select Y-axis column", columns)
    
    if st.button("Generate Plot"):
        plt.figure(figsize=(8, 5))
        plt.plot(df[x_axis], df[y_axis], marker='o')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title("Financial Data Visualization")
        st.pyplot(plt)
