import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ensure streamlit is available (to avoid ModuleNotFoundError)
try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("The 'streamlit' module is not installed. Install it using 'pip install streamlit'.")

# Sample Data Preparation (Replace this with your actual dataset)
data = {
    "Market": ["Market A", "Market B", "Market C"] * 50,
    "CompanyCode": [f"C{i}" for i in range(1, 51)] * 3,
    "Price": np.random.uniform(0, 100, 150),
}
df = pd.DataFrame(data)

def plot_price_clustering(selected_market, company_code):
    """Filter data based on market and company code, then plot price clustering."""
    filtered_data = df[(df["Market"] == selected_market)]
    if company_code:
        filtered_data = filtered_data[filtered_data["CompanyCode"] == company_code]

    if filtered_data.empty:
        st.warning("No data available for the selected market and company code.")
        return

    # Create histogram for price clustering
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data["Price"], bins=20, color="skyblue", edgecolor="black")
    plt.title(f"Price Clustering in {selected_market}" + (f" (Company: {company_code})" if company_code else ""))
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    st.pyplot(plt)

# Streamlit UI
def main():
    st.title("Price Clustering Visualization")

    # Market selection
    selected_market = st.selectbox("Select a Market", options=df["Market"].unique())

    # Company code input
    company_code = st.text_input("Enter Company Code (optional)")

    # Plot button
    if st.button("Show Chart"):
        plot_price_clustering(selected_market, company_code)

if __name__ == "__main__":
    main()
