from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Specify the path to the web driver executable
driver_path = "C:\\utils\\chromedriver.exe"

# Create a new instance of the web driver
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

# Navigate to the desired URL
url = 'https://google.com'
driver.get(url)

# Save the page source to a file
with open('page.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

# Close the browser
driver.quit()
