import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro/login.php")

try:
    recovery_link = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Reset Password"))
    )
    recovery_link.click()

    email_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys("test@beatrice.com")

    submit_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "recover_password"))
    )
    submit_button.click()

    new_password_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "new_password"))
    )
    new_password_field.send_keys("123cand!")
    new_password_c_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "new_password_c"))
    )
    new_password_c_field.send_keys("123cand!")

    submit_button_2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "recover_password"))
    )
    submit_button_2.click()

    login_form = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "here"))
    )
    print("Password reset: Successful!")
except TimeoutException:
    print("Password reset: Failed!")

driver.quit()