# 🛡️ Fraud Sentinel: Real-Time Detection Engine
### Unsupervised Anomaly Detection for High-Velocity Financial Streams

## 🎯 Project Overview
In the banking sector, fraud detection is a race against time. This project implements a **Real-Time Sentinel** that monitors a simulated stream of credit card transactions and utilizes **Unsupervised Machine Learning** to flag suspicious behavior in milliseconds. 

Unlike traditional rule-based systems, this engine uses **Isolation Forest** algorithms to learn "Normal" spending profiles and detect "Anomalies" (outliers) based on geographic and monetary variance without requiring pre-labeled historical fraud data.

## 🏗️ Technical Architecture
- **Live Stream Generation:** A Python generator simulating a 1-second "heartbeat" of transaction metadata (Amount, Time, Location).
- **Unsupervised AI:** Isolation Forest model (Scikit-Learn) calibrated with a 3% contamination rate to identify outliers.
- **Dynamic War Room:** A live-updating dashboard featuring real-time KPI metrics and Plotly-based cluster analysis.
- **Human-in-the-Loop Forensics:** A dedicated investigative module for "pausing" the stream to perform deep-dive analysis on flagged suspects.

## 🛠️ Tech Stack
- **Environment:** Ubuntu (LinData VM)
- **Language:** Python 3.12
- **UI Framework:** Streamlit (Buffered `st.empty` management)
- **Machine Learning:** Scikit-learn (Isolation Forest)
- **Visualization:** Plotly Express (Spatial Anomaly Mapping)

## 🚀 Key Engineering Features
- **Real-Time Data Persistence:** Implemented `st.session_state` to allow pausing and resuming of live streams without data loss.
- **Waterfall Execution Fix:** Optimized script architecture to ensure UI responsiveness during high-velocity data loops.
- **Loss Prevention Dashboard:** Real-time calculation of total "at-risk" capital identified by the AI.
