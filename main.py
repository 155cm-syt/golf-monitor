import streamlit as st
import pandas as pd

st.title("⛳ ゴルフクラブ利益スキャナーAI")

clubs = [
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー",
"G430 ドライバー",
"G425 ドライバー",
"パラダイム ドライバー",
"TSR2 ドライバー"
]

results = []

for club in clubs:

    st.header(club)

    mercari = f"https://www.mercari.com/jp/search/?keyword={club}"
    golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
    partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
    gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

    st.write("🟥 メルカリ", mercari)
    st.write("🔵 ゴルフ5", golf5)
    st.write("🟢 ゴルフパートナー", partner)
    st.write("🟣 GDO", gdo)

    buy = st.number_input(f"{club} 仕入れ価格", key=club+"buy")
    sell = st.number_input(f"{club} メルカリ販売価格", key=club+"sell")

    if buy > 0 and sell > 0:

        profit = sell - buy
        rate = (profit / buy) * 100

        results.append({
            "クラブ": club,
            "利益": profit,
            "利益率": round(rate,1)
        })

if results:

    df = pd.DataFrame(results)
    df = df.sort_values("利益率", ascending=False)

    st.header("🏆 利益ランキング")

    st.dataframe(df)
    st.markdown("---")
st.markdown("## 🧾 メルカリ Sold 相場チェッカー")

club_query = st.text_input("クラブ名（Sold検索）")

if club_query:
    mercari_sold = f"https://jp.mercari.com/search?keyword={club_query}&status=sold_out"
    golf5 = f"https://www.alpen-group.jp/store/search?keyword={club_query}"
    partner = f"https://www.golfpartner.co.jp/shop/?keyword={club_query}"
    gdo = f"https://shop.golfdigest.co.jp/search/?q={club_query}"

    st.write("🟥 メルカリ Sold", mercari_sold)
    st.write("🔵 ゴルフ5", golf5)
    st.write("🟢 ゴルフパートナー", partner)
    st.write("🟣 GDO", gdo)

    buy_price = st.number_input("仕入れ価格", key="sold_buy")
    sold_price = st.number_input("メルカリSold平均価格（自分で入力）", key="sold_sell")

    if buy_price > 0 and sold_price > 0:
        profit = sold_price - buy_price
        rate = (profit / buy_price) * 100

        st.markdown("### 📊 利益結果")
        st.write(f"利益: {profit} 円")
        st.write(f"利益率: {rate:.1f} %")

        if rate >= 40:
            st.success("🔥 利益チャンス")
        elif rate >= 20:
            st.info("👍 利益あり")
        else:
            st.warning("⚠️ 利益薄い")
            st.markdown("---")
st.markdown("## 🤖 利益クラブ自動発見AI")

scan_clubs = [
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー",
"G430 ドライバー",
"G425 ドライバー",
"パラダイム ドライバー",
"TSR2 ドライバー",
"ZX5 ドライバー"
]

import pandas as pd

auto_results = []

for club in scan_clubs:

    st.subheader(club)

    mercari = f"https://jp.mercari.com/search?keyword={club}"
    golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
    partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
    gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

    st.write("🟥 メルカリ", mercari)
    st.write("🔵 ゴルフ5", golf5)
    st.write("🟢 ゴルフパートナー", partner)
    st.write("🟣 GDO", gdo)

    buy = st.number_input(f"{club} 仕入れ価格", key=club+"auto_buy")
    sell = st.number_input(f"{club} 想定販売価格", key=club+"auto_sell")

    if buy > 0 and sell > 0:

        profit = sell - buy
        rate = (profit / buy) * 100

        auto_results.append({
            "クラブ": club,
            "利益": profit,
            "利益率": round(rate,1)
        })

if auto_results:

    df = pd.DataFrame(auto_results)
    df = df.sort_values("利益率", ascending=False)

    st.markdown("### 🏆 利益クラブランキング")

    st.dataframe(df)
    st.markdown("---")
st.markdown("## 🧠 ブランドAIスキャナー")

brand_data = {
"TaylorMade":[
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー"
],
"PING":[
"G430 ドライバー",
"G425 ドライバー"
],
"Callaway":[
"パラダイム ドライバー",
"ローグST ドライバー"
],
"Titleist":[
"TSR2 ドライバー"
]
}

import pandas as pd

selected_brand = st.selectbox(
"ブランド選択",
list(brand_data.keys())
)

brand_results = []

for club in brand_data[selected_brand]:

    st.subheader(club)

    mercari = f"https://jp.mercari.com/search?keyword={club}"
    golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
    partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
    gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

    st.write("🟥 メルカリ", mercari)
    st.write("🔵 ゴルフ5", golf5)
    st.write("🟢 ゴルフパートナー", partner)
    st.write("🟣 GDO", gdo)

    buy = st.number_input(f"{club} 仕入れ価格", key=club+"brand_buy")
    sell = st.number_input(f"{club} 想定販売価格", key=club+"brand_sell")

    if buy>0 and sell>0:

        profit = sell-buy
        rate = (profit/buy)*100

        brand_results.append({
            "クラブ":club,
            "利益":profit,
            "利益率":round(rate,1)
        })

if brand_results:

    df = pd.DataFrame(brand_results)
    df = df.sort_values("利益率",ascending=False)

    st.markdown("### 🏆 ブランド利益ランキング")

    st.dataframe(df)
