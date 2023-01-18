import requests

res = requests.get('https://automatetheboringstuff.com/2e/chapter12/')
res.status_code

len(res.text)

print(res.text[:500])

res.raise_for_status()
playFile = open('RomeoandJuliet.txt', 'wb')
import os
os.getcwd()
'C:\\Users\\Kuya\\AppData\\Local\\Programs\\Python\\Python311'
for chunk in res.iter_content(100000):
    playFile.write(chunk)

    
100000
30204
playFile.close()
