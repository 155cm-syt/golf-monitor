import streamlit as st

st.set_page_config(page_title="中古ゴルフクラブ価格差モニター", layout="wide")

st.title("🏌️ 中古ゴルフクラブ価格差モニター（URL比較版）")

st.markdown("## 🔎 商品検索")

product_name = st.text_input("商品名を入力してください")

if product_name:

    st.markdown("### 🛒 各サイト検索リンク")

    golf5_url = f"https://www.alpen-group.jp/store/search?keyword={product_name}"
    partner_url = f"https://www.golfpartner.co.jp/shop/?keyword={product_name}"
    gdo_url = f"https://shop.golfdigest.co.jp/search/?q={product_name}"

    st.write("🔵 ゴルフ5")
    st.write(golf5_url)

    st.write("🟢 ゴルフパートナー")
    st.write(partner_url)

    st.write("🟣 GDO")
    st.write(gdo_url)

    st.markdown("---")

    st.markdown("## 💰 価格入力")

    buy_price = st.number_input("仕入れ価格", min_value=0)
    golf5_price = st.number_input("ゴルフ5価格", min_value=0)
    partner_price = st.number_input("ゴルフパートナー価格", min_value=0)
    gdo_price = st.number_input("GDO価格", min_value=0)

    prices = [p for p in [golf5_price, partner_price, gdo_price] if p > 0]

    if prices and buy_price > 0:
        max_price = max(prices)
        profit = max_price - buy_price
        rate = (profit / buy_price) * 100

        st.markdown("## 📊 利益計算結果")

        st.write(f"最高販売価格: {max_price} 円")
        st.write(f"利益: {profit} 円")
        st.write(f"利益率: {rate:.1f} %")

        if rate >= 50:
            st.success("🔥 激アツ案件！")
        elif rate >= 30:
            st.info("👍 仕入れ候補")
        else:
            st.warning("⚠️ 利益薄め")
            st.markdown("---")
st.markdown("## 🧠 利益ランキング")

site_prices = {
    "ゴルフ5": golf5_price,
    "ゴルフパートナー": partner_price,
    "GDO": gdo_price
}

results = []

for site, price in site_prices.items():
    if price > 0 and buy_price > 0:
        profit = price - buy_price
        rate = (profit / buy_price) * 100
        results.append({
            "サイト": site,
            "販売価格": price,
            "利益": profit,
            "利益率": round(rate,1)
        })

if results:
    import pandas as pd
    df = pd.DataFrame(results)
    df = df.sort_values("利益率", ascending=False)

    st.dataframe(df)

    best = df.iloc[0]

    st.markdown("### 🏆 ベスト販売先")

    st.success(
        f"{best['サイト']}で販売 → 利益 {best['利益']}円 / 利益率 {best['利益率']}%"
    )
    st.markdown("---")
st.markdown("## 🤖 人気クラブ一括検索")

clubs = [
"ステルス ドライバー",
"SIM2 ドライバー",
"ローグST ドライバー",
"G425 ドライバー",
"パラダイム ドライバー"
]

if st.button("人気クラブを検索"):
    
    for club in clubs:

        st.markdown(f"### ⛳ {club}")

        golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
        partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
        gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

        st.write("🔵 ゴルフ5", golf5)
        st.write("🟢 ゴルフパートナー", partner)
        st.write("🟣 GDO", gdo)

        st.markdown("---")
        st.markdown("---")
st.markdown("## 🚀 価格差クラブスキャナー")

clubs = [
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー",
"G425 ドライバー",
"パラダイム ドライバー",
"TSR2 ドライバー"
]

results = []

for club in clubs:

    st.markdown(f"### ⛳ {club}")

    buy = st.number_input(f"{club} 仕入れ価格", key=club+"buy")

    golf5 = st.number_input(f"{club} ゴルフ5価格", key=club+"g5")
    partner = st.number_input(f"{club} ゴルフパートナー価格", key=club+"gp")
    gdo = st.number_input(f"{club} GDO価格", key=club+"gdo")

    prices = [p for p in [golf5, partner, gdo] if p > 0]

    if prices and buy > 0:

        max_price = max(prices)
        profit = max_price - buy
        rate = (profit / buy) * 100

        results.append({
            "クラブ": club,
            "利益": profit,
            "利益率": round(rate,1)
        })

if results:

    import pandas as pd

    df = pd.DataFrame(results)
    df = df.sort_values("利益率", ascending=False)

    st.markdown("## 🏆 利益ランキング")

    st.dataframe(df)
    st.markdown("---")
st.markdown("## 🤖 自動クラブスキャナー")

clubs = [
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー",
"G425 ドライバー",
"パラダイム ドライバー"
]

import pandas as pd

scan_results = []

for club in clubs:

    st.markdown(f"### ⛳ {club}")

    google = f"https://www.google.com/search?tbm=shop&q={club}"
    golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
    partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
    gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

    st.write("🌐 Google相場", google)
    st.write("🔵 ゴルフ5", golf5)
    st.write("🟢 ゴルフパートナー", partner)
    st.write("🟣 GDO", gdo)

    buy = st.number_input(f"{club} 仕入れ価格", key=club+"buy")

    sell = st.number_input(f"{club} 想定販売価格", key=club+"sell")

    if buy > 0 and sell > 0:

        profit = sell - buy
        rate = (profit / buy) * 100

        scan_results.append({
            "クラブ": club,
            "利益": profit,
            "利益率": round(rate,1)
        })

if scan_results:

    df = pd.DataFrame(scan_results)
    df = df.sort_values("利益率", ascending=False)

    st.markdown("## 🏆 利益クラブランキング")

    st.dataframe(df)
