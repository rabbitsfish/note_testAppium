import unittest
from common.desired_caps import *
from businessView.login_veiw import LoginView
from common.home_page import HomePage
import warnings
import time
class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('start...')
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = appium_desired_caps()
        self.login_view = LoginView(self.driver)
        home_page = HomePage(self.driver)
        home_page.check_cancelBtn()
        home_page.check_skipBtn()

    def tearDown(self):
        logging.info('end...')
        time.sleep(5)
        self.driver.close_app()

    def test_login_1(self):
        logging.info('start login...')
        self.login_view.login_action('自学网2018', 'zxw2018')
        logging.info('login success')

    def test_login_2(self):
        logging.info('start login...')
        self.login_view.login_action('自学网2017', 'zxw2017')
        logging.info('login fail')

    def test_login_3(self):
        logging.info('start login...')
        self.login_view.login_action('666', '222')
        logging.info('login fail')

if __name__ == '__main__':
    unittest.main()
