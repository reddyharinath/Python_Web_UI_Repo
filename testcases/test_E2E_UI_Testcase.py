import pytest
from faker import Faker
from robot.utils.asserts import assert_true
from pages.BaseClass import BaseClass
from pages.Webpage import Web_UI_Page
from utilities.Ui_Assessment_Utility import Utility_Class


configuration_Details = Utility_Class.read_Config_Details()
baseClass= BaseClass()
logger=baseClass.get_Log_Details()
dataFromJsonFile = Utility_Class.read_Json_File()
excel_Test_Data_Dict = Utility_Class.read_Excel_File('../testdata/reg_Test_Data.xlsx')
csv_Test_Data_Dict = Utility_Class.read_CSV_File('../testdata/testData_CSV.csv')
fakerData = Faker()


@pytest.mark.usefixtures("browser_SetUp")
class Test_Class_UI:


    def testcase_Handle_Dynamic_DropDown(self,browser_SetUp):

        logger.info('URL data from properties file is : '+configuration_Details['UI_Assessment']['handle_Dynamic_Dropdown_URL'])
        logger.info('Data from Json file is : '+ dataFromJsonFile['search_For'])
        self.driver.get(configuration_Details['UI_Assessment']['handle_Dynamic_Dropdown_URL'])
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)
        page.handle_Dynamic_DropDown(dataFromJsonFile['search_For'])
        logger.info('Searching got completed.')
        logger.info('driver closed...')


    def testcase_handle_Static_Dropdown(self,browser_SetUp):

        logger.info('Captured URL from properties file is : ' + configuration_Details['UI_Assessment']['handle_Static_DropDown'])
        logger.info('test data from Json file is : ' + dataFromJsonFile['staticDropDownValue'])
        self.driver.get(configuration_Details['UI_Assessment']['handle_Static_DropDown'])
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)
        page.handle_Static_Dropdown(dataFromJsonFile['staticDropDownValue'])
        logger.info('Searching got completed.')
        logger.info('driver closed...')


    def testcase_Drag_And_Drop_Task(self,browser_SetUp):

        APP_URL = configuration_Details['UI_Assessment']['drag_And_Drop_Task_URL']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        self.driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)
        page.drag_And_Drop_Task()
        logger.info('driver closed...')


    def testcase_Handle_Frame(self,browser_SetUp):

        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        self.driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)
        page.handle_Frame_Elements()
        logger.info('driver closed...')


    def testcase_Capture_AlertText_And_Accept(self,browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        alert_Data = page.handle_Alerts_Accept(dataFromJsonFile['Alert_Data'])
        assert dataFromJsonFile['Alert_Data'].lower() in alert_Data.lower()
        logger.info('driver closed...')


    def testcase_Capture_AlertText_And_Dismiss(self,browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        alert_Data=page.handle_Confirm_Alerts_Dismiss(dataFromJsonFile['Alert_Data'])
        assert dataFromJsonFile['Alert_Data'].lower() in alert_Data.lower()
        logger.info('driver closed...')


    def testcase_Move_To_Element_And_Click(self,browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        data = page.handle_Move_To_Element_And_Click()
        assert_true(bool(data))
        logger.info('driver closed...')


    def testcase_Handle_Windows(self, browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        parent_Window_Title_data = page.handle_Windows()
        assert_true(parent_Window_Title_data.lower() == 'practice page')
        logger.info('driver closed...')


    def testcase_Handle_Windows_Tabs(self, browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        parent_Window_Title_data = page.handle_Window_Tab()
        assert_true(parent_Window_Title_data.lower() == 'practice page')
        logger.info('driver closed...')


    def testcase_Handle_Slier_Bar(self, browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['drag_And_Drop_Task_URL']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        data = page.handle_SliderBar()
        logger.info(data)
        assert data[0] < data[1]
        logger.info('driver closed...')

    @pytest.mark.smoke

    def testcase_Handle_Dynamic_Suggession_Box(self, browser_SetUp):
        driver = self.driver
        APP_URL = configuration_Details['UI_Assessment']['handle_Static_DropDown']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(driver)
        data = page.handle_Suggession_Box_Dynamic_DropDown(dataFromJsonFile['Input_Dynamic_Dropdown'])
        assert dataFromJsonFile['Input_Dynamic_Dropdown'].lower() in data.lower()
        logger.info('driver closed...')


    def testcase_Registration_With_Excel_Data(self,browser_SetUp):
        APP_URL = configuration_Details['UI_Assessment']['registration_Task_URL']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        self.driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)

        firstName = excel_Test_Data_Dict['firstName']
        lastName = excel_Test_Data_Dict['lastName']
        phone = excel_Test_Data_Dict['phone']
        email = excel_Test_Data_Dict['email']

        address = excel_Test_Data_Dict['address']
        city   = excel_Test_Data_Dict['city']
        state = excel_Test_Data_Dict['state']
        postalCode = excel_Test_Data_Dict['postalcode']
        country = excel_Test_Data_Dict['country']

        username = excel_Test_Data_Dict['username']
        password = excel_Test_Data_Dict['password']
        confirm_Password = excel_Test_Data_Dict['cPassword']

        userName_Details = page.registration_Using_External_File_Test_Data(firstName,lastName,phone,email,address,city,state,postalCode,country,username,password,confirm_Password)
        assert username.lower() in userName_Details.lower()


    def test_Handle_CSV_File(self):
        APP_URL = configuration_Details['UI_Assessment']['registration_Task_URL']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        self.driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)

        firstName = csv_Test_Data_Dict['firstName']
        lastName = csv_Test_Data_Dict['last_Name']
        phone = csv_Test_Data_Dict['phone']
        email = csv_Test_Data_Dict['email']

        address = csv_Test_Data_Dict['address']
        city = csv_Test_Data_Dict['city']
        state = csv_Test_Data_Dict['state']
        postalCode = csv_Test_Data_Dict['postalcode']
        country = csv_Test_Data_Dict['country']

        username = csv_Test_Data_Dict['username']
        password = csv_Test_Data_Dict['password']
        confirm_Password = csv_Test_Data_Dict['confirm_Password']

        userName_Details = page.registration_Using_External_File_Test_Data(firstName,lastName,phone,email,address,city,state,postalCode,country,username,password,confirm_Password)
        assert username.lower() in userName_Details.lower()


    def test_Read_FakerData(self):
        APP_URL = configuration_Details['UI_Assessment']['registration_Task_URL']
        logger.info('Captured URL from properties file is : ' + APP_URL)
        self.driver.get(APP_URL)
        logger.info('Page loaded')
        page = Web_UI_Page(self.driver)

        firstName = fakerData.first_name()
        lastName = fakerData.last_name()
        phone = fakerData.phone_number()
        email = fakerData.email()

        address = csv_Test_Data_Dict['address']
        city = csv_Test_Data_Dict['city']
        state = csv_Test_Data_Dict['state']
        postalCode = csv_Test_Data_Dict['postalcode']
        country = csv_Test_Data_Dict['country']

        username = fakerData.user_name()
        password = fakerData.password()
        confirm_Password = password

        userName_Details = page.registration_Using_External_File_Test_Data(firstName, lastName, phone, email, address,
                                                                           city, state, postalCode, country, username,
                                                                           password, confirm_Password)
        assert username.lower() in userName_Details.lower()



