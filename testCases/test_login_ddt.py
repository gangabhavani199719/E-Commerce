import time
import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtilis

class  Test_002_DDT_Login:

    baseURL=ReadConfig.getApplicationURL()
    path="C:\\python-selenium\\E-commerce\\TestData\\loginDataset.xlsx"


    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********************Test_002_DDT_Login********************")
        self.logger.info("*******************Verifying Login DDT Test************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=excelUtilis.getRowCount(self.path,'Sheet1')
        print("Number of rows i a Excel:",self.rows)

        lst_status =[]  # empty list variable

        for r in range(2,self.rows+1):
            self.user=excelUtilis.readData(self.path,'Sheet1',r,1)
            self.password = excelUtilis.readData(self.path,'Sheet1', r,2)
            self.exp=excelUtilis.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****passed******")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Failed")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****failed********")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***********passed*******")
                    lst_status.append("Pass")
        if "Fail"  not in lst_status:
            self.logger.info("************ Login DDT test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Login DDT has failed ***********")
            self.driver.close()
            assert False

        self.logger.info("********* End of login DDT test ************")
        self.logger.info("*********** Completed TC_loginDDT_002 **************");