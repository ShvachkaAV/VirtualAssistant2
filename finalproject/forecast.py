import requests
from bs4 import BeautifulSoup as BS2


def forecast_main(city):
    r2 = requests.get("https://www.google.com/search?q=погода+" + city)
    html2 = BS2(r2.content, "html.parser")
    weather_temp = html2.find("div", class_="BNeawe").text
    return "Текущая температура: " + weather_temp
