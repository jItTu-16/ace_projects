import requests


def exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/5eae1d0a50ecb31d874aef66/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    print(data)
    conversion_rate = data.get("conversion_rates")
    return conversion_rate[target_currency]


base_currency = input("Enter base crrency code: ")
target_currency = input("Enter target currency code: ")
base_currency = base_currency.upper()
target_currency = target_currency.upper()
print(
    f"Exchange rate between {base_currency} and {target_currency} is",
    exchange_rate(base_currency, target_currency),
)
