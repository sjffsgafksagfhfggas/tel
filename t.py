import requests
import time

url = 'https://persian-follower.000webhostapp.com/tel/online.php'

s = requests.session()

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

r = s.get(url, headers=headers)

while True:
    print(r)
    time.sleep(10)
    s.get('https://persian-follower.000webhostapp.com/tel/online.php')