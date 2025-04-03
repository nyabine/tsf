from random import randint
from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from opencard_driver import create_driver, delete_element, scroll_to


@pytest.fixture(scope="session")
def driver():
    return create_driver()


@pytest.mark.order(1)
def test_find_macbook(driver):
    # Поле поиска
    search = driver.find_element(By.ID, "search").find_element(By.TAG_NAME, "input")
    search.send_keys("MacBook")
    search.send_keys(Keys.RETURN)
    assert "There is no product that matches the search criteria" not in driver.page_source


@pytest.mark.order(2)
def test_add_to_cart(driver):
    product_list = driver.find_element(By.ID, "product-list")
    first_product = product_list.find_element(By.CLASS_NAME, "product-thumb")
    add_to_card_button = first_product.find_element(By.CLASS_NAME, "fa-shopping-cart")
    scroll_to(driver, add_to_card_button)
    add_to_card_button.click()
    sleep(0.5)

    delete_element(driver, driver.find_element(By.CLASS_NAME, "alert"))
    card_link = driver.find_element(By.XPATH, "//li[contains(., 'Shopping Cart')]")
    scroll_to(driver, card_link)

    card_link.click()
    cart_table_row = driver.find_element(By.XPATH, "//div[@id='shopping-cart']//tbody/tr")

    assert "MacBook" in cart_table_row.find_elements(By.TAG_NAME, "td")[1].text


@pytest.mark.order(3)
def test_delete_from_cart(driver):
    cart_table_row = driver.find_element(By.XPATH, "//div[@id='shopping-cart']//tbody/tr")
    cart_delete_button = cart_table_row.find_element(By.CLASS_NAME, 'btn-danger')
    cart_delete_button.click()
    sleep(1)

    assert "Your shopping cart is empty" in driver.page_source


@pytest.mark.order(4)
def test_register(driver):
    my_account_link = driver.find_element(By.XPATH, "//li[contains(., 'My Account')]")
    my_account_link.click()
    register_link = driver.find_element(By.XPATH, "//a[contains(., 'Register')]")
    register_link.click()

    # Форма
    driver.find_element(By.ID, 'input-firstname').send_keys('test')
    driver.find_element(By.ID, 'input-lastname').send_keys('test')
    driver.find_element(By.ID, 'input-email').send_keys(f'test{randint(0, 99999)}@test.te')
    driver.find_element(By.ID, 'input-password').send_keys('test')
    driver.find_element(By.XPATH, "//div[@class='text-end']//input").click()

    # Отправляем запрос
    driver.find_element(By.XPATH, "//div[@class='text-end']//button").click()
    sleep(1)
    assert "Your Account Has Been Created" in driver.page_source

    # Выходим из аккаунта
    my_account_link = driver.find_element(By.XPATH, "//li[contains(., 'My Account')]")
    my_account_link.click()
    logout_link = driver.find_element(By.XPATH, "//a[contains(., 'Logout')]")
    logout_link.click()


@pytest.mark.order(5)
def test_login(driver):
    my_account_link = driver.find_element(By.XPATH, "//li[contains(., 'My Account')]")
    my_account_link.click()
    login_link = driver.find_element(By.XPATH, "//a[contains(., 'Login')]")
    login_link.click()

    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(f'amogus@amogus.ni')
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys('amogus')
    driver.find_element(By.XPATH, "//button[contains(., 'Login')]").click()
    sleep(1)

    assert "My Affiliate Account" in driver.page_source
