# coding=utf-8
import pytest
from businessView.register_view import RegisterView
def test_register_username_exsit(start):
    register_view = RegisterView(start)
    register_view.register_action('zxw4321', 'zxw888', '3985938593@qq.com')
    assert register_view.get_toast('用户名已存在1')
