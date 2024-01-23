from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro")

try:

    sign_in_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu__link framed-item shiny-item' and contains(text(), 'Sign In')]"))
    )
    sign_in_link.click()

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


username_field.send_keys("tdascal")
password_field.send_keys("tdascal")

login_button.click()
time.sleep(5)
try:
    link_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "home.php")]'))
    )
    print("Login Successful!")
except TimeoutException:
    print("Login Failed!")

driver.quit()
