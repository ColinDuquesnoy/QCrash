from qcrash.backends.email import EmailBackend


def get_backend():
    return EmailBackend('colin.duquesnoy@gmail.com', 'TestQCrash')


def test_send_report():
    b = get_backend()
    ret = b.send_report('A title', 'A body')
    assert ret is False  # means report dialog must not be closed
