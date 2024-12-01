import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.Ui_Assessment_Utility import Utility_Class


def pytest_addoption(parser):
    parser.addoption("--browserName",action='store',default="chrome")

options = Options()
options.add_argument("--headless")

@pytest.fixture(scope='class')
def browser_SetUp(request):
    browser_name = request.config.getoption("browserName")
    if browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=options) #options=options
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.close()
    time.sleep(2)

@pytest.fixture(params=Utility_Class.read_Excel_File('../testdata/reg_Test_Data.xlsx'))
def get_Test_Data_From_Excel(request):
    return request.param
