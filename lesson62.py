from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.python.org")
# print(html.text)

soup = BeautifulSoup(html.text, "lxml")