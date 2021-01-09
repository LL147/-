from appium import webdriver
from test_xueqiu.po.base_page import BasePage
from test_xueqiu.po.main import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.xueqiu.android",
                "appActivity": "com.xueqiu.android.main.view.MainActivity",
                "noReset": "true",
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver.launch_app()
            self.driver.implicitly_wait(5)


    def goto_main(self):

        return MainPage(self.driver)

