import streamlit as st

# -------------------------------
# 1. Dashboard Title and Objective
# -------------------------------
st.title("Business Performance Dashboard")
msg = " ## Objective: This dashboard provides insights into revenue, customer feedback, and market trends for better business decisions."
st.write(msg)
#markdown(#) sth that u wanna format the text

# -------------------------------
# 2. Columns Layout for Quarterly Revenue
# -------------------------------
st.subheader("Quarterly Revenue Overview")
col1, col2, col3 = st.columns(3)

# if u have 3 columns then 3

with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")

# -------------------------------
# 3. Tabs for Different Business Sections
# -------------------------------
tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])

with tab1:
    st.write("### Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    # q1 2024 is key 1.2m is value
    # .item can extract both
    # .item fstring,forloop, dictionary
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
    st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]}, height=200)

with tab2:
    st.write("### Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
          # markdown(-) its bullet point
    for idx, feedback in enumerate(customer_feedback, start=1):
        st.write(f"{idx}. {feedback}")
        # want 1., 2. 
      

with tab3:
    st.write("### Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")

# -------------------------------
# 4. Expander for Additional Information
# -------------------------------
with st.expander("More Information"):
    st.write("Data was collected through surveys, customer feedback forms, and official sales reports.")

# -------------------------------
# 5. Add Interactivity
# -------------------------------
st.subheader("Interactive Revenue Checker")
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
selected_quarter = st.selectbox("Select a quarter:", quarters)

# Display revenue dynamically
st.write(f"Revenue for {selected_quarter}: {sales_data[selected_quarter]}")

# Bonus: Growth adjustment
growth = st.slider("Adjust growth percentage:", 0, 50, 10)
base_revenue = float(sales_data[selected_quarter].strip("$M"))
adjusted_revenue = base_revenue * (1 + growth / 100)
st.write(f"Adjusted Revenue for {selected_quarter}: ${adjusted_revenue:.2f}M")

# -------------------------------
# 6. Motivational Button
# -------------------------------
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
