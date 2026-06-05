import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

def test_logout():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        driver.find_element(By.ID, "react-burger-menu-btn").click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )

        assert driver.find_element(By.ID, "user-name").is_displayed()

        print("✅ Logout Test Passed")

    finally:
        driver.quit()   