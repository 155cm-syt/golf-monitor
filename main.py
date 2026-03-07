import streamlit as st
import pandas as pd

st.title("⛳ ゴルフクラブ価格差AIスキャナー")

brands = {
"TaylorMade":[
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー"
],
"Callaway":[
"パラダイム ドライバー",
"ローグST ドライバー"
],
"PING":[
"G430 ドライバー",
"G425 ドライバー"
],
"Titleist":[
"TSR2 ドライバー"
]
}

results = []

for brand in brands:

    st.header(brand)

    for club in brands[brand]:

        st.subheader(club)

        google = f"https://www.google.com/search?tbm=shop&q={club}"
        golf5 = f"https://www.alpen-group.jp/store/search?keyword={club}"
        partner = f"https://www.golfpartner.co.jp/shop/?keyword={club}"
        gdo = f"https://shop.golfdigest.co.jp/search/?q={club}"

        st.write("🌐 相場", google)
        st.write("🔵 ゴルフ5", golf5)
        st.write("🟢 ゴルフパートナー", partner)
        st.write("🟣 GDO", gdo)

        buy = st.number_input(f"{club} 仕入れ", key=club+"buy")
        sell = st.number_input(f"{club} 販売", key=club+"sell")

        if buy>0 and sell>0:

            profit = sell-buy
            rate = (profit/buy)*100

            results.append({
                "クラブ":club,
                "利益":profit,
                "利益率":round(rate,1)
            })

if results:

    df = pd.DataFrame(results)
    df = df.sort_values("利益率",ascending=False)

    st.header("🏆 利益ランキング")

    st.dataframe(df)
