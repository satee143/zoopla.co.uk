from selenium import webdriver
import pytest
import time

def pytest_addoption(parser):
     parser.addoption('--browser',action='store',default='chrome')

@pytest.fixture()
def Setup(request):
     browser=request.config.getoption('--browser')
     if browser=='chrome':
          driver=webdriver.Chrome(executable_path='C:/Users/Dusa/PycharmProjects/zoopla.co.uk/Drivers/chromedriver.exe')
     elif browser=='firefox':
          driver=webdriver.Firefox(executable_path='C:/Users/Dusa/PycharmProjects/zoopla.co.uk/Drivers/geckodriver.exe')
     request.cls.driver=driver
     driver.maximize_window()
     driver.implicitly_wait(2)
     yield
     driver.close()
     driver.quit()
	