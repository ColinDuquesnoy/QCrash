from qcrash._dialogs.gh_login import DlgGitHubLogin


def test_github_login_dialog():
    dlg = DlgGitHubLogin(None, '', False)
    assert not dlg.ui.bt_sign_in.isEnabled()
    dlg.ui.le_username.setText('user')
    dlg.ui.le_password.setText('password')
    assert dlg.ui.bt_sign_in.isEnabled()
