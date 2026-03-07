import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.title("🏌️ ゴルフ利益クラブ自動発見AI")

clubs = [
"Qi10 ドライバー",
"ステルス2 ドライバー",
"SIM2 ドライバー",
"G430 ドライバー",
"G425 ドライバー",
"パラダイム ドライバー",
"TSR2 ドライバー"
]

shafts = [
"VENTUS",
"TourAD",
"DI",
"UB",
"HD",
"IZ"
]

results = []

for club in clubs:

    mercari_url = f"https://www.mercari.com/jp/search/?keyword={club}"
    
    try:
        r = requests.get(mercari_url)
        soup = BeautifulSoup(r.text,"html.parser")

        prices = []
        for p in soup.select(".items-box-price")[:10]:
            price = int(p.text.replace("¥","").replace(",",""))
            prices.append(price)

        if prices:
            avg_price = sum(prices)/len(prices)
        else:
            avg_price = 0

    except:
        avg_price = 0

    shop_price = avg_price * 0.6

    profit = avg_price - shop_price

    results.append({
        "クラブ":club,
        "メルカリ平均":int(avg_price),
        "想定仕入れ":int(shop_price),
        "利益":int(profit)
    })

df = pd.DataFrame(results)

df = df.sort_values("利益",ascending=False)

st.dataframe(df)

st.success("利益クラブを上からチェックしてください")
