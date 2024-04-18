import json
import time
import requests
from lxml import etree

rawData = []
for fileName in ['can-ho', 'nha-dat', 'phong-tro']:
    with open(fileName+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        rawData.append(data)
data = [element for sublist in rawData for subsublist in sublist for element in subsublist]

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
'referer': "https://www.nhatot.com/thue-nha-dat-quan-phu-nhuan-tp-ho-chi-minh/",
}

num = 1
newData = []
for i in data:
    list_id = i['list_id']
    while True:
        time.sleep(0.5)
        print(f'Start to fetch {num}/12000 id {list_id}. Status: ')
        response = requests.get("https://www.nhatot.com/thue-nha-dat-quan-phu-nhuan-tp-ho-chi-minh/" + str(list_id) + ".htm", headers=headers)
        if response.status_code == 200:
            print('Success\n')
            dom = etree.HTML(response.content)
            elements = dom.xpath('//p[@class="styles_adBody__vGW74"]')

            if elements:
                element = elements[0]
                newHouse = dict(id=i['ad_id'], 
                        name=i['subject'], 
                        cost=i['price'], area=i['size'], 
                        numberOfBedRooms=i['rooms'] if 'rooms' in i else "", 
                        numberOfToilets=i['toilets']  if 'toilets'  in i else "", 
                        # numberOfFloors=i['floors']  if 'floors'  in i else "",
                        streetNumber=(i['street_number']  + ' ') if 'street_number'  in i else "" + i['street_name'] if 'street_name'  in i else "",
                        city=i['region_name'] if 'region_name'  in i else "",\
                        district=i['area_name'] if 'area_name'  in i else "",
                        ward=i['ward_name'] if 'ward_name'  in i else "",
                        lanlordAccountId=i['account_id']) 
                newHouse['description'] = element.text
                newData.append(newHouse)
            else:
                print("Cannot found.")
            num += 1
            break
        else:
            print("Failed, code " + str(response.status_code))

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(newData, f, ensure_ascii=False, indent=4)