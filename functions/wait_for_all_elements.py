import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from functions.normRNG import normRNG


def wait_for_all_elements(driver, randomWaitAvg=0, timeout=3):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located)
        if randomWaitAvg>0:
            time.sleep(normRNG(randomWaitAvg))
    except TimeoutException:
        print("Timed out waiting for all elements to be located.")
