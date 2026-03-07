import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

keywords = ["Ventus", "TourAD"]

url = "https://www.golfpartner.co.jp/shop/"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")

clubs = soup.find_all("a")

for c in clubs:

    text = c.text

    for k in keywords:

        if k.lower() in text.lower():

            print("候補クラブ:", text)
