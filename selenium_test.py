
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("DevOps")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        lambda d: d.title != "Google"
    )

    print("Page Title:", driver.title)

finally:
    driver.quit()
