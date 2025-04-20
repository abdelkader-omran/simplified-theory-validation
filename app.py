
import streamlit as st
from utils.load_metrics import load_validation_metrics
from utils.plot_helpers import plot_loss_bar_chart

st.set_page_config(page_title="Model Validation Dashboard", layout="wide")

st.title("Scientific Pipeline Dashboard")
st.markdown("Track and compare validation performance for all models.")

# Load metrics
metrics_df = load_validation_metrics("data/validation_metrics")

# Display bar chart
st.subheader("Validation Loss Summary")
fig = plot_loss_bar_chart(metrics_df)
st.pyplot(fig)

# Show data table
st.subheader("Raw Validation Metrics")
st.dataframe(metrics_df)

# Placeholder for additional features
st.subheader("Future Enhancements")
st.markdown("""
- Checkpoint Explorer
- Per-Epoch Loss Curves
- Model Version Comparison
- Integration with Git/DVC metadata
""")
