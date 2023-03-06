import os
import smtplib
import ssl
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from dotenv import load_dotenv

load_dotenv()

item_lowest_price = 540

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
item = soup.find(name="span", id="productTitle").getText()

# Sending Email
if price < item_lowest_price:
    context = ssl.create_default_context()

    EMAIL = "kesterdaniel401@gmail.com"
    PASSWORD = os.environ["EMAIL_PASSWORD"]

    msg = MIMEMultipart()
    msg["from"] = EMAIL
    msg["To"] = "kesterdan17@gmail.com"
    msg["Subject"] = "Amazon Low Price Alert!!"

    html = "<html><body>"
    html += f"<h3>{item} now ${price}</h3>"
    html += f"<p><a href={amazon_url}>Check it Out</a></p>"
    html += "</body></html>"

    msg.attach(MIMEText(html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="kesterdan17@gmail.com",
            msg=msg.as_string()
        )
