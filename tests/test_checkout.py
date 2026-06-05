import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_checkout():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        # Add Product
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        # Open Cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Checkout
        driver.find_element(By.ID, "checkout").click()

        # Customer Details
        driver.find_element(By.ID, "first-name").send_keys("Hemant")
        driver.find_element(By.ID, "last-name").send_keys("Wagh")
        driver.find_element(By.ID, "postal-code").send_keys("411001")

        driver.find_element(By.ID, "continue").click()

        # Finish Order
        driver.find_element(By.ID, "finish").click()

        success_msg = driver.find_element(By.CLASS_NAME, "complete-header")

        print(success_msg.text)

        assert "Thank you for your order!" in success_msg.text

        print("✅ Checkout Test Passed")

        time.sleep(2)

    finally:
        driver.quit()