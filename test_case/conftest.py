# coding=utf-8
import pytest
import time
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from businessView.register_view import RegisterView
from common.home_page import *

driver = None
@pytest.fixture(scope='module')
def start():
    global driver
    driver = appium_desired_caps()
    print(driver)
    yield driver
    driver.close_app()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            image_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots',
                                      '%s_%s.png' % (report.nodeid.replace("::", "_"), time.strftime('%Y-%m-%d-%H-%M-%S')))
            #file_name = report.nodeid.replace("::", "_") + ".png"
            driver.get_screenshot_as_file(image_file)
            screen_img = get_base64(image_file)
            if image_file:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# def pytest_addoption(parser):
#     report_dir = '../reports/%s.log' % time.strftime('%Y-%m-%d-%H-%M-%S')
#     parser.addoption(
#         "--html", action="store", default=report_dir, help="my option: type1 or type2"
#     )
#
# @pytest.fixture
# def get_report(request):
#     return request.config.getoption("--html")
