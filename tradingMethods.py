import matplotlib.pyplot as plt
import streamlit as st
import tradingData as td

class TradingMethods():
    # Initialize ticker instance variable
    def __init__(self, ticker):
        self.ticker = ticker
        
    def ma(self, delta=365, window=1):
        """Simple Moving Average
        ### Parameters 
        delta: days in past to get ticker data
        window: MA widow period days
        ### Output
        Displays a streamlab matplotlib plot
        """
        data = td.histData.daily(self.ticker, delta)
        data[window] = data['close'].rolling(window).mean()

        fig, ax = plt.subplots(tight_layout=True)
        data[window].plot(ax=ax, alpha=0.8, color='orange')
        data['close'].plot(ax=ax, alpha=0.9, color='royalblue')
        st.pyplot(fig)
        
    # Exponential Moving Average
    def ema(self, delta=365, window=1):
        """Exponential Moving Average
        ### Parameters 
        delta: days in past to get ticker data
        window: MA widow period days
        ### Output
        Displays a streamlab matplotlib plot
        """
        data = td.histData.daily(self.ticker, delta)
        data[window] = data['close'].ewm(span=window, adjust=False).mean()

        fig, ax = plt.subplots(tight_layout=True)
        data[window].plot(ax=ax, alpha=0.8, color='orange')
        data['close'].plot(ax=ax, alpha=0.9, color='royalblue')
        st.pyplot(fig)
        
    # Moving Average Convergence Divergence
    def macd(self, delta, ema1=12, ema2=26, signal=9):
        """MACD
        ### Parameters 
        delta: days in past to get ticker data
        ema1: fast EMA period
        ema2: slow EMA period
        ### Output
        Displays a streamlab matplotlib plot
        """
        data = td.histData.daily(self.ticker, delta)
        exp1 = data['close'].ewm(span=ema1, adjust=False).mean()
        exp2 = data['close'].ewm(span=ema2, adjust=False).mean()
        data['MACD'] = exp1 - exp2
        data['signal line'] = data['MACD'].ewm(span=signal, adjust=False).mean()

        fig, ax = plt.subplots(2,1, gridspec_kw={'height_ratios': [3, 2]}, tight_layout=True)
        data['close'].plot(ax=ax[0], fontsize=6, color='royalblue')
        data[['MACD', 'signal line']].plot(ax=ax[1], fontsize=6, alpha=0.8, color=['green', 'red'])
        ax[1].axhline(color='black')
        ax[1].legend(prop={"size": 7})
        st.pyplot(fig) 
    
    def crossOver(self, delta, slow, fast):
        """MA Crossover
        ### Parameters 
        delta: days in past to get ticker data
        slow: fast MA period
        fast: fast EMA period
        ### Output
        Displays a streamlab matplotlib plot
        """
        data = td.histData.daily(self.ticker, delta)
        if fast and slow:
            slowText = "MA " + str(slow)
            fastText = "MA " + str(fast)
            data[fastText] = data['close'].rolling(fast).mean()
            data[slowText] = data['close'].rolling(slow).mean()

            fig, ax = plt.subplots(tight_layout=True)
            data[[fastText, slowText]].plot(ax=ax, alpha=0.8, color=['green', 'orange'])
            data['close'].plot(ax=ax, alpha=0.9, color='royalblue')
            st.pyplot(fig)