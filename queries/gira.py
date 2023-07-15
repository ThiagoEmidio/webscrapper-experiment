import clipboard
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from functions.get_webdriver import get_webdriver
from functions.wait_for_all_elements import wait_for_all_elements
from services.log import log

driver = get_webdriver(isHeadless=False, isToConnectWithAlreadyExistingTab=True)
with open("notfound.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for x,text in reader:
        if x != "Id":
# for x in range(13,35):
            driver.get(f"https://app.qase.io/project/TRIMTRI?case={x}&previewMode=modal&suite=9&view=1")
            wait_for_all_elements(driver,3.5)
            if len(driver.find_elements(By.CSS_SELECTOR,".nBLXOa"))==0:
                log.info("not found yet")
                nameofIssue = driver.find_element(By.CSS_SELECTOR,".gMQ1n6").text.strip()
                #find button to link
                driver.find_element(By.CSS_SELECTOR,".oJlblK").click()
                wait_for_all_elements(driver,0.5)
                clipboard.copy(nameofIssue)
                driver.find_element(By.CSS_SELECTOR,".XRXnTf").click()
                wait_for_all_elements(driver,0.5)
                driver.find_element(By.CSS_SELECTOR,".XRXnTf").send_keys(Keys.CONTROL+'v')
                driver.find_element(By.CSS_SELECTOR,".X9y516 > span:nth-child(2)").click()
                wait_for_all_elements(driver,1)
                if len(driver.find_elements(By.CSS_SELECTOR,".TOrbtp"))!=0:
                    log.info("FoundLinkage")
                    text = driver.find_element(
                        By.CSS_SELECTOR,
                        ".TOrbtp > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)").text
                    if text == nameofIssue:
                        log.info("is correct")
                        driver.find_element(
                            By.CSS_SELECTOR,
                            ".TOrbtp > tbody:nth-child(2) > tr:nth-child(1) > " +
                            "td:nth-child(5) > button:nth-child(1)").click()
                        wait_for_all_elements(driver,3)
                        while len(driver.find_elements(By.CSS_SELECTOR,".ic9QAx"))==0:
                            wait_for_all_elements(driver,1)
                    else:
                        log.info(f"could not find the corrrect name: |{x}|{nameofIssue}")
                else:
                    log.info(f"not able to find the result:|{x}|{nameofIssue}")
            else:
                log.info(f"already linked: {x}")
                continue
