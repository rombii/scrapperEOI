import csv
from re import split
from selenium import webdriver
from selenium.webdriver.common.by import By

f = open('lakes.csv')

csvF = csv.reader(f)

header = []
header = next(csvF)

rows = []
for row in csvF:
    rows.append(row)
fishes = []
for row in rows:
    for fish in split(" - ", row[5]):
        if not fish in fishes:
            fishes.append(fish)

print(fishes)

driver = webdriver.Chrome()

driver.get("https://eol.org")
driver.find_element(By.ID, 'q').click()

driver.close()