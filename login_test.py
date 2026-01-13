from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

# POSITIVE TEST
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
print("Positive login test passed")

# NEGATIVE TEST - INVALID
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
print("Invalid login test passed")

# NEGATIVE TEST - EMPTY
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)
print("Empty field test passed")

driver.quit()
