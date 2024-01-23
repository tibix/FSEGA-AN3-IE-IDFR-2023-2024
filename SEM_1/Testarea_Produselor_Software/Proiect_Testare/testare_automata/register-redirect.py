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
    # Find the "Register" link and click on it
    register_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
    )
    register_link.click()

    # Wait for the registration page to load
    registration_page_title = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "inregistrare"))
    )

    # Check if the URL contains "register.php"
    if "register.php" in driver.current_url:
        print("Clicked on Register link, redirected to register.php. Registration page loaded successfully.")
    else:
        print("Clicked on Register link, but not redirected to register.php. Registration page load failed.")
    time.sleep(5)
except TimeoutException as e:
    print("Timed out waiting for the Register link to be present.")
    raise e

driver.quit()
