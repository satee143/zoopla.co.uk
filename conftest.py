from selenium import webdriver
import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.microsoft import IEDriverManager

from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
     parser.addoption('--browser',action='store',default='chrome')

@pytest.fixture()
def Setup(request):
     browser=request.config.getoption('--browser')
     if browser=='chrome':
          driver=webdriver.Chrome(ChromeDriverManager().install())
     elif browser=='firefox':
          driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
     elif browser== 'edge':
          driver=webdriver.Edge(executable_path=EdgeDriverManager().install())
     elif browser=='ie' or 'internet explorer':
          driver=webdriver.Ie(executable_path=IEDriverManager().install())


     request.cls.driver=driver
     driver.maximize_window()
     driver.implicitly_wait(2)
     yield
     driver.close()
     driver.quit()

	