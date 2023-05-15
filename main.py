import csv
from re import split
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pynput.keyboard import Key, Controller


def find_links():
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

    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options)

    driver.get("https://eol.org")
    input = driver.find_element(By.ID, 'q')

    links = []
    for fish in fishes:
        input.send_keys(fish)
        sleep(3)
        try:
            suggestion = driver.find_element(By.CSS_SELECTOR, 'div.tt-suggestion>a:first-child')
            links.append(suggestion.get_attribute('href'))
        except:
            links.append(None)
        input.send_keys(Keys.CONTROL + "a")
        input.send_keys(Keys.DELETE)

    f = open("links.txt", "w")
    for link in links:
        f.write(link)
    f.close()


def get_attr():
    f_links = open("links.txt", 'r')
    f_attr = open("value_links.txt", 'r')
    driver = webdriver.Chrome()
    for line in f_links:
        for attr in f_attr:
            temp = split(' - ', attr)
            driver.get(line + temp[0])
            # TODO
            # read attributes and write them to some array to later create queries for database


    driver.quit()

attrPerFish = []
get_attr()

