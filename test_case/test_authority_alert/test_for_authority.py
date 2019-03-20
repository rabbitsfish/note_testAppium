import pytest
import os
import time
from common.common_operations import *
def test_click_continue(start):
    common_operations = CommonOperations(start)
    logging.info('test_click_continue')
    if common_operations.get_current_activity() != '.ui.GnPermissionSummaryActivity':
        os.system('adb shell pm clear com.gionee.note')
        common_operations.click_homepage_note_icon()
    assert common_operations.click_authority_alert_continue()

def test_click_continue_reenter(start):
    common_operations = CommonOperations(start)
    logging.info('test_click_continue_reenter')
    if common_operations.get_current_activity() != '.ui.GnPermissionSummaryActivity':
        os.system('adb shell pm clear com.gionee.note')
        common_operations.click_homepage_note_icon()
    common_operations.click_authority_alert_continue()
    assert common_operations.is_note_homepage()

def test_click_cancel(start):
    common_operations = CommonOperations(start)
    logging.info('test_click_cancel')
    if common_operations.get_current_activity() != '.ui.GnPermissionSummaryActivity':
        os.system('adb shell pm clear com.gionee.note')
        common_operations.click_homepage_note_icon()
    assert common_operations.click_authority_alert_cancel() == 'com.android.launcher2.Launcher'

def test_click_cancel_reenter(start):
    common_operations = CommonOperations(start)
    logging.info('test_click_cancel_reenter')
    if common_operations.get_current_activity() != '.ui.GnPermissionSummaryActivity':
        os.system('adb shell pm clear com.gionee.note')
        common_operations.click_homepage_note_icon()
    assert common_operations.get_current_activity() == '.ui.GnPermissionSummaryActivity'

def test_home_at_authority(start):
    common_operations = CommonOperations(start)  #start中封装了desired_cap的相关信息并启动了
    logging.info('test_home_at_authority')
    time.sleep(10)
    if common_operations.get_current_activity() != '.ui.GnPermissionSummaryActivity':  #if判断语句可以忽略不看
        os.system('adb shell pm clear com.gionee.note')
        common_operations.click_homepage_note_icon()
    common_operations.click_mobile_keycode(3)  #点按home键
    time.sleep(2)
    common_operations.click_homepage_note_icon()
    time.sleep(2)
    assert common_operations.get_current_activity() == '.ui.GnPermissionSummaryActivity'


