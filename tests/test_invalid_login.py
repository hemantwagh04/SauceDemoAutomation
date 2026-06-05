import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_invalid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login("wrong_user", "wrong_password")

        error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

        print("Error Message =", error_message.text)

        assert "Username and password do not match" in error_message.text

        print("✅ Invalid Login Test Passed")

        time.sleep(2)

    finally:
        driver.quit()