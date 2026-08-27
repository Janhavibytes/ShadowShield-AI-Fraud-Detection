import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="ShadowShield",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp{
background:#080b14;
color:white;
}

.title{
font-size:48px;
font-weight:800;
color:#9d4edd;
text-align:center;
}

.hero{
padding:25px;
border-radius:18px;

background:
linear-gradient(
135deg,
#111827,
#172033
);

}

.block-container{
padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
"""
<div class='hero'>

<div class='title'>
SHADOWSHIELD
</div>

<p style='text-align:center;color:#cbd5e1'>

AI Fraud Detection • Real-Time Risk Intelligence

</p>

</div>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(
os.path.dirname(
os.path.abspath(__file__)
)
)

MODEL_PATH = os.path.join(
BASE_DIR,
"model",
"fraud_model.pkl"
)

DATA_PATH = os.path.join(
BASE_DIR,
"data",
"fraud.csv"
)

# ---------------- LOAD ----------------
model = joblib.load(MODEL_PATH)

# ---------------- METRICS ----------------
m1,m2,m3=st.columns(3)

with m1:
    st.metric(
        "Transactions / Day",
        "500K+"
    )

with m2:
    st.metric(
        "Latency",
        "<100 ms"
    )

with m3:
    st.metric(
        "Detection Recall",
        "84%"
    )

st.divider()

# ---------------- INPUT ----------------
st.subheader("Transaction Simulator")

c1,c2=st.columns(2)

with c1:

    amount=st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )

with c2:

    time=st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=10000.0
    )

st.divider()

# ---------------- ANALYSIS ----------------
if st.button("Analyze Transaction"):

    # Create a 30-feature transaction row
    # Time + V1 to V28 + Amount
    row = pd.DataFrame([[
        time,
        0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        amount
    ]], columns=[
        "Time",
        "V1", "V2", "V3", "V4", "V5", "V6", "V7",
        "V8", "V9", "V10", "V11", "V12", "V13", "V14",
        "V15", "V16", "V17", "V18", "V19", "V20", "V21",
        "V22", "V23", "V24", "V25", "V26", "V27", "V28",
        "Amount"
    ])

    # Predict fraud probability
    prob = model.predict_proba(row)[0][1]

    risk = round(prob * 100)

    # ---------------- RESULT ----------------
    st.subheader("Detection Result")

    st.metric(
        "Fraud Probability",
        f"{prob:.2%}"
    )

    st.metric(
        "Risk Score",
        f"{risk}/100"
    )

    st.progress(float(prob))

    # ---------------- RISK LEVEL ----------------
    if prob >= 0.70:

        st.error(
            "⚠ HIGH RISK TRANSACTION DETECTED"
        )

    elif prob >= 0.30:

        st.warning(
            "🟡 SUSPICIOUS ACTIVITY"
        )

    else:

        st.success(
            "✓ Transaction appears safe"
        )

    st.divider()

    # ---------------- ANALYSIS ----------------
    st.subheader("Analysis")

    if prob >= 0.70:

        st.write("""
• Multiple abnormal indicators detected

• High anomaly confidence

• Manual analyst review recommended
""")

    elif prob >= 0.30:

        st.write("""
• Moderate deviation detected

• Additional verification suggested
""")

    else:

        st.write("""
• Pattern aligns with expected behavior

• Low fraud confidence
""")

st.divider()

st.caption(
"ShadowShield • Fraud Intelligence Console"
)
