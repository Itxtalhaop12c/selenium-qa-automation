
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Starting Empty Password Test...")

driver = webdriver.Edge()
wait = WebDriverWait(driver, 10)

try:
    # Open login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Enter username only
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Leave password empty

    # Click login
    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    # Wait for error message
    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    # Verify rejection
    if "Your password is invalid!" in message.text:
        print("TEST RESULT: PASS")
        print("Empty password correctly rejected.")
    else:
        print("TEST RESULT: FAIL")
        print("Unexpected response:", message.text)

    input("Press Enter to close browser...")

except Exception as e:
    print("TEST RESULT: FAIL")
    print("Error:", e)

finally:
    driver.quit()
