import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd
import ta
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Stock Sentinel", layout="wide")
st.title("📊 Stock Sentinel")

st.sidebar.header("📥 Stock Input")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g. AAPL, TSLA, GOOGL)", value="AAPL")
period = st.sidebar.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y"], index=2)
interval = st.sidebar.selectbox("Select Interval", ["1d", "1h", "15m"], index=0)

if ticker:
    data = yf.download(ticker, period=period, interval=interval)
    if not data.empty:
        st.subheader(f"📈 {ticker.upper()} - Market Data")
        st.write(f"### Current Price: ${data['Close'].iloc[-1]:.2f}")

        # Technical Indicators
        rsi = ta.momentum.RSIIndicator(data['Close']).rsi()
        data['RSI'] = rsi
        data['MA20'] = data['Close'].rolling(window=20).mean()

        # Plotting
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))
        fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], mode='lines', name='MA 20'))
        fig.update_layout(title=f"{ticker} Price Chart", xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📉 RSI (Relative Strength Index)")
        st.line_chart(data[['RSI']].dropna())

        # News Headlines
        st.subheader("📰 Latest News Headlines")
        try:
            search_url = f"https://news.google.com/search?q={ticker}+stock"
            res = requests.get(search_url)
            soup = BeautifulSoup(res.text, 'html.parser')
            headlines = soup.select('article h3')[:5]
            if headlines:
                for h in headlines:
                    st.markdown(f"- {h.text}")
            else:
                st.info("No news found.")
        except:
            st.warning("Failed to fetch news. Try again later.")
    else:
        st.error("No data found. Please check the ticker symbol or try a different period.")
