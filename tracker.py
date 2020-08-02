import requests
from bs4 import BeautifulSoup
import smtplib
import time

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('orpaz007@gmail.com','qsupoyqcfxnsjtql')
    subject = "The Price Of S20 is Low Down - GoMobile"
    body = 'Check Price S20 GoMobile https://www.gomobile.co.il/items/2746963-Samsung-Galaxy-S20-SM-G980F-128GB-8GB'
    msg = f"subject: {subject}\n\n{body}"
    server.sendmail('orpaz007@gmail.com','orpaz007@gmail.com',msg)
    print("sent mail")
    server.quit()


def check_price():
    url ='https://www.gomobile.co.il/items/2746963-Samsung-Galaxy-S20-SM-G980F-128GB-8GB'
    headers = { "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    page = requests.get(url,headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id ="item_current_title").get_text()
    price = soup.find("span",{"class":"eilat_price_number"}).get_text()
    price = float(price[0:5].replace(',',''))

    if price <= 2380:
        send_mail()

# print(title.strip())
while True:
    check_price()
    time.sleep(60)


