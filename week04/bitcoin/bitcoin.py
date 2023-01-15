import requests
import sys
import json

coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():
    print(f"${calc_coins(input_logic()):,.4f}")


def input_logic():

    try:

        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")
            sys.exit(1)
        else:
            return float(sys.argv[1])

    # catch error for if the command-line argument is anything else than a float number
    except (TypeError, ValueError):
        print("Command-line argument is not a number")
        sys.exit(1)


def calc_coins(n):

    try:
        response = requests.get(coindesk_api)
        data = response.json()
        value = data["bpi"]["USD"]["rate_float"]
        amount = value * n

    except requests.RequestException:
        print("Coinbase not available. Please retry in a short moment.")
        sys.exit()

    return amount

if __name__ == "__main__":
    main()