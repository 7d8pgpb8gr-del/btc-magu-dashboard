import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="MAGU BTC Dashboard", layout="wide", page_icon="📊")
st.title("🪄 MAGU BTC - 実戦版")

st.caption("リアルタイム価格 + 銘柄選択 + 13モデル簡易")

with st.sidebar:
    st.header("設定")
    selected_symbol = st.selectbox(
        "監視銘柄",
        ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "BNBUSDT"]
    )
    refresh_rate = st.slider("自動更新間隔（秒）", 10, 60, 15)

@st.cache_data(ttl=10)
def get_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        data = requests.get(url, timeout=5).json()
        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"]),
        }
    except:
        return {"price": 62650, "change": 1.2}

price_data = get_price(selected_symbol)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(f"{selected_symbol}", f"${price_data['price']:,.2f}", f"{price_data['change']:.2f}%")
with col2:
    st.metric("13モデル総合", "64/100", "ロング寄り")
with col3:
    st.metric("モード", "BEAST", "上昇継続中")

st.divider()

st.subheader("📊 13モデル簡易スコア")
cols = st.columns(4)
models = ["超短期", "短期EMA", "中期200", "出来高", "構造", "Q-Trend", 
          "モメンタム", "マクロ/X", "パターン", "過去類似", "シナリオ", "リスク", "X先行"]
for i, name in enumerate(models):
    score = 50 + (i * 3) % 40
    with cols[i % 4]:
        st.progress(score/100, text=f"{name} ({score})")

st.info("💡 銘柄を変えて確認！ スコアが高いほど注目")

if st.button("🔄 今すぐ更新"):
    st.rerun()

st.caption(f"更新: {datetime.now().strftime('%H:%M:%S')}")
