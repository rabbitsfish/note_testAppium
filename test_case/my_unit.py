import unittest
from common.desired_caps import *
from businessView.register_view import RegisterView
class MyUnit(unittest.TestCase):
    def setUp(self):
        self.driver = appium_desired_caps()
        self.register_view = RegisterView(self.driver)

    def tearDown(self):
        self.driver.close_app()

    def test_register_username_exsit(self):
        self.register_view.register_action('zxw4321', 'zxw888', '3985938593@qq.com')
        self.assertTrue(self.register_view.get_toast('用户名已存在'))

if __name__ == '__main__':
    unittest.main()