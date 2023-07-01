
def save_page_source(driver):
    with open('page.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
