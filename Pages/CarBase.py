from selenium.webdriver.common.by import By

from Utilities import ConfigReader


class CarBase:
    def __init__(self,driver):
        self.driver=driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, ConfigReader.readconfig("locators", "carTitle_XPATH")).text

    def getCarNameAndPrice(self):
        carName = self.driver.find_elements(By.XPATH, ConfigReader.readconfig("locators", "carName_XPATH"))
        carPrice = self.driver.find_elements(By.XPATH, ConfigReader.readconfig("locators", "carPrice_XPATH"))


#         We need to get the length of car prices: we need to run a loop on car prices to get the correct name correctly
        for i in range(1, len(carPrice)):
            print((carName[i].text+"-----Prices are----------"+carPrice[i].text).encode('utf8'))


