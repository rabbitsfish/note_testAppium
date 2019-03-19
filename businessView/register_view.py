from common.home_page import *
from selenium.webdriver.common.by import By
from common.desired_caps import *
import time
import random
class RegisterView(HomePage):
    register_data = (By.XPATH, '//*[@resource-id="com.tal.kaoyan:id/login_register_text"]')
    register_image_button_data = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    register_image_data = (By.XPATH, '//*[@resource-id="com.tal.kaoyan:id/item_image"]')
    register_image_save_data = (By.ID, 'com.tal.kaoyan:id/save')
    register_username_data = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_psw_data = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email_data = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_commit_data = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    def register_action(self, register_username, register_psw, register_email):
        self.check_cancelBtn()
        self.check_skipBtn()
        try:
            logging.info('start register')
            self.find_element_kyb(*self.register_data).click()
            logging.info('start for image')
            self.find_element_kyb(*self.register_image_button_data).click()
            logging.info('start for select picture')
            self.find_elements_kyb(*self.register_image_data)[2].click()
            logging.info('start for save image')
            self.find_element_kyb(*self.register_image_save_data).click()
            logging.info('register for username')
            self.find_element_kyb(*self.register_username_data).send_keys(register_username)
            logging.info('register for password')
            self.find_element_kyb(*self.register_psw_data).send_keys(register_psw)
            self.find_element_kyb(*self.register_psw_data).click()
            logging.info('register for address')
            self.find_element_kyb(*self.register_email_data).send_keys(register_email)
            self.find_element_kyb(*self.register_email_data).click()
            logging.info('click register button')
            time.sleep(3)
            self.find_element_kyb(*self.register_commit_data).click()
        except TimeoutException:
            logging.info('定位失败')

if __name__ == '__main__':
    register_view = RegisterView(appium_desired_caps())
    register_view.register_action('zxw80297', 'zxw900257', 'fwe345056_we@163.com')

# driver.find_element_by_xpath('//*[@resource-id="com.tal.kaoyan:id/login_register_text"]').click()
# print('点按注册')
# driver.implicitly_wait(2)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
# print('点按设置头像')
# # driver.implicitly_wait(5)
# # driver.find_element_by_xpath('//android.widget.ImageView[@index="0"]').click()
# driver.implicitly_wait(2)
# driver.find_elements_by_xpath('//*[@resource-id="com.tal.kaoyan:id/item_image"]')[2].click()
# print('选择头像')
# driver.implicitly_wait(2)
# driver.find_element_by_id('com.tal.kaoyan:id/save').click()
# print('点按保存')
# driver.implicitly_wait(2)
# username = 'FLY' + str(random.randint(1000, 9999))
# psw = '@zxw' + str(random.randint(1000, 9999))
# print('username: ', username)
# print('password:', psw)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(psw)
# address = str(random.randint(10000000, 99999999)) + '@qq.com'
# print('address:', address)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(address)
# driver.implicitly_wait(2)
# driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()