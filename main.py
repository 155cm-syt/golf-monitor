import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

#################################
# 設定
#################################

TARGET_SHAFTS = [
    "VENTUS",
    "Tour AD",
    "Speeder"
]

MIN_PROFIT_RATE = 0.10

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

#################################
# 店舗データ取得
#################################

def get_store_items():

    url = "https://www.golfpartner.co.jp/shop/"

    r = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(r.text, "lxml")

    clubs = []

    items = soup.select(".item")

    for item in items:

        name_tag = item.select_one(".name")
        price_tag = item.select_one(".price")

        if not name_tag or not price_tag:
            continue

        name = name_tag.text.strip()

        price = price_tag.text.replace("¥","").replace(",","")

        try:
            price = int(price)
        except:
            continue

        clubs.append({
            "name": name,
            "buy_price": price
        })

    return clubs

#################################
# シャフト検出
#################################

def detect_shaft(text):

    for shaft in TARGET_SHAFTS:

        if shaft.lower() in text.lower():

            return shaft

    return None

#################################
# メルカリ価格取得
#################################

def mercari_average_price(keyword):

    url = f"https://jp.mercari.com/search?keyword={keyword}"

    r = requests.get(url, headers=HEADERS)

    soup = BeautifulSoup(r.text, "lxml")

    prices = soup.select("span")

    price_list = []

    for p in prices:

        t = p.text

        if "¥" in t:

            try:

                value = int(t.replace("¥","").replace(",",""))

                if 5000 < value < 100000:

                    price_list.append(value)

            except:
                pass

    if len(price_list) == 0:

        return 0

    return int(sum(price_list[:10]) / min(len(price_list),10))

#################################
# 利益計算
#################################

def calc_profit(buy, sell):

    profit = sell - buy

    rate = profit / buy

    return profit, rate

#################################
# メインAI
#################################

def golf_resale_ai():

    print("クラブ検索開始")

    clubs = get_store_items()

    results = []

    for club in clubs:

        name = club["name"]

        buy = club["buy_price"]

        shaft = detect_shaft(name)

        if shaft:

            sell_price = mercari_average_price(name)

            if sell_price == 0:
                continue

            profit, rate = calc_profit(buy, sell_price)

            if rate >= MIN_PROFIT_RATE:

                results.append({
                    "club": name,
                    "shaft": shaft,
                    "buy_price": buy,
                    "sell_price": sell_price,
                    "profit": profit,
                    "profit_rate": round(rate*100,1)
                })

    df = pd.DataFrame(results)

    if len(df) == 0:

        print("利益クラブなし")

    else:

        print("\n🔥利益クラブ候補\n")

        print(df.sort_values("profit", ascending=False))

#################################
# 定期実行
#################################

schedule.every(60).minutes.do(golf_resale_ai)

print("ゴルフ転売AI起動")

while True:

    schedule.run_pending()

    time.sleep(30)
