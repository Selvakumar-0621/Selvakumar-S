
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#Import Exception
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


from selenium.webdriver.common.action_chains import ActionChains

class Data:
    url = "https://jqueryui.com/droppable/"

class Locators:
    source = "draggable"
    target = "droppable"

class DragAndDrop(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def drag_drop(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(2)

# ID "draggable" is inside the iframe which is considered as a separate window in selenium. So switching to iframe before locating the source element

            self.driver.switch_to.frame(self.driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame"))

            source = self.driver.find_element(by=By.ID, value=self.source)
            target = self.driver.find_element(by=By.ID, value=self.target)

            self.action.drag_and_drop(source, target).perform()
        except(NoSuchElementException, ElementNotVisibleException) as error:
            print(error)

if __name__ == "__main__":
    selva = DragAndDrop()
    selva.drag_drop()




