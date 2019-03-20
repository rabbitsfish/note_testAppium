from common import desired_caps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
class BaseView:

    def __init__(self, driver):
        self.driver = driver

    def find_element_note(self, *loc):
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*loc))

    def find_elements_note(self, *loc):
        return  WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*loc))

    def get_current_activity(self):
        return self.driver.current_activity

    def click_mobile_keycode(self, keycode):
        self.driver.keyevent(keycode)

    def start_activity(self):
        self.driver.start_activity(desired_caps.app_package_data, desired_caps.app_activity_data)

    def wait_activity(self, app_package, app_activity):
        self.driver.wait_activity(app_package, app_activity)

    def click_homepage_note_icon(self):
        self.find_element_note(*(By.XPATH, '//*[@text="记事本" and @index="24"]')).click()