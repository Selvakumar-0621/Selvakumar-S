from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

def display_cookies(phase):
    cookies = driver.get_cookies()
    print(f"\nCookies {phase} login:")
    for cookie in cookies:
        print(cookie)

# To Display cookies before login
display_cookies("before")

# To Perform login action with the username and password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce" + Keys.RETURN)

# To wait for login to complete
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))

# To Display cookies after login
display_cookies("after")

# To Perform logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

# To wait for logout to complete
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))

# To Display cookies after logout
display_cookies("after logout")

# To Close browser
driver.quit()
