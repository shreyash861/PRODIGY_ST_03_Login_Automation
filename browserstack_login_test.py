from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

USERNAME = "shreyashgautamsu_UO9G8d"
ACCESS_KEY = "riuTCBwWy7o8sj3zjGqG"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

browsers = [
    {"browser": "Chrome", "os": "Windows", "os_version": "11"},
    {"browser": "Firefox", "os": "Windows", "os_version": "11"},
    {"browser": "Edge", "os": "Windows", "os_version": "11"},
    {"browser": "Safari", "os": "OS X", "os_version": "Ventura"},
]

for config in browsers:
    options = Options()
    options.set_capability("browserName", config["browser"])
    options.set_capability("os", config["os"])
    options.set_capability("osVersion", config["os_version"])
    options.set_capability("name", f"Login Test on {config['browser']}")

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(2)

        message = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in message

        print(f"{config['browser']} → PASS")

    except Exception as e:
        print(f"{config['browser']} → FAIL :", e)

    finally:
        driver.quit()
