import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from pages.BaseClass import BaseClass


class Web_UI_Page(BaseClass):

    def __init__(self,driver):
        self.driver  = driver

    loginToolTipFooter = (By.XPATH, "//div[@class='nav-signin-tooltip-footer']")
    loginToolTip = (By.XPATH, "//div[@id='nav-signin-tooltip']")
    searchBox = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    results_Search_Mobiles = (By.XPATH,"//div[@class='left-pane-results-container']/div/div/div[@role='button']")
    table= (By.CSS_SELECTOR,"#resultTable > tbody> tr")
    staticDropdown= (By.CSS_SELECTOR,"#dropdown-class-example")
    source_Element= (By.XPATH,"//div[@id='draggable']")
    destination_Element=(By.XPATH,"//div[@id='droppable']")
    iframe_By_ID=(By.CSS_SELECTOR,"iframe[id='courses-iframe']")
    element_Fact_Count_In_Frame=(By.XPATH,"//div[@class='fact-counter-two']/div/div")
    input_Alert_Box = (By.CSS_SELECTOR,"#name")
    alert_Element = (By.CSS_SELECTOR,"#alertbtn")
    confirm_Alert_Element = (By.CSS_SELECTOR, "#confirmbtn")
    mouse_Hover_Element=(By.XPATH,"//div[@class='mouse-hover']")
    sub_ele= (By.CSS_SELECTOR,"div[class=mouse-hover]> div >a[href ='#top']")
    blinking_Text=(By.CSS_SELECTOR,"a[class='blinkingText']")
    button_In_parent_Window=(By.CSS_SELECTOR,"button[class='btn-style class1']")
    button_In_parent_Window_Tab = (By.CSS_SELECTOR, "a[class='btn-style class1 class2']")
    dynamic_Dropdown_Input=(By.CSS_SELECTOR,"input[id='autocomplete']")
    list_Results=(By.XPATH,"//ul[@id='ui-id-1']/li//div")
    slider_1=(By.XPATH,"//div[@id='slider-range']/span[1]")
    slider_2=(By.XPATH,"//div[@id='slider-range']/span[2]")
    link_Registration=(By.LINK_TEXT,"REGISTER")
    img_Registration=(By.CSS_SELECTOR,"img[src='images/mast_register.gif']")

    input_First_Name=(By.CSS_SELECTOR,"input[name='firstName']")
    input_Last_Name = (By.CSS_SELECTOR, "input[name='lastName']")
    input_Phone = (By.CSS_SELECTOR, "input[name='phone']")
    input_User_Email=(By.CSS_SELECTOR,"input[name='userName']")

    input_Address = (By.CSS_SELECTOR, "input[name='address1']")
    input_City = (By.CSS_SELECTOR, "input[name='city']")
    input_State = (By.CSS_SELECTOR, "input[name='state']")
    input_Postal_Code = (By.CSS_SELECTOR, "input[name='postalCode']")
    input_Select_Country = (By.CSS_SELECTOR, "select[name='country']")

    input_UserName = (By.CSS_SELECTOR, "input[name='email']")
    input_User_Password = (By.CSS_SELECTOR, "input[name='password']")
    input_User_Confirm_Password = (By.CSS_SELECTOR, "input[name='confirmPassword']")
    input_Submit_Button = (By.CSS_SELECTOR, "input[name='submit']")

    link_SignIN_After_Registration = (By.CSS_SELECTOR, "a[href='login.php']")
    userName_After_Registration = (By.XPATH, "//b[contains(text(), ' Note:')]")




    def handle_Dynamic_DropDown(self,searchFor):
        logger = self.get_Log_Details()
        logger.info('Handling dynamic drop down')
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='nav-signin-tooltip']")))
        except Exception as e:
            self.driver.get_screenshot_as_file('../failed_Testcase_Screenshots/screenshot2.png')
            raise e

        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, "//div[@id='nav-signin-tooltip']")))
        self.driver.find_element(*self.searchBox).send_keys(searchFor)
        time.sleep(4)

        #WebDriverWait(self.driver, 20).until(
        #EC.presence_of_element_located((By.XPATH,"//div[@class='left-pane-results-container']/div/div/div[@role='button']")))
        all_Results = self.driver.find_elements(*self.results_Search_Mobiles)

        for result in all_Results:
            logger.info(result.get_attribute('aria-label'))
            if result.text.__contains__('under 8000'):
                logger.info(result.text + ' option about to selected')
                result.click()
                time.sleep(2)
                break

        searchedOption =self.driver.find_element(*self.searchBox).get_attribute('value')


        try:
            assert searchedOption.lower() == searchFor.lower()
        except Exception as e:
            self.driver.get_screenshot_as_file('../failed_Testcase_Screenshots/screenshot1.png')
            raise e
        logger.info('selected value is: '+self.driver.find_element(*self.searchBox).get_attribute('value'))
        logger.info('selected value is: ' + self.driver.find_element(*self.searchBox).get_attribute('value'))


    def handle_Static_Dropdown(self,optionName):
        logger = self.get_Log_Details()
        logger.info("Handling static drop down")
        dropdown = self.driver.find_element(*self.staticDropdown)
        static_Dropdown = Select(dropdown)
        static_Dropdown.select_by_visible_text(optionName) #Option3
        time.sleep(2)
        selectedDropdownValue= self.driver.find_element(*self.staticDropdown).get_attribute('value')
        logger.info('the selected value is:  '+ selectedDropdownValue)
        logger.info('the option value is:  ' + optionName)
        logger.info('the selected value is:  ' + selectedDropdownValue)
        logger.info('the option value is:  ' + optionName)
        assert selectedDropdownValue.lower() == optionName.lower()

    def drag_And_Drop_Task(self):
        logger = self.get_Log_Details()
        logger.info("drag and drop task")
        source_Ele = self.driver.find_element(*self.source_Element)
        dest_Ele = self.driver.find_element(*self.destination_Element)
        actionsClass = ActionChains(self.driver)
        actionsClass.drag_and_drop(source_Ele,dest_Ele).perform()
        time.sleep(3)
        logger.info('task done')

    def handle_Frame_Elements(self):
        logger = self.get_Log_Details()
        logger.info("Iframe task")
        frame_Element = self.driver.find_element(*self.iframe_By_ID)
        self.driver.switch_to.frame(frame_Element)
        logger.info('switched into frame...')
        fact_Elements_List = self.driver.find_elements(*self.element_Fact_Count_In_Frame)
        logger.info('length of fact element is: '+ str(len(fact_Elements_List)))


    def handle_Alerts_Accept(self,data_To_Input):
        logger = self.get_Log_Details()
        logger.info("Handle alert")
        self.driver.find_element(*self.input_Alert_Box).send_keys(data_To_Input)
        self.driver.find_element(*self.alert_Element).click()
        alert = self.driver.switch_to.alert
        logger.info('switched into alert...')
        logger.info('the alert text is: '+ alert.text)
        alertData= alert.text
        alert.accept()
        return alertData

    def handle_Confirm_Alerts_Dismiss(self,data_To_Input):
        logger = self.get_Log_Details()
        logger.info("Handle alert")
        self.driver.find_element(*self.input_Alert_Box).send_keys(data_To_Input)
        self.driver.find_element(*self.confirm_Alert_Element).click()
        alert = self.driver.switch_to.alert
        logger.info('switched into alert...')
        logger.info('the alert text is: '+ alert.text)
        alertData= alert.text
        alert.dismiss()
        return alertData


    def handle_Move_To_Element_And_Click(self):
        logger = self.get_Log_Details()
        logger.info("Mouse hover actions")
        mouse_Hover_Ele = self.driver.find_element(*self.mouse_Hover_Element)
        action = ActionChains(self.driver)
        action.move_to_element(mouse_Hover_Ele).perform()
        sub_Ele = self.driver.find_element(*self.sub_ele)
        action.click(sub_Ele).perform()
        blinking_Text_Data = self.driver.find_element(*self.blinking_Text).text
        #assert blinking_Text_Data.is_displayed()
        return blinking_Text_Data

    def handle_Windows(self):
        logger = self.get_Log_Details()
        logger.info("Handling windows....")
        logger.info('the parent window title is: '+ self.driver.title)
        self.driver.find_element(*self.button_In_parent_Window).click()
        all_Windows = self.driver.window_handles
        for handle in all_Windows:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                logger.info('child window title is: '+ self.driver.title)
                assert self.driver.find_element(By.XPATH,"//div[@class='header-logo-support pt-30 pb-30']").is_displayed()
                self.driver.close()
                break

        self.driver.switch_to.window(self.driver.window_handles[0])
        parent_Window_title1 = self.driver.title
        return parent_Window_title1

    def handle_Window_Tab(self):
        logger = self.get_Log_Details()
        logger.info("Handling windows....")
        logger.info('the parent window title is: '+ self.driver.title)
        self.driver.find_element(*self.button_In_parent_Window_Tab).click()
        all_Windows = self.driver.window_handles
        for handle in all_Windows:
            if handle != self.driver.current_window_handle:
                self.driver.switch_to.window(handle)
                logger.info('child window title is: '+ self.driver.title)
                assert self.driver.find_element(By.XPATH,"//div[@class='header-logo-support pt-30 pb-30']").is_displayed()
                self.driver.close()
                break

        self.driver.switch_to.window(self.driver.window_handles[0])
        parent_Window_title = self.driver.title
        return parent_Window_title


    def handle_Suggession_Box_Dynamic_DropDown(self, partialInput):
        logger = self.get_Log_Details()
        logger.info("Handling dynamic drop down....")
        self.driver.find_element(*self.dynamic_Dropdown_Input).send_keys(partialInput)
        time.sleep(3)
        all_Results = self.driver.find_elements(*self.list_Results)
        logger.info('the size of list is: '+ str(len(all_Results)))
        for result in all_Results:
            if result.text.lower() == 'india':
                result.click()
                break
        logger.info("the selected value is: "+self.driver.find_element(*self.dynamic_Dropdown_Input).get_attribute('value'))
        return self.driver.find_element(*self.dynamic_Dropdown_Input).get_attribute('value')

    def handle_SliderBar(self):
        logger = self.get_Log_Details()
        logger.info("Handling slider bar")
        slider1=self.driver.find_element(*self.slider_1)
        min_value = self.driver.execute_script("return arguments[0].getBoundingClientRect().left;;", slider1)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider1,100,0).perform()
        logger.info('slider moved...')
        time.sleep(2)
        #min_value = self.driver.execute_script("return arguments[0].getBoundingClientRect().left;;", slider1)
        max_value = self.driver.execute_script("return arguments[0].getBoundingClientRect().left;;", slider1)
        return [min_value,max_value]


    def registration_Using_External_File_Test_Data(self,firstName,lastName,PhoneNumber,emailID,address,city,state,postalcode,country,username,password,confirmPassword):
        logger = self.get_Log_Details()
        logger.info("Handling slider bar")
        self.driver.find_element(*self.link_Registration).click()
        assert self.driver.find_element(*self.img_Registration).is_displayed()
        self.driver.find_element(*self.input_First_Name).send_keys(firstName)
        self.driver.find_element(*self.input_Last_Name).send_keys(lastName)
        self.driver.find_element(*self.input_Phone).send_keys(PhoneNumber)
        self.driver.find_element(*self.input_User_Email).send_keys(emailID)
        self.driver.find_element(*self.input_Address).send_keys(address)
        self.driver.find_element(*self.input_City).send_keys(city)
        self.driver.find_element(*self.input_State).send_keys(state)
        self.driver.find_element(*self.input_Postal_Code).send_keys(postalcode)
        #time.sleep(2)
        county_Name = Select(self.driver.find_element(*self.input_Select_Country))
        county_Name.select_by_visible_text(country)
        #time.sleep(2)
        self.driver.find_element(*self.input_UserName).send_keys(username)
        self.driver.find_element(*self.input_User_Password).send_keys(password)
        self.driver.find_element(*self.input_User_Confirm_Password).send_keys(confirmPassword)
        self.driver.find_element(*self.input_Submit_Button).click()
        #time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='login.php']")))
        userNameDetails = self.driver.find_element(*self.userName_After_Registration).text
        logger.info(userNameDetails)
        return userNameDetails














