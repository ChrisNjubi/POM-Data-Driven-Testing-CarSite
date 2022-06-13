import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Utilities import ConfigReader


# Parameterized Fixture


@pytest.fixture(params=["chrome", "edge"], scope="function")
def get_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    request.cls.driver = driver
    driver.get(ConfigReader.readconfig("basic info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    driver.quit()
