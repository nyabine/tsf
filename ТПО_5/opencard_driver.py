import os.path
import pickle
from time import sleep

import undetected_chromedriver as webdriver


def create_driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.opencart.com/")

    if os.path.isfile('cookies.pkl'):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://demo.opencart.com/")

    while "needs to review the security" in driver.page_source:
        print("Please, solve captcha")
        sleep(1)

    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    return driver


def scroll_to(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(1.5)


def delete_element(driver, element):
    driver.execute_script('arguments[0].remove();', element)
