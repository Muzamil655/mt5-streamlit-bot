import streamlit as st

st.title("🤖 MT5 Automated Trading Bot")
st.sidebar.header("Bot Controls")

status = st.sidebar.radio("Bot State:", ("Stopped", "Running"))

if status == "Running":
    st.success("Bot status: Active and listening for signals...")
else:
    st.warning("Bot status: Paused.")
