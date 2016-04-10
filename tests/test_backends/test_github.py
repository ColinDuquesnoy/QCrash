from qcrash import api, qt

USERNAME = 'QCrash-Tester'
PASSWORD = 'TestQCrash1234'
GH_OWNER = 'ColinDuquesnoy'
GH_REPO = 'QCrash-Test'


def get_backend():
    b = api.backends.GithubBackend(GH_OWNER, GH_REPO)
    b._show_msgbox = False
    return b


def get_backend_bad_repo():
    b = api.backends.GithubBackend(GH_OWNER, GH_REPO + '1234')
    b._show_msgbox = False
    return b


def get_wrong_user_credentials():
    """
    Monkeypatch GithubBackend.get_user_credentials to force the case where
    invalid credentias were provided
    """
    return 'invalid', 'invalid', False, False


def get_empty_user_credentials():
    """
    Monkeypatch GithubBackend.get_user_credentials to force the case where
    invalid credentias were provided
    """
    return '', '', False, False


def get_fake_user_credentials():
    """
    Monkeypatch GithubBackend.get_user_credentials to force the case where
    invalid credentias were provided
    """
    return USERNAME, PASSWORD, False, False


def test_invalid_credentials():
    b = get_backend()
    b.get_user_credentials = get_wrong_user_credentials
    ret = b.send_report('Wrong credentials', 'Wrong credentials')
    assert ret is False


def test_empty_credentials():
    b = get_backend()
    b.get_user_credentials = get_empty_user_credentials
    ret = b.send_report('Empty credentials', 'Wrong credentials')
    assert ret is False


def test_fake_credentials():
    b = get_backend()
    b.get_user_credentials = get_fake_user_credentials
    ret = b.send_report('Test suite', 'Test fake credentials')
    assert ret is True


def test_fake_credentials_bad_repo():
    b = get_backend_bad_repo()
    b.get_user_credentials = get_fake_user_credentials
    ret = b.send_report('Test suite', 'Test fake credentials')
    assert ret is False


def test_get_credentials_from_qsettings():
    qsettings = qt.QtCore.QSettings('TestCrashCredentials')
    qsettings.clear()
    api.set_qsettings(qsettings)
    b = get_backend()
    username, remember, remember_password = b._get_credentials_from_qsettings()
    assert username == ''
    assert remember is False
    assert remember_password is False

    qsettings.setValue('github/username', 'toto')
    qsettings.setValue('github/remember_credentials', '1')
    qsettings.setValue('github/remember_password', '1')

    username, remember, remember_password = b._get_credentials_from_qsettings()
    assert username == 'toto'
    assert remember is True
    assert remember_password is True


def test_store_user_credentials():
    qsettings = qt.QtCore.QSettings('TestCrashCredentials')
    qsettings.clear()
    api.set_qsettings(qsettings)
    b = get_backend()
    b._store_credentials('user', 'toto', True, False)
    username, remember, remember_pasword = b._get_credentials_from_qsettings()
    assert username == 'user'
    assert remember is True
    assert remember_pasword is False
