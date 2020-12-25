from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import pytest
class Test():
    def setup(self):
        caps = {
          "platformName": "android",
          "deviceName": "127.0.0.1:62001",
          "appPackage": "com.tencent.wework",
          "appActivity": "com.tencent.wework.launch.WwMainActivity",
          "dontStopAppOnReset": "true",
          "skipServerInstallation": "true",
          "skipDeviceInitialization": "true",
          "noReset": "true",
          "settings[waitForIdleTimeout]": 0
}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(5)

    def tesrdown(self):
        self.driver.quit()


    def testcase(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                      'scrollable(true).instance(0)).'
                                                      'scrollIntoView(new UiSelector().'
                                                      'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        WebDriverWait(self.driver, 10).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source



if __name__ == "__main__":
     pytest.main()


