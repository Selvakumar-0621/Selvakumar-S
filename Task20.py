from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class MovingBetweenWindows:
    #Driver Initialization
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.faq_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
        self.partners_locator = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"

    def windows(self):
        try:
            self.driver.get(url)                                        # To open the given URL
            self.driver.maximize_window()                               # To Maximize the window
            sleep(2)

            parent_window_handle = self.driver.current_window_handle   #To get parent window ID#
            print("Window ID of Homepage", parent_window_handle)

            # To Click on "Create FAQ" and open a new window
            self.driver.find_element(by=By.XPATH, value=self.faq_locator).click()

            # To Click on "Partners" and open a new window

            self.driver.find_element(by=By.XPATH, value=self.partners_locator).click()

            # To print Frame ID od two opened windows
            all_window_handle = self.driver.window_handles
            print(all_window_handle)

            # To close new windows
            for windows in all_window_handle:
                if windows != parent_window_handle:
                    self.driver.switch_to.window(windows)
                    sleep(2)
                    self.driver.close()
                    break

            # To get back to home page
            self.driver.switch_to.window(parent_window_handle)
            sleep(2)
            print("Returned to the parent window.")

        except Exception as error:
            print("Error", error)

        finally:
            print("Automation Executed Successfully")
            self.driver.quit()



#Main Execution
if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    selva = MovingBetweenWindows(url)
    selva.windows()
