import atexit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from constants.paths import chrome_driver_path
from services.log import log

def addAtEndFunction(driver):
    def cleanup_function():
        driver.quit()
    atexit.register(cleanup_function)

def get_webdriver(
        isHeadless:bool = True,
        isToConnectWithAlreadyExistingTab: bool = False
        ) -> ChromiumDriver:
    driver_path = chrome_driver_path
    service = ChromeService(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    if isHeadless:
        options.add_argument("--headless=new")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--window-size=1600,738")
        print(options.arguments)
    if isToConnectWithAlreadyExistingTab:
        options.add_experimental_option("debuggerAddress", "localhost:9222")
    driver = webdriver.Chrome(service=service, options=options)
    addAtEndFunction(driver)
    log.info("got the driver")
    return driver
