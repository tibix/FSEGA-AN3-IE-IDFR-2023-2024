from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro/login.php")

try:

    username_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
except TimeoutException as e:
    print("Timed out waiting for the username field to be present.")
    raise e


password_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "password"))
)


login_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.NAME, "autentificare"))
)


username_field.send_keys("bmov")
password_field.send_keys("bla")

login_button.click()
time.sleep(5)

# Check if an error message is present indicating incorrect username or password
try:
    error_message_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "alert-danger")]'))
    )
    print("Login Failed! Incorrect username or password.")
except TimeoutException:
    # If there is no error message, consider the login successful
    print("Login Successful!")

driver.quit()
