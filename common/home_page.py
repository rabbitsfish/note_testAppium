from baseView import base_veiw
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from common.desired_caps import *
import time
import csv
import base64
class HomePage(base_veiw.BaseView):
    cancel_button_data = (By.ID, 'android:id/button2')
    skip_button_data = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        try:
            logging.info('checking cancelBtn')
            cancel_btn = self.find_element_kyb(*self.cancel_button_data)
        except TimeoutException:
            logging.info('no cancel button')
        else:
            logging.info('click cancel button')
            cancel_btn.click()

    def check_skipBtn(self):
        try:
            logging.info('checking skipBtn')
            skip_btn = self.find_element_kyb(*self.skip_button_data)
        except TimeoutException:
            logging.info('no  skip button')
        else:
            logging.info('click skip button')
            skip_btn.click()

    def get_size(self):
        logging.info('get size')
        size = self.driver.get_window_size()
        return size['width'], size['height']

    def swip_left(self):
        logging.info('start swip left')
        x, y = self.get_size()
        self.driver.swipe(x*0.8, y*0.5, x*0.4, y*0.5, 1000)

    # def get_time(self):
    #     self.now = time.strftime('%Y-%m-%d-%H-%M-%S')
    #     return self.now
    #
    # def get_sreenshot(self, module):
    #     logging.info('get %s screenshot' % module)
    #     image_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots', '%s_%s.png' % (module, self.get_time()))
    #     self.driver.get_screenshot_as_file(image_file)

    def get_toast(self, message):
        logging.info('get toast')
        toast = '//*[@text="{}"]'.format(message)
        try:
            self.find_element_kyb(*(By.XPATH, toast))
        except TimeoutException:
            logging.info('not toast')
            return False
        else:
            logging.info('toast is %s' % message)
            return True

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for index, enum in enumerate(reader, 1):
                if index  == line:
                    return enum

def get_base64(file_dir):
    with open(file_dir, 'rb') as file:
        base64_data = base64.b64encode(file.read())
    return base64_data.decode()

if __name__ == '__main__':
    home_page = HomePage(appium_desired_caps())
    # home_page.check_cancelBtn()
    # home_page.find_element_kyb(*home_page.skip_button_data)
    # home_page.swip_left()
    # home_page.get_sreenshot('start-app')
    # home_page.check_skipBtn()
    print(home_page.get_csv_data('../data/account.csv', 2))
