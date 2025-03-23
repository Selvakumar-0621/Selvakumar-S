from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To Initialize WebDriver
driver = webdriver.Chrome()

# To Open Instagram Guvi page
driver.get("https://www.instagram.com/guviofficial/")

# To Wait for the page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'x78zum5')]")))

# Xpath of followers and following
followers_xpath = "//ul[contains(@class, 'x78zum5')]/li[2]//span"
following_xpath = "//ul[contains(@class, 'x78zum5')]/li[3]//span"

followers = driver.find_element(By.XPATH, followers_xpath).text
following = driver.find_element(By.XPATH, following_xpath).text

# To Print extracted details
print(f"Total number of Followers: {followers}")
print(f"Total number of Following: {following}")

# To Close browser
driver.quit()