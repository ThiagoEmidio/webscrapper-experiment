
import pdb
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from functions.capture_and_replay import capture_and_replay
from functions.generate_random_hash import generate_random_hash
from functions.get_webdriver import get_webdriver
# from functions.save_page_source import save_page_source
from functions.wait_for_all_elements import wait_for_all_elements
from constants.paths import sm_path, frame, cap
from services.log import log


driver = get_webdriver(isHeadless=False)
driver.get(sm_path)
wait_for_all_elements(driver,2)
log.info("got to sm")
# save_page_source(driver)
tab1 = driver.current_window_handle
buttom = driver.find_element(
    By.XPATH,
    '//button[contains(text(), "ddit") and@role="button" and @tabindex="0"]',
    )
buttom.click()
# driver.switch_to.new_window("tab")
# tab2 = driver.current_window_handle
# driver.get(gmail_path)
# wait_for_all_elements(driver,2)
# driver.find_element(By.XPATH,'//label[@for="use-alias"]').click()
# email = driver.find_element(By.XPATH,'//span[@id="email-widget"]').text
# log.info("got to email")
# with open(email_output_path, 'a+', encoding="utf-8") as file:
#     writer = csv.writer(file)
#     if file.tell() == 0:
#         writer.writerow(['Email', 'Email2'])
#     writer.writerow([email,email])
# driver.switch_to.window(tab1)
email = "dsfylhuc@sharklasers.com"
wait_for_all_elements(driver,3)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
driver.find_element(By.XPATH,'//*[@id="regEmail"]').click()
driver.find_element(By.XPATH,'//*[@id="regEmail"]').send_keys(email)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
wait_for_all_elements(driver,1)
user = driver.find_element(By.XPATH,'//*[@id="regUsername"]').get_attribute("value")
psw = generate_random_hash()
driver.find_element(By.XPATH,'//*[@id="regPassword"]').send_keys(psw)
actions = ActionChains(driver)

actions.send_keys(Keys.TAB)
actions.perform()
wait_for_all_elements(driver,3)
element = driver.find_element(By.XPATH,f'//*[@title="{cap}"]')
capture_and_replay(driver,element)
wait_for_all_elements(driver,2)
element = driver.find_element(By.XPATH,f'//*[@title="{cap}"]')
# driver.switch_to.default_content()
element = driver.find_element(By.XPATH,f'//*[contains(@src,"{frame}")]')
while driver.find_element(By.XPATH,f'//*[contains(@src,"{frame}")]') == element:
    capture_and_replay(driver,element)

text = driver.find_element(By.XPATH,'//*[@class="AnimatedForm__errorMessage"]')


pdb.set_trace()
log.info("turned in email")