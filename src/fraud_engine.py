# src/fraud_engine.py
import pandas as pd
import numpy as np
import random

def create_transaction():
    """
    Simulates a single credit card transaction.
    """
    is_anomaly = np.random.choice([0, 1], p=[0.97, 0.03]) # 3% chance of being weird
    
    if is_anomaly:
        # High amount, strange hour (3 AM)
        amount = round(random.uniform(800, 5000), 2)
        hour = random.randint(0, 4)
    else:
        # Normal daily spending
        amount = round(random.uniform(5, 150), 2)
        hour = random.randint(8, 22)
        
    return {
        "Timestamp": pd.Timestamp.now(),
        "Amount": amount,
        "Hour": hour,
        "Distance_from_Home": round(random.uniform(0, 100), 2),
        "Is_Anomaly": is_anomaly # We use this to check our AI later
    }

from sklearn.ensemble import IsolationForest

def train_anomaly_detector(df):
    """
    Learns the 'normal' patterns of the stream.
    """
    # We train on Amount, Hour, and Distance
    features = ['Amount', 'Hour', 'Distance_from_Home']
    
    # contamination=0.03 means we expect roughly 3% of data to be 'weird'
    model = IsolationForest(contamination=0.03, random_state=42)
    model.fit(df[features])
    
    return model

def predict_anomaly(model, tx_dict):
    """
    Scores a single transaction. 
    Returns -1 for Anomaly, 1 for Normal.
    """
    features = ['Amount', 'Hour', 'Distance_from_Home']
    df_tx = pd.DataFrame([tx_dict])[features]
    
    # Predict returns -1 (anomaly) or 1 (normal)
    prediction = model.predict(df_tx)
    return prediction[0]
