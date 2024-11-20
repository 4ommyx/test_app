import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('mtcar_linear_reg.pkl')


# Add a footer with credits
st.markdown("""
---
💡 *Built with Streamlit* | 🚀 *Your predictive companion*
""")
