import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

URL = 'https://zno.osvita.ua/mathematics/346/'
# URL = 'https://zno.osvita.ua/geography/434/'


def submit_form(driver):
    timeout = 10

    div = driver.find_element_by_id('q1')
    table = div.find_element_by_class_name('select-answers-variants')
    # inp = table.find_element_by_xpath('//input[@value="a"]')
    # answer = inp.parent.find_element_by_xpath('//span[@class="marker"]')
    label = table.find_element_by_xpath('//label')
    answer = label.find_element_by_xpath('//span[@class="marker"]')
    driver.execute_script("arguments[0].scrollIntoView(true)", answer)
    answer.click()

    WebDriverWait(driver, timeout).until(
        expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                '//span[contains(text(), "Завершити тест")]'
            )
        )
    ).click()
    time.sleep(3)


def get_html(url, save_to_file=True):
    chrome_driver = 'chromedriver.exe'

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--disable-blink-features=AutomationControlled')

    capabilities = DesiredCapabilities.CHROME
    capabilities["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(executable_path=chrome_driver, desired_capabilities=capabilities, options=options)
    driver.get(url)

    time.sleep(3)
    driver.execute_script("window.stop()")

    submit_form(driver)

    if save_to_file:
        url_split = url[:-1].split('/')
        file_name = url_split[-2] + url_split[-1] + '.html'
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

    html = driver.page_source
    driver.close()
    return html


if __name__ == '__main__':
    print(get_html(URL))
