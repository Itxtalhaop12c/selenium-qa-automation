
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Starting Login Test...")

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    # Open login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Enter username
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Enter password
    driver.find_element(By.ID, "password").send_keys(
        "SuperSecretPassword!"
    )

    # Click login button
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Verify successful login
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.TAG_NAME, "h2")
        )
    )

    if heading.text == "Secure Area":
        print("TEST RESULT: PASS")
        print("Login successful!")
    else:
        print("TEST RESULT: FAIL")

    input("Press Enter to close the browser...")

except Exception as e:
    print("TEST RESULT: FAIL")
    print("Error:", e)

finally:
    driver.quit()

