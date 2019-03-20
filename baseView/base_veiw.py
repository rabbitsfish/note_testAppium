from common.desired_caps import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class BaseView:

    def __init__(self, driver):
        self.driver = driver
        print('driver:', driver)

    def find_element_note(self, *loc):
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))

    def find_elements_note(self, *loc):
        return  WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))

    def get_current_activity(self):
        return self.driver.current_activity

    def click_mobile_keycode(self, keycode):
        self.driver.keyevent(keycode)

    def start_activity(self):
        self.driver.start_activity(app_package_data, app_activity_data)