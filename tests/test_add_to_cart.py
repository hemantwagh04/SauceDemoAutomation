import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_add_to_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        print("Cart Count =", cart_badge.text)

        assert cart_badge.text == "1"

        print("✅ Add To Cart Test Passed")

        time.sleep(2)

    finally:
        driver.quit()