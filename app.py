import streamlit as st
import requests

# Page Custom Styling (Animated Gradient Background)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #1e1e2f, #2a2a40, #131324, #1f1a3a);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    h1 {
        color: #00ffcc !important;
        text-shadow: 0px 0px 10px rgba(0,255,204,0.5);
    }
    .stRadio p { color: #ffffff !important; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 MT5 Automated Trading Bot")

# Sidebar Controls
st.sidebar.header("Bot Controls")
status = st.sidebar.radio("Bot State:", ("Stopped", "Running"))

# Ngrok URL Box (Is mein hum aap ka pc link dalein ge)
NGROK_URL = st.sidebar.text_input("Enter PC Bridge URL (Ngrok):", "https://ngrok-free.app")

if status == "Running":
    st.success("Bot status: Active and listening for signals...")
    
    # Trading Panel Layout
    st.subheader("📊 Manual Execution Panel")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🟢 BUY NOW", use_container_width=True):
            with st.spinner("Sending BUY order..."):
                try:
                    response = requests.post(f"{NGROK_URL}/trade", json={"action": "BUY", "symbol": "EURUSD", "lot": 0.01}, timeout=10)
                    if response.status_code == 200:
                        st.success("BUY Order Executed!")
                    else:
                        st.error(f"Failed: {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
                    
    with col2:
        if st.button("🔴 SELL NOW", use_container_width=True):
            with st.spinner("Sending SELL order..."):
                try:
                    response = requests.post(f"{NGROK_URL}/trade", json={"action": "SELL", "symbol": "EURUSD", "lot": 0.01}, timeout=10)
                    if response.status_code == 200:
                        st.success("SELL Order Executed!")
                    else:
                        st.error(f"Failed: {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
else:
    st.warning("Bot status: Paused. Turn on 'Running' from sidebar to trade.")
