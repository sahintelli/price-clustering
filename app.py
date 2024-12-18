import streamlit as st
import pandas as pd
import numpy as np
from mpl_interactions import interactive_plot
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Generate some example data
np.random.seed(42)
x = np.linspace(0, 10, 100)

# Create the initial plotly figure
fig = go.Figure()

# Add initial scatter plot
fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='Sine Wave'))

# Create steps for the slider to adjust the frequency of sine wave
steps = []
for i in np.linspace(1, 5, 10):
    step = {
        'label': f'{i:.1f}',  # Show frequency value on the slider
        'method': 'update',  # Use 'update' method for dynamic updates
        'args': [
            {'y': [np.sin(x * i)]},  # Update the y-values based on frequency
            {'title': f'Sine Wave with Frequency {i:.1f}'}  # Update the title dynamically
        ],
    }
    steps.append(step)

# Add slider functionality and update layout with updatemenus
fig.update_layout(
    title='Interactive Sine Wave with Frequency Adjustment',
    sliders=[{
        'currentvalue': {'visible': True, 'prefix': 'Frequency: '},
        'steps': steps
    }],
    updatemenus=[{
        'buttons': [{
            'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}],
            'label': 'Play',
            'method': 'animate',
        }],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top',
    }]
)

# Display the figure using Streamlit
st.plotly_chart(fig)


# # Ensure streamlit is available (to avoid ModuleNotFoundError)
# try:
#     import streamlit as st
# except ModuleNotFoundError:
#     raise ImportError("The 'streamlit' module is not installed. Install it using 'pip install streamlit'.")

# # Load real data from a publicly available source (example: Yahoo Finance)
# def load_real_data():
#     """Fetch real data for demonstration purposes."""
#     import yfinance as yf
    
#     # Fetch historical data for a sample stock (e.g., AAPL)
#     ticker = "AAPL"
#     data = yf.download(ticker, period="1mo", interval="1d")
    
#     # Prepare the DataFrame
#     data.reset_index(inplace=True)
#     data = data.rename(columns={"Adj Close": "Price"})
#     data["Market"] = "Stock Market"
#     data["CompanyCode"] = ticker
#     return data

# df = load_real_data()

# def plot_price_clustering_with_slider(selected_market, company_code):
#     """Filter data based on market and company code, then plot price clustering with an interactive slider."""
#     filtered_data = df[(df["Market"] == selected_market)]
#     if company_code:
#         filtered_data = filtered_data[filtered_data["CompanyCode"] == company_code]

#     if filtered_data.empty:
#         st.warning("No data available for the selected market and company code.")
#         return

#     # Define the interactive function for the histogram
#     def interactive_histogram(bins):
#         st.write(bins)
#         plt.figure(figsize=(10, 6))
#         plt.hist(filtered_data["Price"], bins=int(bins), color="skyblue", edgecolor="black")
#         plt.title(f"Price Clustering in {selected_market}" + (f" (Company: {company_code})" if company_code else ""))
#         plt.xlabel("Price")
#         plt.ylabel("Frequency")
#         plt.show()

#     # Create an interactive plot
#     interactive_plot(interactive_histogram, bins=(5, 50, 1))

# # Streamlit UI
# def main():
#     st.title("Price Clustering Visualization")

#     # Market selection
#     selected_market = st.selectbox("Select a Market", options=df["Market"].unique())

#     # Company code input
#     company_code = st.text_input("Enter Company Code (optional)")

#     # Interactive plot button
#     if st.button("Show Interactive Chart"):
#         plot_price_clustering_with_slider(selected_market, company_code)

# if __name__ == "__main__":
#     main()
