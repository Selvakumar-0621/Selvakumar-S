"""
Program to login into a web page with given username and password and fetch
title of webpage, current url & create a text consisting the entire content of the web page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SauceDemoAutomation:

    def __init__(self, username, password):
                                                                    # Method to Initialize the Chrome driver with options
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.options)
        self.username = username
        self.password = password



    def login(self, url):                          # Method to tpen the SauceDemo URL and log in

        self.driver.get(url)
        self.driver.find_element(By.ID, "user-name").send_keys(self.username)
        self.driver.find_element(By.ID, "password").send_keys(self.password)
        time.sleep(2)



    def get_page_title(self):                      # Method to get the title of the web page
        return self.driver.title




    def get_current_url(self):                    # Method to get the current URL of the web page
        return self.driver.current_url



    def save_page_content(self, filename):   # Method to Extract the page source and save it to a file

        page_content = self.driver.page_source
        with open(filename, "w", encoding="utf-8") as file:
            file.write(page_content)
        print(f"Page content saved to '{filename}'")




    def close_browser(self):                     # Method to close the browser
        self.driver.quit()



# Main function to all the class created
def main():
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    filename = "Webpage_task_11.txt"



    # Creating an instance of the SauceDemoAutomation class
    automation = SauceDemoAutomation(username, password)


    try:
        automation.login(url)
        print("Title of the web page:", automation.get_page_title())
        print("Current URL of the web page:", automation.get_current_url())
        automation.save_page_content(filename)

    finally:
        automation.close_browser()




# Run the main function
if __name__ == "__main__":
    main()
