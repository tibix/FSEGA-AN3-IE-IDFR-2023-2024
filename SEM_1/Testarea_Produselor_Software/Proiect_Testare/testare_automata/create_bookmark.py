import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

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
    password_field.send_keys("tdascal")
    login_button.click()

    add_bookmark_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[@href="new_bookmark.php" and contains(@class, "btn-outline-primary")]'))
    )

    add_bookmark_button.click()

    title_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "title"))
    )
    url_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "url"))
    )
    descriere_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "description"))
    )

    title_cat="Books-express"
    title_field.send_keys("Books-express")
    url_field.send_keys("https://www.carturesti.ro/")
    descriere_field.send_keys("Books-express ")

    desired_category = "Shopping"

    category_dropdown = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "category"))
    )
    category_select = Select(category_dropdown)
    category_select.select_by_visible_text(desired_category)

    submit_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "save"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(1)

    if "new_bookmark.php" in driver.current_url:
        print("Bookmark added: Successfully.")
        print(f"Bookmark with title '{title_cat}' added successfully!")
    else:
        print("Bookmark added: Failed!")

except TimeoutException:
    print("Bookmark added: Failed!")

finally:
    time.sleep(5)
    driver.quit()
