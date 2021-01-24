import yfinance as yf
import streamlit as st

st.write("""
# Hisse Senedi Fiyatı Uygulaması
Google'ın hisse senedi **kapanış fiyatı** ve **işlem hacmi** gösterilmektedir.
Borsada işlem hacmi, bir menkul kıymette ya da borsada tüm alış ve satışların parasal değerleridir.
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Hisse Senedi Kapanış Fiyatı
""")
st.line_chart(tickerDf.Close)
st.write("""
## İşlem Hacmi
""")
st.line_chart(tickerDf.Volume)
