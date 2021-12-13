import requests

from bs4 import BeautifulSoup as BS

r = requests.get("http://banki.tomsk.ru/pages/41/")
html = BS(r.content, "html.parser")

curr = html.get_text()

currencytypes = {"Австралийский доллар": "AUD", "Азербайджанский манат": "AZN", "Армянский драм": "AMD",
                 "Белорусский рубль": "BYN", "Болгарский лев": "BGN", "Бразильский реал": "BRL",
                 "Венгерский форинт": "HUF", "Вон Республики Корея": "KRW", "Гонконгский доллар": "HKD",
                 "Датская крона": "DKK", "Доллар США": "USD", "Евро": "EUR", "Индийский рупий": "INR",
                 "Казахский тенге": "KZT", "Канадский доллар": "CAD", "Киргизский сом": "KGS", "Китайский юань": "CNY",
                 "Молдавский лей": "MDL", "Новый румынский лей": "RON", "Новый туркменский манат": "TMT",
                 "Норвежская крона": "NOK", "Польский злотый": "PLN", "Сингапурский доллар": "SGD",
                 "Таджикский сомони": "TJS", "Турецкая лира": "TRY", "Узбекский сум": "UZS", "Украинская гривна": "UAH",
                 "Фунт стерлингов Соединенного королевства": "GBP", "Чешская крона": "CZK", "Шведская крона": "SEK",
                 "Швейцарский франк": "CHF", "Южноафриканский рэнд": "ZAR", "Японская йена": "JPY"}

currencynames = currencytypes.keys()


class infcurrency:
    tiker = ""
    edinica = ""
    kurs = ""
    name = ""


def start_search(a):
    start = curr.find(a, curr.find(a) + 1)
    return start


def currency_main(find_currency, kol):
    nach = start_search(currencytypes[find_currency])
    res = curr[nach:nach + 14].split("\n")
    OurCurrency = infcurrency()
    OurCurrency.tiker = res[0]
    OurCurrency.kurs = res[2]
    OurCurrency.edinica = res[1]
    OurCurrency.name = find_currency
    final_text_currency = "Валюта: " + str(OurCurrency.name) + "\n\n\nКурс: " + str(
        OurCurrency.kurs) + "\n\n\nИтого в рублях: " + str(
        (int(kol) / int(OurCurrency.edinica)) * float(OurCurrency.kurs.replace(",", ".")))
    return final_text_currency

