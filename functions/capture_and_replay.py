
from selenium.webdriver.common.action_chains import ActionChains
from functions.get_click_offsets import get_click_offsets

def capture_and_replay(driver, element,once=False):
    offset_x, offset_y = get_click_offsets(element, once)
    if offset_x is not None and offset_y is not None:
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(element, offset_x, offset_y)
        actions.click()
        actions.perform()
