from baseView.base_veiw import BaseView
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from common.desired_caps import *
class CommonOperations(BaseView):
    authority_alert_continue_data = (By.ID, 'amigo:id/amigo_button1')
    authority_alert_cancel_data = (By.ID, 'amigo:id/amigo_button2')
    home_page_title_data = (By.ID, 'com.gionee.note:id/note_mian_actionbar_title')

    def click_authority_alert_continue(self):
        try:
            elm = self.find_element_note(*self.authority_alert_continue_data)
        except TimeoutException:
            logging.info('authority alert is not exist')
        else:
            logging.info('authority alert is exist,now click the continue button ')
            elm.click()
            return self.is_note_homepage()


    def click_authority_alert_cancel(self):
        try:
            elm = self.find_element_note(*self.authority_alert_cancel_data)
        except TimeoutException:
            logging.info('authority alert is not exist')
        else:
            logging.info('authority alert is exist,now click the cancel button . The current activity is %s' % self.get_current_activity())
            elm.click()
            logging.info('already clicked the cancel button')
            # com.android.launcher2.Launcher
            return self.get_current_activity()

    def is_note_homepage(self):
        try:
            self.find_element_note(*self.home_page_title_data)
        except TimeoutException:
            logging.info('click the continue button,but there is not at homepage')
            return False
        else:
            logging.info('click the continue button successful')
            return True

if __name__ == '__main__':
    common_operations = CommonOperations(appium_desired_caps())
    common_operations.click_authority_alert_cancel()


