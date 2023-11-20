import os.path as op
import urllib.request
from datetime import date
from currency_converter import ECB_URL, CurrencyConverter

# Note that the default source is the European Central Bank,
# therefore some currencies might be missing.

filename = f"ecb_{date.today():%Y%m%d}.zip"
if not op.isfile(filename):
    urllib.request.urlretrieve(ECB_URL, filename)
converter = CurrencyConverter(filename)

result = None
while result is None:
    try:
        amount = float(input("Please enter the amount you want to convert: "))
        input_currency = input("Please enter the currency code that has to be converted: ").upper()
        output_currency = input("Please enter the currency code to convert: ").upper()
        print("You are converting", amount, input_currency, "to", output_currency, ".")
        result = converter.convert(amount, input_currency, output_currency)
        print("The converted rate is:", result)
    except ValueError as ve:
        print("The exchange information for the currency is currently not available, please try again later.")
        pass
        break
