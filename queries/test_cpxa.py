from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from functions.get_click_offsets import get_click_offsets2
from functions.get_webdriver import get_webdriver
from functions.wait_for_all_elements import wait_for_all_elements
from constants.paths import capxa_path, frame, body_xpath, frame_xpath

driver = get_webdriver(isHeadless=False)
driver.get(capxa_path)
wait_for_all_elements(driver,1)
body = driver.find_element(By.XPATH,body_xpath)
body.get_attribute("visibility")
frame = driver.find_element(By.XPATH,frame_xpath)
actions = ActionChains(driver)
def create_click_function(element):
    def click(x, y):
        if x is not None and y is not None:
            actions.move_to_element_with_offset(element, x, y)
            actions.click()
            actions.perform()
    return click
def should_skip_when_frame_visible(whenFrameVisible:bool):
    def call():
        frame_visible = frame.value_of_css_property("visibility") != "hidden"
        if whenFrameVisible:
            return frame_visible
        else:
            return frame_visible is False
    return call
get_click_offsets2(body, create_click_function(body), should_skip_when_frame_visible(True))
get_click_offsets2(frame, create_click_function(frame), should_skip_when_frame_visible(False))
