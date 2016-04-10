from qcrash._dialogs.gh_login import DlgGitHubLogin


def test_github_login_dialog():
    dlg = DlgGitHubLogin(None, '', False, False)
    assert not dlg.ui.bt_sign_in.isEnabled()
    dlg.ui.le_username.setText('user')
    dlg.ui.le_password.setText('password')
    assert dlg.ui.cb_remember.isChecked() is False
    assert dlg.ui.cb_remember_password.isChecked() is False
    assert dlg.ui.cb_remember_password.isEnabled() is False
    assert dlg.ui.bt_sign_in.isEnabled()


def test_focus_username(qtbot):
    dlg = DlgGitHubLogin(None, '', False, False)
    dlg.show()
    assert dlg.ui.le_username.text() == ''
    assert dlg.ui.le_password.text() == ''
    qtbot.waitForWindowShown(dlg)
    dlg.close()


def test_focus_password(qtbot):
    dlg = DlgGitHubLogin(None, 'user', False, False)
    dlg.show()
    qtbot.waitForWindowShown(dlg)
    assert dlg.ui.le_username.text() == 'user'
    assert dlg.ui.le_password.text() == ''
    dlg.close()
