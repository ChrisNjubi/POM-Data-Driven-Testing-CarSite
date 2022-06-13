# In this base page class, we are going to keep all the common code and all other pages will extend this page
from selenium.webdriver.common.by import By
from Utilities import ConfigReader
from selenium.webdriver import ActionChains


class BasePage:
    # We need to define a driver
    # This driver should be common in all pages
    def __init__(self, driver):
        self.driver = driver

    # Keyword driven approach: What are the events we are going to perform
    # Once we define our keywords we can use them in all our page classes

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readconfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readconfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readconfig("locators", locator)).click()

    def moveTo(self, locator):
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, (ConfigReader.readconfig("locators", locator)))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, (ConfigReader.readconfig("locators", locator)))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, (ConfigReader.readconfig("locators", locator)))

        # I want to hover over NewCars option
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
