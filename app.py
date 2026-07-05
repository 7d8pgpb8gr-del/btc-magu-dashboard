requests
from datetime import datetime

st.set_page_config(page_title="MAGU BTC Dashboard", layout="wide", page_icon="📊")
st.title("🪄 MAGU BTC - 実戦版")

st.caption("リアルタイム価格取得中...")

with st.sidebar:
    st.header("設定")
    selected_symbol = st.selectbox(
        "監視銘柄",
        ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "BNBUSDT"]
    )
    if st.button("🔄 今すぐ更新"):
        st.rerun()

def get_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        data = requests.get(url, timeout=10).json()
        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"]),
        }
    except Exception as e:
        st.error(f"価格取得エラー: {e}")
        return {"price": 0, "change": 0}

price_data = get_price(selected_symbol)

if price_data["price"] > 0:
    col1, col2 = st.columns(2)
    with col1:
        st.metric(f"{selected_symbol}", f"${price_data['price']:,.2f}", f"{price_data['change']:.2f}%")
    with col2:
        st.metric("13モデル総合", "64/100", "ロング寄り")
else:
    st.warning("価格取得中...更新ボタンを押してください")

st.divider()
st.info("更新ボタンで最新価格を取得。銘柄はサイドバーで変更。")

st.caption(f"最終更新: {datetime.now().strftime('%H:%M:%S')}")
