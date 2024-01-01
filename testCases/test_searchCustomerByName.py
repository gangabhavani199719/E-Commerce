import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.regression
class Test_005_SearchCustomerByName:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen() #logger

    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("*********** Test_005_SearchCustomerByName ***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********** login successfull *********************")

        self.logger.info("*********** starting search by name *****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info(" **************** searching customer by name **************")
        searchCust=SearchCustomer(self.driver)
        searchCust.setFirstName("Victoria")
        searchCust.setLastName("Terces")
        searchCust.clickSearch()
        time.sleep(4)
        self.addcust.page_scroll()
        status=searchCust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("************ Test_005_SearchCustomerByName Finished **********")
        self.driver.close()