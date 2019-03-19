from baseView.base_veiw import BaseView
from selenium.webdriver.common.by import By
from common.desired_caps import *
from common.home_page import *
class LoginView(HomePage):
    username_data = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    psw_data = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    login_button_data = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    login_alert_data = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    my_button_data = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    check_username_data = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    setting_data = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logout_data = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    logout_commit_data = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self, username, psw):
        logging.info('start login')
        self.find_element_kyb(*self.username_data).clear()
        logging.info('username: %s' % username)
        self.find_element_kyb(*self.username_data).send_keys(username)
        logging.info('password: %s' % psw)
        self.find_element_kyb(*self.psw_data).send_keys(psw)
        logging.info('click login button')
        self.find_element_kyb(*self.login_button_data).click()
        logging.info('login success')

    def check_login_alert(self):
        logging.info('check login alert')
        try:
            el = self.find_element_kyb(*self.login_alert_data)
        except TimeoutException:
            logging.info('no login alert')
        else:
            logging.info('click login alert')
            el.click()

    def check_login_status(self):
        logging.info('check login status')
        self.check_login_alert()
        try:
            self.find_element_kyb(*self.my_button_data).click()
            self.find_element_kyb(*self.check_username_data)
        except TimeoutException:
            logging.info('login fail')
            return False
        else:
            logging.info('login success')
            return True

    def logout_action(self):
        try:
            logging.info('click my button')
            self.find_element_kyb(*self.my_button_data).click()
            logging.info('click setting button')
            self.find_element_kyb(*self.setting_data).click()
            logging.info('click logout button ')
            self.find_element_kyb(*self.logout_data).click()
            logging.info('click logout commit button')
            self.find_element_kyb(*self.logout_commit_data).click()
        except TimeoutException:
            logging.info('TimeoutException')

if __name__ == '__main__':
    driver = appium_desired_caps()
    login_view = LoginView(driver)
    home_page = HomePage(driver)
    home_page.check_cancelBtn()
    home_page.check_skipBtn()
    login_view.login_action('自学网2018', 'zxw2028')
    login_view.check_login_status()
