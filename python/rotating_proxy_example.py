import requests
import random
import time

proxies = [
    "http://USERNAME:PASSWORD@PROXY1:PORT",
    "http://USERNAME:PASSWORD@PROXY2:PORT",
    "http://USERNAME:PASSWORD@PROXY3:PORT"
]

url = "https://httpbin.org/ip"

def get_random_proxy():
    return {
        "http": random.choice(proxies),
        "https": random.choice(proxies)
    }

for i in range(5):
    proxy = get_random_proxy()
    
    try:
        response = requests.get(url, proxies=proxy, timeout=10)
        print(f"Request {i+1}: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request {i+1} failed:", e)
    
    time.sleep(2)
