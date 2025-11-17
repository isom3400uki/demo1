import streamlit as st

st.set_page_config(page_title="Retail Business Dashboard", page_icon="📊", layout="centered")

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and select the region.")

sales_target = st.number_input("Enter Monthly Sales Target (in USD):", min_value=0, max_value=100000, value=50000)
region = st.selectbox("Select Region:", ["North", "South", "East", "West"])

submitted = st.button("Submit")

if submitted:
    st.write("### Summary")
    st.write(f"- **Sales Target:** ${sales_target:,.0f}")
    st.write(f"- **Region:** {region}")
    st.success("Dashboard updated successfully!")
