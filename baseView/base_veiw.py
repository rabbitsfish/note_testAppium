from common.desired_caps import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
class BaseView:
    def __init__(self, driver):
        self.driver = driver

    def find_element_kyb(self, *loc):
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))

    def find_elements_kyb(self, *loc):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))
        return self.driver.find_elements(*loc)