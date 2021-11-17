import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# 🚗🔌🔋 Stock Price App for Tesla

Shown are the stock closing price and volume of Tesla

""")

#defining ticker symbol
tSymbol = 'TSLA'

#get data on this ticker
tData = yf.Ticker(tSymbol)

#get historical prices for this ticker
tDf = tData.history(period='1d', start='2017-11-18', end='2021-11-17')

st.title("Closing Price")
st.subheader("Closing Price is the raw price of the last transacted price in a security before the market officially closes. ")
st.line_chart(tDf.Close)

st.title("Volume")
st.subheader("Volume is the number of shares of a security traded during a given period of time. ")
st.line_chart(tDf.Volume)
