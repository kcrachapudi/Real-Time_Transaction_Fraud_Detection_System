# streamlit_app.py
import streamlit as st
import pandas as pd
import time
from src.fraud_engine import create_transaction

st.set_page_config(page_title="Fraud Sentinel", layout="wide")

st.title("🛡️ Real-Time Transaction Fraud Detection")
st.markdown("#### *Phase 1: The Live Transaction Stream*")
st.divider()

# --- INITIALIZE SESSION STATE ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Timestamp", "Amount", "Hour", "Distance_from_Home", "Is_Anomaly"])

# --- LIVE FEED CONTROLS ---
run_stream = st.toggle("🛰️ Start Real-Time Stream")

# We create a placeholder so the table updates in one spot
placeholder = st.empty()

if run_stream:
    while True:
        # 1. Create a new "swipe"
        new_tx = create_transaction()
        new_df = pd.DataFrame([new_tx])
        
        # 2. Append and CLEAN the index (The fix for your error)
        # .reset_index(drop=True) ensures every row has a unique identifier
        st.session_state.history = pd.concat([new_df, st.session_state.history]).reset_index(drop=True).head(20)
        
        # 3. Update the UI
        with placeholder.container():
            st.subheader("Incoming Transactions")
            
            # Now the Styler will work perfectly because the index is unique
            st.dataframe(
                st.session_state.history.style.highlight_max(axis=0, subset=['Amount'], color='#9b2226'),
                width='stretch'
            )
            
            avg_val = st.session_state.history['Amount'].mean()
            st.metric("Avg Transaction Value (Rolling)", f"${avg_val:.2f}")
        
        time.sleep(5)  # Simulate delay between transactions
