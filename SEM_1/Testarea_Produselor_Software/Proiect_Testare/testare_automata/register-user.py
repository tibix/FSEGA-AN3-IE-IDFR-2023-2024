import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro/register.php")

try:
    registration_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "inregistrare"))
    )

    username_field = registration_form.find_element(By.ID, "user_name")
    firstname_field = registration_form.find_element(By.ID, "first_name")
    lastname_field = registration_form.find_element(By.ID, "last_name")
    email_field = registration_form.find_element(By.ID, "email")
    language_dropdown = Select(registration_form.find_element(By.ID, "language"))
    language_dropdown.select_by_value("no_language")

    password_field = registration_form.find_element(By.ID, "password")
    password_confirm_field = registration_form.find_element(By.ID, "password_c")

    submit_button = registration_form.find_element(By.NAME, "register")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    username_field.send_keys("testuser_5")
    firstname_field.send_keys("Test")
    lastname_field.send_keys("User")
    email_field.send_keys("testuser@testuser5.com")
    language_dropdown.select_by_value("en")
    password_field.send_keys("123cand")
    password_confirm_field.send_keys("123cand")

    driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(5)

    login_form = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    print("Registration Successful!")
except TimeoutException:
        print("Registration Failed!")

driver.quit()
