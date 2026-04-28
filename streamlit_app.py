# streamlit_app.py
import streamlit as st
import pandas as pd
import time
import os
import plotly.express as px

# Import the engine logic from src
from src.fraud_engine import (
    create_transaction, 
    train_anomaly_detector, 
    predict_anomaly
)

# --- PAGE CONFIG ---
st.set_page_config(page_title="Fraud Sentinel Engine", layout="wide")

# --- TITLES ---
st.title("🛡️ Fraud Sentinel: Real-Time Detection Engine")
st.markdown("#### *The Story of a Sentinel: From Pattern Learning to Live Defense*")
st.divider()

# --- INITIALIZE PERSISTENT HISTORY ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=[
        "Timestamp", "Amount", "Hour", "Distance_from_Home", "AI_Flag"
    ])

# --- THE BRAIN (AI INITIALIZATION) ---
st.header("Training the Anomaly Detector")
if 'fraud_model' not in st.session_state:
    if st.button("🧠 Bootstrap AI (Train on 100 Transactions)"):
        baseline_data = [create_transaction() for _ in range(100)]
        baseline_df = pd.DataFrame(baseline_data)
        st.session_state.fraud_model = train_anomaly_detector(baseline_df)
        st.success("✅ AI Brain Active: Baseline established.")
else:
    st.success("✅ AI Brain is currently Active.")
    if st.button("🗑️ Reset AI & History"):
        del st.session_state.fraud_model
        st.session_state.history = pd.DataFrame(columns=["Timestamp", "Amount", "Hour", "Distance_from_Home", "AI_Flag"])
        st.rerun()

st.divider()

# --- THE FORENSIC INVESTIGATOR (WATERFALL FIX: PLACED ABOVE LOOP) ---
st.header("Forensic Deep-Dive")
# This section is now physically above the loop, so it is reachable when paused
if not st.session_state.history.empty:
    anomalies_only = st.session_state.history[st.session_state.history['AI_Flag'] == "🚨 SUSPECT"]
    if not anomalies_only.empty:
        st.subheader("Select a Suspect for Investigation")
        # The selectbox will now be responsive when the toggle below is OFF
        selection = st.selectbox("Inspect Transaction (Timestamp)", options=anomalies_only['Timestamp'])
        
        evidence = anomalies_only[anomalies_only['Timestamp'] == selection].iloc[0]
        
        ev1, ev2, ev3 = st.columns(3)
        ev1.warning(f"Amount: ${evidence['Amount']}")
        ev2.info(f"Hour: {evidence['Hour']}:00")
        ev3.info(f"Distance: {evidence['Distance_from_Home']} miles")
        
        st.markdown("**Sentinel Reasoning:** Statistical outlier detected in geographic/monetary variance.")
    else:
        st.info("No anomalies found in current buffer.")
else:
    st.info("Ingest data via the Live Feed below to enable forensics.")

st.divider()

# --- THE PULSE & INTELLIGENCE (THE LOOP) ---
st.header("Live Monitoring & Strategic Intelligence")

if 'fraud_model' in st.session_state:
    run_stream = st.toggle("🛰️ Stream Active (Toggle OFF to Pause & Investigate)")
else:
    st.warning("⚠️ Please Bootstrap the AI")
    run_stream = False

placeholder = st.empty()

if run_stream:
    while True:
        # 1. New Transaction
        new_tx = create_transaction()
        prediction = predict_anomaly(st.session_state.fraud_model, new_tx)
        new_tx['AI_Flag'] = "🚨 SUSPECT" if prediction == -1 else "✅ CLEAR"
        
        # 2. Update History
        new_df = pd.DataFrame([new_tx])
        st.session_state.history = pd.concat([new_df, st.session_state.history]).reset_index(drop=True).head(50)
        
        # 3. Data Cleaning for Plotly
        plot_df = st.session_state.history.copy()
        plot_df['Amount'] = pd.to_numeric(plot_df['Amount'], errors='coerce')
        plot_df['Distance_from_Home'] = pd.to_numeric(plot_df['Distance_from_Home'], errors='coerce')
        
        with placeholder.container():
            # KPI Dashboard
            k1, k2, k3 = st.columns(3)
            fraud_df = plot_df[plot_df['AI_Flag'] == "🚨 SUSPECT"]
            k1.metric("Total Scanned", len(plot_df))
            k2.metric("Anomalies", len(fraud_df), delta=f"{(len(fraud_df)/len(plot_df))*100:.1f}%")
            k3.metric("Loss Prevented", f"${fraud_df['Amount'].sum():,.2f}")

            # Cluster Map
            fig = px.scatter(
                plot_df, x="Amount", y="Distance_from_Home", color="AI_Flag", size="Amount",
                color_discrete_map={"✅ CLEAR": "#00FF00", "🚨 SUSPECT": "#FF0000"}
            )
            fig.update_layout(template="plotly_dark", height=400)
            st.plotly_chart(fig, width='stretch')

            # Live Grid
            def color_rows(row):
                return ['background-color: #9b2226' if row.AI_Flag == "🚨 SUSPECT" else '' for _ in row]
            st.dataframe(st.session_state.history.style.apply(color_rows, axis=1), width='stretch')
        
        time.sleep(1.0)
else:
    if not st.session_state.history.empty:
        st.info("⏸️ Stream Paused. Scroll up to investigate.")
        with placeholder.container():
            st.dataframe(st.session_state.history.head(10), width='stretch')
