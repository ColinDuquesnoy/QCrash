from qcrash import api

USERNAME = 'QCrash-Tester'
PASSWORD = 'TestQCrash1234'


def get_backend():
    b = api.backends.GithubBackend('ColinDuquesnoy', 'QCrash-Test')
    b._show_msgbox = False
    return b


def get_backend_bad_repo():
    b = api.backends.GithubBackend('ColinDuquesnoy', 'QCrash-Test222')
    b._show_msgbox = False
    return b


def get_wrong_user_credentials():
    """
    Monkeypatch GithubBackend.get_user_credentials to force the case where
    invalid credentias were provided
    """
    return 'invalid', 'invalid', False


def get_fake_user_credentials():
    """
    Monkeypatch GithubBackend.get_user_credentials to force the case where
    invalid credentias were provided
    """
    return USERNAME, PASSWORD, False


def test_invalid_credentials():
    b = get_backend()
    b.get_user_credentials = get_wrong_user_credentials
    ret = b.send_report('Wrong credentials', 'Wrong credentials')
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
