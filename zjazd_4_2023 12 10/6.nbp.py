"""
używając https://api.nbp.pl/en.html
pobierz i wyprintuj ostatni kurs wybranej waluty
"""

import httpx
from datetime import datetime, timedelta

"""response = httpx.get("http://api.nbp.pl/api/cenyzlota")
rate_dict = response.json()
print(f"The last date {rate_dict[0]['data']}, value: {rate_dict[0]['cena']}")

"""
"""
Napisz funkcj, która dla zadanej daty i waluty wyprintuje kurs.
Przykładowy URL : https://api.nbp.pl/api/exchangerates/rates/a/jpy/2023-12-08/
"""


def download_course(date, currency):
    try:
        response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}")
        response.raise_for_status()     # Rzuć wyjątek dla błędnych statusów HTTP
        rate_dict = response.json()['rates'][0]
        print(f"Course: {rate_dict['mid']} {currency}")
    except httpx.HTTPError as e:
        if e.response.status_code == 404:
            print(f"No data {currency} this day {date}. I will try to find the data from previous day.")
            previous_date = (datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
            print(f"I'll check for the date: {previous_date}")
            download_course(previous_date, currency)
        else:
            print(f"HTTP Error: {e.response.status_code}")
    except Exception as e:
        print(f"Different error: {e}")


date = input("Enter the date (yyyy-mm-dd): ")
currency = input("Enter the currency (EUR, USD, JPY, CHF, GBP): ")

download_course(date, currency)

"""
Zadanie domowe:
przy response.json() zrób sekcję try: except:
złap odpowiedni wyjątek, i spróbuj httpx.get ponownie z datą poprzedzającą.
PROBLEMY :(  :
1. datetime - obliczenie daty poprzedzającej
2. rekurencja
"""