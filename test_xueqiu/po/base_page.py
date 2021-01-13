import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_xueqiu.black_wrapper import black_wrapper


class BasePage:
    FIND = "find"
    ACTION = "action"
    FIND_CLICK = "find_click"
    FIND_SEND = "find_send"
    TXT = "text"


    def __init__(self, driver: WebDriver = None):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.main.view.MainActivity",
            "noReset": "true",
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(10)
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]


    def load(self, yaml_xpath):
        with open(yaml_xpath, encoding="utf-8") as a:
            data = yaml.load(a)
        for i in data:
            xpath_data = i.get(self.FIND)
            action = i.get(self.ACTION)

            if action == self.FIND_CLICK:
                self.find_click(By.XPATH, xpath_data)

            elif action == self.FIND_SEND:
                txt = i.get(self.TXT)
                self.find_send(By.XPATH, xpath_data, txt)



    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)


    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        self.find(by,locator).click()

    #滑动查找
    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        els = self.driver.find_elements(by, locator)
        while els == 0:
            self.driver.swipe(0, 600, 0, 400)
            els = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return els[0]

    def find_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_find(self, by, locator):
        def find_nv(driver):
            eles = self.driver.find_elements(by, locator)
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(find_nv)

    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result


    def screenshot(self, pictrue_path):
        self.driver.save_screenshot(pictrue_path)
