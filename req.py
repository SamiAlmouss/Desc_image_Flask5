import threading
import requests
import time
url0 = "https://desc-image-flask2.onrender.com/"
url1 = "https://desc-image-flask4.onrender.com/"

def run_app():
    while True:
        try:
            r=requests.get(url0, timeout=100)
            r=requests.get(url1, timeout=100)
            print(r.status_code)
            time.sleep(300)
        except requests.RequestException as e:
            print("Request failed:", e)

t = threading.Thread(target=run_app)
t.daemon=True
t.start()
