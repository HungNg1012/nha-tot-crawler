import json
import unicodecsv as csv
import numpy as np
import random
import datetime
from unidecode import unidecode
import string
import numpy as np

def preProcess(fileNames):
    rawData = []
    for fileName in fileNames:
        with open(fileName+'.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            rawData.append(data)
    return [element for sublist in rawData for subsublist in sublist for element in subsublist]

def random_date(start_year, end_year):
    # Chọn ngẫu nhiên một năm từ start_year đến end_year
    year = random.randint(start_year, end_year)
    
    # Nếu năm là năm hiện tại, chọn tháng và ngày từ đầu năm đến ngày hiện tại
    if year == datetime.datetime.now().year:
        start_month = 1
        end_month = datetime.datetime.now().month
    else:
        start_month = 1
        end_month = 12
    
    # Chọn ngẫu nhiên một tháng và một ngày từ start_month đến end_month
    month = random.randint(start_month, end_month)
    # Xác định ngày cuối cùng của tháng
    last_day = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    day = random.randint(1, last_day)
    
    # Trả về ngày ngẫu nhiên
    return datetime.date(year, month, day)

def creatEmail(name):
    str_without_diacritics = unidecode(name)
    str_lower = str_without_diacritics.lower()
    str_formatted = str_lower.replace(" ", "")
    email = str_formatted + "@gmail.com"
    return email

def randomPassword():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(random.randint(8, 50)))
    return password

def randomPhoneNumber():
    phone_number = '0' + ''.join(random.choice('0123456789') for _ in range(9))
    return phone_number

# account = {
#     "id": int,
#     "createAt": "",
#     "updatedAt": "",
#     "email": "",
#     "password": "",
#     "phoneNumber": "",
#     "avatarUrl": "",
#     "name": "",
#     "streetNumber": "",
#     "city": "",
#     "district": "",
#     "ward": ""
# }

def extractAccount(data):
    account = []
    for i in data:
        newAccount = dict(id=i['account_id'], name=i['account_name'])   
        newAccount['createdAt'] = random_date(2020,2022).strftime("%Y-%m-%d")
        newAccount['updateAt'] = ""
        newAccount['email'] = creatEmail(i['account_name'])
        newAccount['password'] = randomPassword()
        newAccount['phoneNumber'] = randomPhoneNumber()
        newAccount['streetNumber'] = ""
        newAccount['city'] = ""
        newAccount['district'] = ""
        newAccount['ward'] = ""
        account.append(newAccount)
    return account

# roomingHouse = {
#     "id": int,
#     "createAt": "",
#     "updatedAt": "",
#     "name": "",
#     "cost": "",
#     "area": "",
#     "numberOfBedRooms": "",
#     "numberOfToilets": "",
#     "streetNumber": "",
#     "city": "",
#     "district": "",
#     "ward": "",
#     "LanlordAccountId": "",
# }

def extractHouse(data):
    house = []
    for i in [data]:
        newHouse = dict(id=i['ad_id'], 
                        name=i['subject'], 
                        cost=i['price'], area=i['size'], 
                        numberOfBedRooms=i['rooms'] if 'rooms' in i else "", 
                        numberOfToilets=i['toilets']  if 'toilets'  in i else "", 
                        streetNumber=(i['street_number']  + ' ') if 'street_number'  in i else "" + i['street_name'] if 'street_name'  in i else "",
                        city=i['region_name'] if 'region_name'  in i else "",\
                        district=i['area_name'] if 'area_name'  in i else "",
                        ward=i['ward_name'] if 'ward_name'  in i else "",
                        lanlordAccountId=i['account_id'])   
        newHouse['type'] = type
        newHouse['createAt'] = random_date(2022, 2024)
        newHouse['updatedAt'] = ""
        house.append(newHouse)
    return house

if __name__ == "__main__":
    data = preProcess(['can-ho', 'nha-dat', 'phong-tro'])
    account = extractAccount(data)
    house = extractHouse(data)
    
    with open('./output/account.csv','wb') as csv_file:
        csv_writer = csv.writer(csv_file, encoding="utf-8")
        
        count = 0
        for data in account:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        csv_file.close()

    with open('./output/roomingHouse.csv','wb') as csv_file:
        csv_writer = csv.writer(csv_file, encoding="utf-8")
        
        count = 0
        for data in house:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        csv_file.close()
    print("Done!")