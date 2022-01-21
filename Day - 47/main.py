
import requests
from bs4 import BeautifulSoup
import lxml
from notification_manager import NotificationManager

email = NotificationManager()
URL = "https://www.lazada.co.th/products/k2-v2-usb-c-to-usb-a-keychron-k2-v2-wireless-hot-swappable-mechanical-keyboard-i598456393-s4925938395.html?spm=a2o4m.searchlist.list.1.55ff5643gFKg1r&search=1"

response = requests.get(URL, headers={"Accept-Language":"en-US,en;q=0.9"})
data = response.text

soup = BeautifulSoup(data, "lxml")

price = soup.find("span", class_="pdp-price")
text_price = price.getText()
str_price = price.getText().split('฿')[1]
# remove period and trailing zero in a string decimal
prc = str_price.rstrip('0').rstrip('.') if '.' in str_price else str_price
# remoing comma
final_price = int(prc.replace(',',''))


email.mail_sender(final_price, text_price)
