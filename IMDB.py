from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Step 1: Visit IMDb Search page
driver.get('https://www.imdb.com/search/name/')

# Step 2: Explicit Wait to ensure the elements are loaded
wait = WebDriverWait(driver, 10)

# Wait until the name input field is present
name_field = driver.find_element(By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label")
name_field.send_keys("M. Manikandan")

# Fill in the Birthdate
BirthDay_field = driver.find_element(By.XPATH, "//*[@id='birthdayAccordion']/div[1]/label")
BirthDay_field.send_keys("02-13")

# To Perform the search
see_results = driver.find_element(By.XPATH, "//*[@id='__next']/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button")

# To Close the driver
driver.quit()
