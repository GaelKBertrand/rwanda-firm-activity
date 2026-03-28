import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/kigali_firms_clean.csv")

st.title("Rwanda Firm Activity Tracker")

st.write(df.head())

st.subheader("Firm Types Distribution")
st.bar_chart(df["type"].value_counts())

#to run:
#pip install streamlit
#streamlit run app/app.py