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
            links.append(suggestion.get_attribute('href') + ' - ' + fish + '\n')
        except:
            links.append('\n')
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
    final_list = []
    for line in f_links:
        line_split = split(' - ', line.replace('\n', ''))
        fish_attributes = [line_split[1].replace(' ', '_')]
        for attr in f_attr:
            try:
                temp = split(' - ', attr.replace('\n', ''))
                driver.get(line + temp[0])
                value = driver.find_element(By.CLASS_NAME, 'trait-val').text
                if value != '?':
                    fish_attributes.append([temp[1].replace(' ', '_'), value])
            except:
                continue
        f_attr.seek(0)
        final_list.append(fish_attributes)
    driver.quit()
    return final_list


def attr_to_n4j(list_of_attr):
    f = open('queries.txt', 'w')
    for fish in list_of_attr:
        query = "CREATE (n:Fish {name:'" + fish[0]
        if len(fish) > 1:
            for i in range(1, len(fish)):
                query += "', " + fish[i][0] + ":'" + fish[i][1]

        query += "'});\n"
        f.write(query)

# find_links()
fish_attr = get_attr()

attr_to_n4j(fish_attr)

