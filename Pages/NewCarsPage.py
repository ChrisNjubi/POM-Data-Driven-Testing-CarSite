from Pages.BasePage import BasePage


class NewCarsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def selectKia(self):
        self.click("Kia_XPATH")

    def selectBMW(self):
        self.click("BMW_XPATH")

    def selectTata(self):
        self.click("Tata_XPATH")

    def selectSkoda(self):
        self.click("Skoda_XPATH")
