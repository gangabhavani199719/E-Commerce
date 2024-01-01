import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() #logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*********** Test_003_AddCustomer ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************ Login successful *************")

        self.logger.info("********* starting Add Customer Test *****************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickonAddnew()

        self.logger.info("*************Providing customer info *************")

        self.email=random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("NSR")
        self.addcust.setLastName("Technologies")
        self.addcust.setGender("Male")
        self.addcust.setDob("01/19/1997")
        self.addcust.setCompanyName("NSR")
        self.addcust.page_scroll()
        self.addcust.setcustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is  for testing")
        self.addcust.clickOnSave()

        self.logger.info("************ Saving customer information *******************")
        self.logger.info("*********** Add customer Validation started ****************")

        self.msg =self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("***************** Add customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screeshots\\" + "test_addcustomer_scr.png")  #screenshot
            self.logger.error("************* Add customer Test failed")
            assert True == False
        self.driver.close()
        self.logger.info("*********** Ending Home Page Title Test *****************")


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
