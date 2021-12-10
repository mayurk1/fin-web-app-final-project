import streamlit as st
from streamlit.type_util import Key
import tradingMethods as tm

# Page settings
st.set_page_config(
     page_title="Not Financial Advice",
     page_icon="🤑",
     layout="wide",
     initial_sidebar_state="expanded"
)

# Create tickerInput variable, handle if there is no ticker passed by user
tickerInput = st.sidebar.text_input(label="Ticker", placeholder="SPY")
if not tickerInput:
    tickerInput = "SPY"
tickerInput = tickerInput.upper()
    
# Technical Analysis indicator selection
taInput = st.sidebar.selectbox(label="Technical Analysis", options=["MA", "EMA", "MACD", "MA Cross Over"])

# Establish form to properly take in user input and selections
form = st.sidebar.form(key="testing")
deltaInput = form.slider(label="Delta", min_value=1, max_value=999, step=1)

# Populate sidebar forms to show proper inputs based on user selection
if taInput == "MA":
    windowInput = form.slider(label="Window Period", min_value=1, max_value=999, step=1)
elif taInput == "EMA":
    windowInput = form.slider(label="Window Period", min_value=1, max_value=999, step=1)
elif taInput == "MACD":
    ema1Input = form.slider(label="Fast EMA", min_value=1, max_value=100, step=1, value=12)
    ema2Input = form.slider(label="Slow EMA", min_value=1, max_value=100, step=1, value=26)
    signalInput = form.slider(label="Signal", min_value=1, max_value=100, step=1, value=9)
elif taInput == "MA Cross Over":
    maFastInput = form.slider(label="Fast EMA", min_value=1, max_value=999, step=1, value=1)
    maSlowInput = form.slider(label="Slow EMA", min_value=1, max_value=999, step=1, value=1)

# Button to submit form, triggers logic to take in all values from the Streamlit form in order to prevent inputs from having conflicts
submitButton = form.form_submit_button(label="Run")

# Update page title based on ticker and selection
st.title(taInput + " - " + tickerInput)

# Logic for charting based on user selection
if taInput == 'MA':
    chart = tm.TradingMethods(tickerInput).ma(window=windowInput, delta=deltaInput)
elif taInput == 'EMA':
    chart = tm.TradingMethods(tickerInput).ema(window=windowInput, delta=deltaInput)
elif taInput == 'MACD':
    chart = tm.TradingMethods(tickerInput).macd(delta=deltaInput, ema1=ema1Input, ema2=ema2Input, signal=signalInput)
elif taInput == 'MA Cross Over':
    chart = tm.TradingMethods(tickerInput).crossOver(delta=deltaInput, slow=maSlowInput, fast=maFastInput)
