import atexit
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webelement import WebElement
from constants.paths import chrome_driver_path
from services.log import log

class CustomSwitchTo(SwitchTo):

    def default_content(self) -> None:
        log.info("gone to default content")
        return super().default_content()

    def frame(self, frame_reference) -> None:
        log.info(f"go to frame: {frame_reference}")
        return super().frame(frame_reference)

    def window(self, window_name) -> None:
        log.info(f"switched to new window: {window_name}")
        return super().window(window_name)

    def new_window(self, type_hint=None) -> None:
        log.info(f"gone to new window: {type_hint}")
        return super().new_window(type_hint)

class CustomChromeDriver(webdriver.Chrome):
    def get(self, url):
        log.info(f"gone to url: {url}")
        return super().get(url)

    def find_element(self, by=By.ID, value: str | None = None) -> WebElement:
        log.info(f"looked for information, by:{by}, value:{value}")
        return super().find_element(by, value)

    def find_elements(self, by=By.ID, value: str | None = None) -> List[WebElement]:
        log.info(f"looked for information, by:{by}, value:{value}")
        return super().find_elements(by, value)

    @property
    def switch_to(self) -> CustomSwitchTo:
        return super().switch_to

    @property
    def current_window_handle(self) -> str:
        windowhandle = super().current_window_handle()
        log.info(f"get window handle: {windowhandle}")
        return windowhandle

def addAtEndFunction(driver):
    def cleanup_function():
        driver.quit()
    atexit.register(cleanup_function)

def get_webdriver(
        isHeadless:bool = True,
        isToConnectWithAlreadyExistingTab: bool = False
        ) -> CustomChromeDriver:
    driver_path = chrome_driver_path
    service = ChromeService(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1600,738")
    if isHeadless:
        options.add_argument("--headless=new")
        options.add_argument("--remote-debugging-port=9222")
    if isToConnectWithAlreadyExistingTab:
        options.add_experimental_option("debuggerAddress", "localhost:9239")
    driver = CustomChromeDriver(service=service, options=options)
    addAtEndFunction(driver)
    log.info("got the driver")
    return driver