import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import DataProvider


class TestCarWale(BaseTest):

    @pytest.mark.skip
    def test_goTONewCars(self):
        home = HomePage(self.driver)
        home.goToNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle",
                             DataProvider.get_data("NewCarsTest"))
    def test_SelectCars(self, carBrand, carTitle):
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Car brand is:" + carBrand)
        if carBrand == "Kia":
            home.goToNewCars().selectKia()
            title = car.getCarTitle()
            print("Car title is: " + title)
            # Assert the cartitle from excel file
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Tata":
            home.goToNewCars().selectTata()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
        elif carBrand == "Skoda":
            home.goToNewCars().selectSkoda()
            title = car.getCarTitle()
            print("Car title is: " + title)
            assert title == carTitle, "Not on the correct page as title is not matching"
    @pytest.mark.parametrize("carBrand,carTitle",
                             DataProvider.get_data("NewCarsTest"))
    def test_printCarNameAndPrice(self, carBrand, carTitle):
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        print("Car brand is:" + carBrand)
        if carBrand == "Kia":
            home.goToNewCars().selectKia()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            # Assert the cartitle from excel file
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "BMW":
            home.goToNewCars().selectBMW()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "Tata":
            home.goToNewCars().selectTata()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()
        elif carBrand == "Skoda":
            home.goToNewCars().selectSkoda()
            title = car.getCarTitle()
            print(("Car title is: " + title).encode('utf8'))
            assert title == carTitle, "Not on the correct page as title is not matching"
            car.getCarNameAndPrice()


"""
How to run allure reports on terminal

1. Go to terminal
2. Navigate to WWWW folder: cd WWWW
3. Type: pytest test_carwale.py --alluredir="../Reports"

After all testcases have being run:
on terminal: allure serve "../Reports"

When to use python package and normal directory:

You can use "Python Package" when you want to put some modules in there which should be importable. 
PyCharm will automatically create an __init__.py for the directory.
 
"""
