from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest

class  Test_001_Login:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()
    #logger=LogGen.custom_logger()



    @pytest.mark.regression
    def test_homePage_Title(self,setup):
        self.logger.info("*******************Test_001_Login***********************************")
        self.logger.info("*******************verifying home page title************************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*******************home page title test is passed************************")
        else:
            self.driver.save_screenshot(".\\screehshots\\"+"test_homePage_Title.png")
            self.driver.close()
            self.logger.error("*******************home page title test is failed************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("*******************Verifying Login Test************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*******************Login Test passed************************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screehshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("*******************login test failed************************")
            assert False
