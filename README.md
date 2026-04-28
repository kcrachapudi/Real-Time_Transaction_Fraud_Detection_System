# 🛡️ Fraud Sentinel: Real-Time Detection Engine
### Unsupervised Anomaly Detection for High-Velocity Financial Streams

## 🎯 Project Overview
In banking, fraud detection is a race against time. This project implements a **Real-Time Sentinel** that monitors a simulated stream of credit card transactions and utilizes **Unsupervised Machine Learning** to flag suspicious behavior in milliseconds. 

Unlike traditional rule-based systems, this engine uses **Isolation Forest** algorithms to learn "Normal" spending profiles and detect "Anomalies" (outliers) based on geographic and monetary variance.

## 🏗️ Technical Architecture
- **Live Stream Generation:** A Python generator simulating a 1-second "heartbeat" of transaction metadata.
- **Unsupervised AI:** Isolation Forest model (Scikit-Learn) that identifies outliers without pre-labeled fraud data.
- **Dynamic Dashboard:** A "War Room" UI with real-time KPI metrics and Plotly-based cluster analysis.
- **Forensic Deep-Dive:** A "Human-in-the-Loop" module for investigating flagged timestamps and AI reasoning.

## 🛠️ Tech Stack
- **OS:** Ubuntu (LinData VM)
- **Language:** Python 3.12
- **UI:** Streamlit (Real-time `st.empty` buffer management)
- **ML:** Scikit-learn (Isolation Forest)
- **Visualization:** Plotly Express (Cluster Mapping)

## 🚀 Key Engineering Features
- **3.0% Contamination Rate:** Calibrated AI sensitivity to balance fraud detection with low false-positive rates.
- **Loss Prevention Metric:** Real-time calculation of total "at-risk" capital identified by the Sentinel.
- **Geometric Anomaly Detection:** Correlates transaction amount with geographic distance from home to identify "Stolen Card" patterns.
