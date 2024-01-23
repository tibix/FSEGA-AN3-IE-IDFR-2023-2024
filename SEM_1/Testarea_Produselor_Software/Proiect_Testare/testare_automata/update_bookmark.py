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

    username_field.send_keys("test_beatrice")
    password_field.send_keys("123cand")
    login_button.click()

    user_menu = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='menu__link framed-item framed-item--dif shiny-item dropdown-toggle account']"))
    )
    user_menu.click()

    bookmarks_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//i[@class='fa-solid fa-book-bookmark']/ancestor::a[@class='dropdown-item']"))
    )
    bookmarks_link.click()

    bookmark_title_to_edit = "Books-express"
    edit_button_xpath = f"//td[text()='{bookmark_title_to_edit}']/following-sibling::td/a[contains(@class, 'btn btn-outline-primary')]"
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, edit_button_xpath))
    )
    edit_button.click()

    title_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "title"))
    )
    url_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "url"))
    )
    descriere_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "description"))
    )

    
    title_field.clear()
    title_field.send_keys("Books-express-edit")
    titlu_nou="Books-express"
    url_field.send_keys("")
    descriere_field.send_keys("")

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

    if "bookmarks.php" in driver.current_url:
        print("Bookmark edited: Successfully.")
        print(f"Bookmark with title '{titlu_nou}' edited successfully!")
    else:
        print("Bookmark edited: Failed!")

except TimeoutException:
    print("Bookmark edited: Failed!")

finally:
    time.sleep(5)
    driver.quit()
