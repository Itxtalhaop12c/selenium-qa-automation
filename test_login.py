
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Edge()
    yield browser
    browser.quit()


def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys(
        "SuperSecretPassword!"
    )
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    heading = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h2")
        )
    )

    assert heading.text == "Secure Area"


def test_invalid_password(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "Your password is invalid!" in message.text


def test_empty_username(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "password").send_keys(
        "SuperSecretPassword!"
    )

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "Your username is invalid!" in message.text


def test_empty_password(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    assert "Your password is invalid!" in message.text
