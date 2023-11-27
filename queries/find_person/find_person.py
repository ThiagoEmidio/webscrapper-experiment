from bs4 import BeautifulSoup
import csv
from functions.get_webdriver import get_webdriver
from functions.save_page_source import save_page_source
from functions.wait_for_all_elements import wait_for_all_elements
import paths as path

driver = get_webdriver(isHeadless=False)
driver.get(path.link_corpo)
wait_for_all_elements(driver,2)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
word_counts = {}

with open("queries\find_person\functions\score_words.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        # Assuming the words are in the first column
        word = row[0].strip()
        word_counts[word] = 0  # Ini

all_text = soup.get_text()

for word in word_counts.keys():
    count = all_text.lower().count(word.lower())  # Case-insensitive count
    word_counts[word] = count

word_counts = {word: count for word, count in word_counts.items() if count > 0}

print(word_counts)