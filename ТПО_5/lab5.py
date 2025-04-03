from time import sleep

from opencard_driver import create_driver, scroll_to, delete_element
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = create_driver()
sleep(20)
# Поле поиска
search = driver.find_element(By.ID, "search").find_element(By.TAG_NAME, "input")
search.send_keys("MacBook")
search.send_keys(Keys.RETURN)
assert "There is no product that matches the search criteria" not in driver.page_source

# Результаты поиска
product_list = driver.find_element(By.ID, "product-list")
first_product = product_list.find_element(By.CLASS_NAME, "product-thumb")
add_to_card_button = first_product.find_element(By.CLASS_NAME, "fa-shopping-cart")
scroll_to(driver, add_to_card_button)
add_to_card_button.click()
sleep(0.5)

# Удаляем всплывающее окно
delete_element(driver, driver.find_element(By.CLASS_NAME, "alert"))

# Переход в корзину
card_link = driver.find_element(By.XPATH, "//li[contains(., 'Shopping Cart')]")
scroll_to(driver, card_link)
card_link.click()

# Смотрим на товар
cart_table_row = driver.find_element(By.XPATH, "//div[@id='shopping-cart']//tbody/tr")
assert "MacBook" in cart_table_row.find_elements(By.TAG_NAME, "td")[1].text

sleep(5)
driver.quit()
