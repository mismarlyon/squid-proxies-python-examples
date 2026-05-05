import requests
import time

proxy = {
    "http": "http://USERNAME:PASSWORD@PROXY_HOST:PORT",
    "https": "http://USERNAME:PASSWORD@PROXY_HOST:PORT"
}

url = "https://httpbin.org/status/500"  # simulate failure

max_retries = 3
retry_delay = 2  # seconds

for attempt in range(1, max_retries + 1):
    try:
        response = requests.get(url, proxies=proxy, timeout=10)

        if response.status_code == 200:
            print("Success:", response.json())
            break
        else:
            print(f"Attempt {attempt}: Status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt} failed:", e)

    if attempt < max_retries:
        print(f"Retrying in {retry_delay} seconds...\n")
        time.sleep(retry_delay)
    else:
        print("Max retries reached. Request failed.")
