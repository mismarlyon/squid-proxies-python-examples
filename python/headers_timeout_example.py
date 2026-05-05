import requests

proxy = {
    "http": "http://USERNAME:PASSWORD@PROXY_HOST:PORT",
    "https": "http://USERNAME:PASSWORD@PROXY_HOST:PORT"
}

url = "https://httpbin.org/headers"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

try:
    response = requests.get(
        url,
        proxies=proxy,
        headers=headers,
        timeout=5  # important for avoiding hangs
    )

    print(response.json())

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
