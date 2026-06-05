from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        assert "inventory" in driver.current_url

    finally:
        driver.quit()