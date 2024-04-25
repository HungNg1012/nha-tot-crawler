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

def extractImage(data):
    image = []
    for i in data:
        newImage = dict(id=i['ad_id'])
        newImage['images'] = []
        newImage['images'].append(i['avatar'] if 'avatar' in i else None)
        newImage['images'].append(i['image'] if 'image' in i else None)
        image.append(newImage)
    return image

if __name__ == "__main__":
    data = preProcess(['can-ho', 'nha-dat', 'phong-tro'])
    image = extractImage(data)
    with open('./output/image.csv','wb') as csv_file:
        csv_writer = csv.writer(csv_file, encoding="utf-8")
        
        count = 0
        for data in image:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        csv_file.close()
    print("Done!")