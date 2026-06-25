import streamlit as st

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
    .stRadio p {
        color: #ffffff !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 MT5 Automated Trading Bot")
st.sidebar.header("Bot Controls")

status = st.sidebar.radio("Bot State:", ("Stopped", "Running"))

if status == "Running":
    st.success("Bot status: Active and listening for signals...")
else:
    st.warning("Bot status: Paused.")

