import streamlit as st
import requests
import time

st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(-45deg, #0f172a, #1e1b4b, #311042); background-size: 400% 400%; animation: gradient 15s ease infinite; }
    @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    h1 { color: #00ffcc !important; text-shadow: 0px 0px 10px rgba(0,255,204,0.5); }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 SMC Fully Automated Bot")

st.sidebar.header("Bot Configuration")
NGROK_URL = st.sidebar.text_input("Enter PC Bridge URL (Ngrok):", "https://ngrok-free.dev")
trade_mode = st.sidebar.radio("Select Working Mode:", ("Manual", "Fully Automated 🚀"))
symbol_to_trade = st.sidebar.selectbox("Select Symbol:", ("EURUSD", "GBPUSD", "XAUUSD"))

if trade_mode == "Fully Automated 🚀":
    st.success(f"Automation Active: Analyzing pichli 100 candles for {symbol_to_trade}...")
    
    # Automated loop trigger box
    if st.button("Start Auto Scan Loop"):
        st.info("Scanner loop started. Checking market structure every 15 seconds. Do not close this tab.")
        placeholder = st.empty()
        
        while True:
            try:
                response = requests.post(f"{NGROK_URL}/auto_trade", json={"symbol": symbol_to_trade}, timeout=10)
                res_data = response.json()
                
                with placeholder.container():
                    st.write(f"🔄 Last Scan Time: {time.strftime('%H:%M:%S')}")
                    if "Executed" in res_data.get('message', ''):
                        st.success(f"🔥 Alert: {res_data.get('message')}")
                    else:
                        st.warning(f"Status: {res_data.get('message')}")
                        
            except Exception as e:
                st.error(f"Scanner Connection Error: {e}")
                
            time.sleep(15) # Har 15 seconds baad auto-check kare ga
else:
    st.warning("Manual mode active. Automation is currently paused.")

