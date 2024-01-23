import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://testare.itdev.ro")

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

    username_field.send_keys("test_beatrice")
    password_field.send_keys("123cand!")
    login_button.click()

    # Navigate to Reset Password
    user_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu__link framed-item framed-item--dif shiny-item dropdown-toggle account']"))
    )
    user_menu.click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'logout.php')]"))
    )
    logout_button.click()
    if "index.php" in driver.current_url:
        print("Log Out: Successfully.")
    else:
        print("Log Out: Failed!")

except TimeoutException:
    print("Log Out: Failed!")

finally:
    time.sleep(3)
    driver.quit()