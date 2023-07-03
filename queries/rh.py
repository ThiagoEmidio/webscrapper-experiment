import csv
from bs4 import BeautifulSoup
from functions.extract_dates import extract_dates
from functions.extract_emails import extract_emails
from functions.get_webdriver import get_webdriver
from functions.save_page_source import save_page_source
from functions.wait_for_all_elements import wait_for_all_elements
from constants.paths import rh_path, rh_output_path

driver = get_webdriver(isHeadless=False)
driver.get(rh_path)
wait_for_all_elements(driver,2)
save_page_source(driver)

with open("page.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')
cardbody_elements = soup.find_all(class_='card-body')


data:list[dict()] = []
for element in cardbody_elements:
    if "Requisitos" in element.text:
        item = dict()

        listOfStrings = element.text.split("\n")
        listOfStrings = list(filter(lambda string: string != "", listOfStrings))
        item["titulo"] = listOfStrings[0]
        for index, string in enumerate(listOfStrings):
            if string == "Requisitos":
                item["Requisitos"] = listOfStrings[index+1]
            if string == "Atividades":
                item["Atividades"] = listOfStrings[index+1]
            if string == "Benefícios":
                item["Benefícios"] = listOfStrings[index+1]
            if string == "Observações":
                item["Observações"] = listOfStrings[index+1] + listOfStrings[index+2]
                item["Email"] = extract_emails(item["Observações"] or "")
            if "Inserida em" in string:
                [item["Inserida"], item["Até"]] = extract_dates(string)
        print(item)
        data.append(item)
fieldnames = data[0].keys()
with open(rh_output_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(data)  # Write the dictionary rows
