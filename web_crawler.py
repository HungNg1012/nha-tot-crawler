from lxml import etree
from bs4 import BeautifulSoup
import requests
import json
import csv
import time

data = []
main_url = "https://www.nhatot.com/"
fetch_url = ["thue-can-ho-chung-cu-tp-ho-chi-minh", "thue-nha-dat-tp-ho-chi-minh", "thue-phong-tro-tp-ho-chi-minh"]

# Edit 0, 1, 2 to fetch
url = fetch_url[2]
page = 1

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
'referer': main_url + url + '?page=' + str(page),
}

while True:
    time.sleep(0.5)
    print(f'Start to fetch page {page} {url}. Status: ')
    response = requests.get(main_url + url + '?page=' + str(page), headers=headers)
    if response.status_code == 200:
        print('Success\n')
        dom = etree.HTML(response.content)
        elements = dom.xpath('//script[@id="__NEXT_DATA__"]')

        if elements:
            element = elements[0]
            # Convert Unicode string to JSON directly
            json_data = json.loads(element.text)
            data.append(json_data['props']['pageProps']['initialState']['adlisting']['data']['ads'])
            
        else:
            print("Cannot found.")

        page += 1
        if (page == 201):
            break
    else:
        print("Failed, code " + str(response.status_code))

with open("phong-tro.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Success create json file")