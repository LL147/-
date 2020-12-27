import random
from appium.webdriver.common.mobileby import MobileBy
from po.base_page import BasePage


def raddomPhone():
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189"]
    return (random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
name = "lisi"
raddomPhone()

class AddressList(BasePage):
    def add_information(self):
        #录入信息
        self.find_send(MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", "%s" % name)
        self.find_click(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
        self.wait_find(MobileBy.XPATH, "//*[@text='女']")
        self.find_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_send(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", "%s" % raddomPhone())
        self.find_click(MobileBy.XPATH, "//*[@text='保存']")

        return True