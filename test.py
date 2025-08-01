import streamlit as st

# Page config
st.set_page_config(page_title="Lot Size Calculator", layout="centered")

# Title
st.title("📊 Forex Lot Size Calculator")

# Select pair type
pair_type = st.selectbox("Select Pair Type", ["Gold (XAUUSD)", "Normal Forex Pair (EURUSD, etc.)"])

# Inject CSS based on pair type
if pair_type == "Gold (XAUUSD)":
    bg_color = "#FFD700"  # Gold
else:
    bg_color = "#87CEFA"  # Light blue

# Apply background color using markdown
st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {bg_color};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Inputs
risk_amount = st.number_input("Enter your risk amount ($)", min_value=0.0, step=0.5, format="%.2f")
stop_loss_pips = st.number_input("Enter Stop Loss (in pips)", min_value=0.0, step=0.1, format="%.1f")

# Define pip value
pip_value_per_lot = 1.0 if pair_type == "Gold (XAUUSD)" else 10.0

# Logic
if risk_amount > 0 and stop_loss_pips > 0:
    lot_size = risk_amount / (stop_loss_pips * pip_value_per_lot)

    if lot_size >= 0.01:
        st.success(f"✅ Recommended Lot Size: **{round(lot_size, 4)} lots**")
    else:
        min_risk = 0.01 * stop_loss_pips * pip_value_per_lot
        st.warning(f"⚠️ Lot size is too small: **{round(lot_size, 4)} lots**")
        st.info(f"💡 To trade at least 0.01 lot, increase your risk to at least **${round(min_risk, 2)}**")
elif risk_amount > 0 or stop_loss_pips > 0:
    st.info("ℹ️ Please enter both Risk Amount and Stop Loss to calculate.")
