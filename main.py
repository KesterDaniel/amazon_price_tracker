from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

request_header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36"
}

amazon_url = "https://www.amazon.com/Apple-i5-8259U-Quad-Core-802-11ac-Bluetooth/dp/B07PXW1QXT/ref=sr_1_9?crid=L7F0ROXUF" \
             "74G&keywords=macbook+pro&qid=1678118322&sprefix=map+book+pro%2Caps%2C1519&sr=8-9"

response = requests.get(url=amazon_url, headers=request_header)
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
price_tag = soup.select_one(".a-price .a-offscreen")
price = float(price_tag.getText().split("$")[1])
