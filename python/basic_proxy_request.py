import requests

proxy = {
    "http": "http://USERNAME:PASSWORD@PROXY_HOST:PORT",
    "https": "http://USERNAME:PASSWORD@PROXY_HOST:PORT"
}

url = "https://httpbin.org/ip"

response = requests.get(url, proxies=proxy, timeout=10)

print(response.json())
