import json
import csv
import unicodecsv
import numpy as np
import random
import datetime
from unidecode import unidecode
import string
import pandas as pd

csv_file_path = './output/roomingHouse.csv'
df = pd.read_csv(csv_file_path)
# df.drop('year', inplace=True, axis=1)
# Step 2: Define the values for the new "City" column
newVal = []
for i in range(1,12001):
    if (i <= 4001): newVal.append('can_ho')
    elif (i <= 8001): newVal.append('nha_dat')
    else: newVal.append('phong_tro')
 
# Step 3: Add the new "City" column to the DataFrame
df['type'] = newVal
 
# Step 4: Write the DataFrame back to the CSV file
df.to_csv(csv_file_path, index=False)