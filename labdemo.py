import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Personal Expense Treacker")

if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns= ['Date','Category','Amount', 'Description'])
    
with st. form("expense_form"):
    st.subheader ("Add New Expense")
    date = st.date_input("Date")
    category = st.selectbox(

submitted = st.form_submit_button("Add Expense")
if submitted:
    new_expense = pd.DataFrame({
        'Date': [Date],
        'Category': [Category],
        'Amount': [Amount],
        'Description': [\Desription]
    })
    st.session_state.expenses = pd. concat([st.session_state.expenses, new_expense], ignore_index=True)
    st.success("Expense added successfully!")

if not st.session_state.expense.empty
    st.subheader("Your Expenses")
    st.dataframe(st.session_state.expenses)

    st.subheader("Summary")
    total_spent = st.session_state.expense['Amount'].sum()
    st.write(f"Total Spent: ${total_spent:.2f}")

    category_totals = st.session_state.expense.groupby('Category')[Amount].sum()
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.pie(category_totals.values, labels=category_totals.index, autopct= '
else:
    st.info("No expenses recorded yet")
