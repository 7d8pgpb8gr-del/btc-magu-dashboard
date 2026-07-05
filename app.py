import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="MAGU BTC Dashboard", layout="wide", page_icon="📊")
st.title("🪄 MAGU BTC - 実戦版")

st.caption("リアルタイム価格 + 銘柄選択")

with st.sidebar:
    st.header("設定")
    selected_symbol = st.selectbox(
        "監視銘柄",
        ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "BNBUSDT"]
    )
    if st.button("🔄 更新"):
        st.rerun()

# 価格取得
def get_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        data = requests.get(url, timeout=5).json()
        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"]),
        }
    except:
        return {"price": 0, "change": 0}

price_data = get_price(selected_symbol)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(f"{selected_symbol}", f"${price_data['price']:,.2f}", f"{price_data['change']:.2f}%")

st.divider()

st.info("上部の「更新」ボタンで価格を最新に！ サイドバーで銘柄変更")

st.caption(f"最終更新: {datetime.now().strftime('%H:%M:%S')}")
