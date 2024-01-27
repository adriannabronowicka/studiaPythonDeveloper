import click
import httpx


def get_rate(currency: str):    #Sposób wykonania dependacy injection: jeśli w nawiasie damy (currency: str, internet=httpx)
    response = httpx.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/last")  #zamiast httpx wstawiamy internet
    rate_dict = response.json()['rates'][0]
    return rate_dict["mid"]


@click.command()
@click.argument("currency")
def main(currency: str):
    print(f"Course: {get_rate(currency)} PLN")
