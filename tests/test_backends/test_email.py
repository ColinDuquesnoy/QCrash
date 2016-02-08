from qcrash.backends.email import EmailBackend


EMAIL = 'your.email@provider.com'


def get_backend():
    return EmailBackend(EMAIL, 'TestQCrash')


def test_send_report():
    b = get_backend()
    ret = b.send_report('A title', 'A body')
    assert ret is False  # means report dialog must not be closed
