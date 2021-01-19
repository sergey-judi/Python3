import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


def submit_form(driver):
    timeout = 100

    div = driver.find_element_by_id('q1')
    table = div.find_element_by_class_name('select-answers-variants')
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


def get_html(url):
    chrome_driver = 'chromedriver.exe'

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('--disable-blink-features=AutomationControlled')

    capabilities = DesiredCapabilities.CHROME
    capabilities["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome(executable_path=chrome_driver, options=options, desired_capabilities=capabilities)
    driver.get(url)

    time.sleep(3)
    driver.execute_script("window.stop()")

    submit_form(driver)

    html = driver.page_source
    driver.close()
    return html
