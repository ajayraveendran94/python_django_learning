import requests

def main():
    payload = {"base": "GBP",
               "symbols": "GBP"}
    response = requests.get('https://api.exchangeratesapi.io/latest?access_key=711effe35c652a168e5c97c1bba544b6', 
                            params= payload)
    print("Status Code :", response.status_code)
    print("Content-Type :", response.headers['Content-Type'])
    print("Data :", response.json())

if __name__ == "__main__":
    main()
