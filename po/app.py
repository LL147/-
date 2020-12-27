from appium import webdriver
from po.base_page import BasePage
from po.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.tencent.wework",
                "appActivity": "com.tencent.wework.launch.WwMainActivity",
                "noReset": "true",
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(5)

        else:
            self.driver.launch_app()
            self.driver.implicitly_wait(5)

   def goto_main(self):
        return MainPage(self.driver)

