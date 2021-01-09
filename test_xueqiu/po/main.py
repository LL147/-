from selenium.webdriver.common.by import By
from test_xueqiu.po.base_page import BasePage
from test_xueqiu.po.maekt import Markt


class MainPage(BasePage):
    def main(self):

        self.find_click(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_click(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")


        return Markt(self.driver)
