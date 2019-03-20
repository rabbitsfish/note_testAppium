import pytest
import os
import time
from common.common_operations import CommonOperations
def test_click_continue(start):
    os.system('adb shell pm clear com.gionee.note')
    common_operations = CommonOperations(start)
    common_operations.start_activity()
    assert common_operations.click_authority_alert_continue()

def test_click_cancel(start):
    os.system('adb shell pm clear com.gionee.note')
    common_operations = CommonOperations(start)
    common_operations.start_activity()
    assert common_operations.click_authority_alert_cancel() == 'com.android.launcher2.Launcher'

def test_home_at_authority(start):
    os.system('adb shell pm clear com.gionee.note')
    common_operations = CommonOperations(start)
    common_operations.start_activity()
    time.sleep(2)
    common_operations.click_mobile_keycode(3)
    assert common_operations.get_current_activity() == 'com.android.launcher2.Launcher'