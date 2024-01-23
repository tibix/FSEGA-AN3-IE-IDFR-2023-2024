import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro/")

try:
    # Sign In
    sign_in_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu__link framed-item shiny-item' and contains(text(), 'Sign In')]"))
    )
    sign_in_link.click()

    # Fill in login details
    username_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "login"))
    )
    password_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    login_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "autentificare"))
    )

    username_field.send_keys("tdascal")
    password_field.send_keys("tdascal2")
    login_button.click()

    # Navigate to Reset Password
    user_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu__link framed-item framed-item--dif shiny-item dropdown-toggle account']"))
    )
    user_menu.click()

    reset_password_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='fa-solid fa-key']/ancestor::a[@class='dropdown-item']"))
    )
    reset_password_link.click()

    # Reset Password
    current_password_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "current_password"))
    )
    current_password_field.send_keys("tdascal2")

    new_password_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "new_password"))
    )
    new_password_field.send_keys("tdascal")

    new_password_c_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "new_password_c"))
    )
    new_password_c_field.send_keys("tdascal")

    submit_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "reset_password"))
    )
    submit_button.click()

    if "home.php" in driver.current_url:
        print("Password reset: Successfully.")
    else:
        print("Password reset: Failed!")

except TimeoutException:
    print("Password reset: Failed!")

finally:
    time.sleep(1)
    driver.quit()
