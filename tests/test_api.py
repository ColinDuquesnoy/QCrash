import sys
import pytest

from qcrash import api
from qcrash.qt import QtCore
from qcrash._hooks import QtExceptHook


def test_set_qsettings():
    assert api._qsettings.organizationName() == 'QCrash'
    api.set_qsettings(QtCore.QSettings('TestQCrash'))
    assert api._qsettings.organizationName() == 'TestQCrash'


def test_value_errors():
    api._backends[:] = []
    with pytest.raises(ValueError):
        api.install_except_hook()
    with pytest.raises(ValueError):
        api.show_report_dialog()


def test_install_backend():
    api._backends[:] = []
    assert len(api.get_backends()) == 0
    b1 = api.backends.GithubBackend('ColinDuquesnoy', 'TestQCrash')
    b2 = api.backends.EmailBackend('colin.duquesnoy@gmail.com', 'TestQCrash')
    api.install_backend(b1, b2)
    assert len(api.get_backends()) == 2
    b1 = api.backends.GithubBackend('ColinDuquesnoy', 'TestQCrash')
    b2 = api.backends.EmailBackend('colin.duquesnoy@gmail.com', 'TestQCrash')
    api.install_backend(b1)
    assert len(api.get_backends()) == 3
    api.install_backend(b2)
    assert len(api.get_backends()) == 4


def test_install_except_hook():
    api.install_except_hook()
    assert isinstance(api._except_hook, QtExceptHook)
    assert sys.excepthook == api._except_hook._except_hook


def test_show_report_dialog(qtbot):
    api._backends[:] = []
    assert len(api.get_backends()) == 0
    b1 = api.backends.GithubBackend('ColinDuquesnoy', 'TestQCrash')
    b2 = api.backends.EmailBackend('colin.duquesnoy@gmail.com', 'TestQCrash')
    api.install_backend(b1, b2)
    assert len(api.get_backends()) == 2

    dlg = api.show_report_dialog(modal=True)

    assert len(dlg.buttons) == 2

    # force email backend to return True to close the dialog
    b2.old_send_report = b2.send_report

    qtbot.wait(1000)

    def send_report(*args, **kwargs):
        b2.old_send_report(*args, **kwargs)
        return True

    b2.send_report = send_report
    dlg.buttons[1].clicked.emit(True)

    dlg.reject()


def test_return_empty_string():
    assert api._return_empty_string() == ''
