import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Treacker")

st. title("Personal Expense Tracker")
if 'expenses' not in st.session_state:
    st. session_state.expenses • pd.DataFrame(columns«['Date','Category','Amount', 'Description' ))
with st. form("expense_form"):
    st. subheader ("Add New Expense")
