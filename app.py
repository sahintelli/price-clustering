import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ensure streamlit is available (to avoid ModuleNotFoundError)
try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("The 'streamlit' module is not installed. Install it using 'pip install streamlit'.")

# Load real data from a publicly available source (example: Yahoo Finance)
def load_real_data():
    """Fetch real data for demonstration purposes."""
    import yfinance as yf
    
    # Fetch historical data for a sample stock (e.g., AAPL)
    ticker = "AAPL"
    data = yf.download(ticker, period="1mo", interval="1d")
    
    # Prepare the DataFrame
    data.reset_index(inplace=True)
    data = data.rename(columns={"Adj Close": "Price"})
    data["Market"] = "Stock Market"
    data["CompanyCode"] = ticker
    return data

df = load_real_data()

def plot_price_clustering(selected_market, company_code, bins):
    """Filter data based on market and company code, then plot price clustering."""
    filtered_data = df[(df["Market"] == selected_market)]
    if company_code:
        filtered_data = filtered_data[filtered_data["CompanyCode"] == company_code]

    if filtered_data.empty:
        st.warning("No data available for the selected market and company code.")
        return

    # Ensure `bins` is an integer
    bins = int(bins)

    # Create histogram for price clustering
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_data["Price"], bins=bins, color="skyblue", edgecolor="black")
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

    # Number of bins slider
    bins = st.slider("Select Number of Bins", min_value=5, max_value=50, value=20, step=1)

    # Plot button
    if st.button("Show Chart"):
        plot_price_clustering(selected_market, company_code, bins)

if __name__ == "__main__":
    main()
