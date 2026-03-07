import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import schedule

#################################
# 設定
#################################

SHAFT_KEYWORDS = [
    "VENTUS",
    "Tour AD",
    "Speeder"
]

MIN_PROFIT_RATE = 0.10

HEADERS = {
    "User-Agent":"Mozilla/5.0"
}

#################################
# 店舗取得
#################################

def get_store_items():

    url = "https://www.golfpartner.co.jp/shop/"

    r = requests.get(url,headers=HEADERS)

    soup = BeautifulSoup(r.text,"lxml")

    items = soup.select(".item")

    clubs = []

    for item in items:

        name = item.select_one(".name")
        price = item.select_one(".price")

        if not name or not price:
            continue

        n = name.text.strip()

        p = price.text.replace("¥","").replace(",","")

        try:
            p = int(p)
        except:
            continue

        clubs.append({
            "name":n,
            "buy":p
        })

    return clubs

#################################
# シャフト検出
#################################

def detect_shaft(name):

    for s in SHAFT_KEYWORDS:

        if s.lower() in name.lower():

            return s

    return None

#################################
# メルカリ価格取得
#################################

def mercari_avg(keyword):

    url = f"https://jp.mercari.com/search?keyword={keyword}"

    r = requests.get(url,headers=HEADERS)

    soup = BeautifulSoup(r.text,"lxml")

    prices = soup.find_all("span")

    result = []

    for p in prices:

        t = p.text

        if "¥" in t:

            try:

                value = int(t.replace("¥","").replace(",",""))

                if 5000 < value < 100000:

                    result.append(value)

            except:
                pass

    if len(result) == 0:
        return 0

    return int(sum(result[:10])/min(len(result),10))

#################################
# ヘッド価格
#################################

def head_price(name):

    keyword = name + " ヘッド"

    return mercari_avg(keyword)

#################################
# シャフト価格
#################################

def shaft_price(shaft):

    keyword = shaft + " シャフト"

    return mercari_avg(keyword)

#################################
# AI分析
#################################

def golf_ai():

    print("クラブ分析開始")

    clubs = get_store_items()

    results = []

    for club in clubs:

        name = club["name"]

        buy = club["buy"]

        shaft = detect_shaft(name)

        if not shaft:
            continue

        head = head_price(name)

        shaft_val = shaft_price(shaft)

        sell = head + shaft_val

        profit = sell - buy

        rate = profit / buy

        if rate >= MIN_PROFIT_RATE:

            results.append({

                "club":name,
                "shaft":shaft,
                "buy":buy,
                "head_price":head,
                "shaft_price":shaft_val,
                "sell_total":sell,
                "profit":profit,
                "profit_rate":round(rate*100,1)

            })

    df = pd.DataFrame(results)

    if len(df) == 0:

        print("利益クラブなし")

    else:

        print("\n🔥利益クラブランキング\n")

        print(df.sort_values("profit",ascending=False))

#################################
# 定期巡回
#################################

schedule.every(30).minutes.do(golf_ai)

print("ゴルフ転売AI起動")

while True:

    schedule.run_pending()

    time.sleep(30)
