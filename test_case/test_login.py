import pytest
from businessView.login_veiw import LoginView
@pytest.mark.parametrize('username,psw', [
    ("自学网2018","zxw2018"),("zxw4321","zxw1234")
])
def test_login(start, username, psw):
    print('test_login')
    login_view = LoginView(start)
    login_view.login_action(username, psw)
    assert login_view.check_login_status()