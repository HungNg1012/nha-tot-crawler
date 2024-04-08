from lxml import etree
from bs4 import BeautifulSoup
import requests
import json
import csv
import time

url = "https://www.nhatot.com/thue-can-ho-chung-cu-tp-ho-chi-minh"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'referer': 'https://www.nhatot.com/thue-can-ho-chung-cu-tp-ho-chi-minh'
}

loop = 1
while True:
    time.sleep(2)
    print(f'Start to fetch {loop} times. Status: ')
    response = requests.get(url, headers=headers)
    loop += 1

    if response.status_code == 200:
        print('Success\n')
        dom = etree.HTML(response.content)
        elements = dom.xpath('//script[@id="__NEXT_DATA__"]')

        if elements:
            element = elements[0]

            # Convert Unicode string to JSON directly
            json_data = json.loads(element.text)
            with open("can-ho.json", "w", encoding="utf-8") as f:
                json.dump(json_data['props']['pageProps']['initialState']['adlisting'], f, ensure_ascii=False, indent=4)
        else:
            print("Cannot found.")

        break
    else:
        print("Failed, code " + str(response.status_code))
