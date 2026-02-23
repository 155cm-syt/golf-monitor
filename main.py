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
