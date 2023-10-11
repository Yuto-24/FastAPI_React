import requests
from pprint import pprint

def main():
    url = 'http://localhost:8000/item'
    body = {
        "name": "apple",
        "description": "an apple",
        "price": 128,
        "tax": 1.08
    }

    # POST時に json= とすることで、requestsが自動的にContentsTypeをjsonとして送信してくれる。
    res = requests.post(url, json=body)
    pprint(res.json())
    return res

if __name__ == "__main__":
    main()
