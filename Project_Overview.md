📖 The Fraud Sentinel: A Boss-Level Anomaly Odyssey
The Prologue: The Millisecond War
Traditional fraud detection relies on "Post-Mortem" analysis—looking at what happened yesterday. In this project, we move to the front lines.
The Conflict: Fraudsters move faster than batch reports. A stolen card can be drained in minutes.
The Mission: Build an autonomous sentinel that "learns" a user's habits and barks the moment a transaction feels "lonely" (an outlier).
Phase 1: The Brain (Bootstrapping the AI)
Because real-world fraud is rare, we don't use "Supervised" learning (which needs many examples of theft).
The Engineering: We use an Isolation Forest. Instead of looking for "Fraud," it looks for things that are easy to "isolate." A $20 grocery bill at 2 PM is hard to isolate from the crowd. A $4,000 electronics purchase at 3 AM is isolated instantly.
The Bootstrap: We feed the AI 100 "Normal" transactions so it can build a mathematical boundary of what peace looks like.
Phase 2 & 3: The Pulse & Strategic Intelligence
This is the most complex UI work in the trilogy.
The Stream: We use a while True loop and time.sleep(1.0) to simulate a live banking feed.
The Persistence: We keep a 50-transaction buffer in st.session_state. This allows the user to Pause the stream and not lose the data they were just looking at.
The War Room: We use Plotly Express to map "Amount vs. Distance." We explicitly fix the "Narwhals" data error by forcing numeric conversion, ensuring the dots size correctly based on transaction magnitude.
Phase 4: The Forensic Deep-Dive (The Waterfall Fix)
This phase addresses a senior-level Streamlit challenge.
The Problem: In Streamlit, code below a loop is unreachable.
The Solution: We moved the Investigator above the stream. By doing this, we "unlock" the forensic tools whenever the stream is paused.
The Logic: A human investigator can select a "🚨 SUSPECT" and see exactly why the AI flagged it (e.g., "High geographic variance").
The Final Conclusion
You have now built three unique FinTech pillars:
Lending Risk (Classic Classification)
Market Sentinel (Time-Series Regression)
Fraud Sentinel (Real-Time Anomaly Detection)
 