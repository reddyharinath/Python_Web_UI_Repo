
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from testcases.PET_CRUD_Operations import Pet_CRUD_Operations


def pytest_addoption(parser):
    parser.addoption("--browserName",action='store',default="chrome")

options = Options()
options.add_argument("--headless")

@pytest.fixture(scope='class')
def browser_SetUp(request):
    browser_name = request.config.getoption("browserName")
    print('browser name is: ', browser_name)
    if browser_name.lower() == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name.lower() == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome() #options=options
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def createPet(request):
    createPetResponseInJson = Pet_CRUD_Operations.createPet()
    request.cls.CreatePetResponse = createPetResponseInJson


