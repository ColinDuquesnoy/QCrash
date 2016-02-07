import logging
import sys

from PyQt5 import QtCore, QtWidgets

logging.basicConfig()

import qcrash.api as qcrash



GITHUB_OWNER = 'ColinDuquesnoy'
GITHUB_REPO = 'TestBugReport'
EMAIL = 'colin.duquesnoy@gmail.com'


def get_system_info():
    return 'OS: %s\nPython: %r' % (sys.platform, sys.version_info)


def get_application_log():
    return "Blabla"


app = QtWidgets.QApplication(sys.argv)
my_settings = QtCore.QSettings()


# use own qsettings to remember username,... (password stored via keyring)
qcrash.set_qsettings(my_settings)


# configure backends
qcrash.install_backend(qcrash.backends.GithubBackend(
    GITHUB_OWNER, GITHUB_REPO))
qcrash.install_backend(qcrash.backends.EmailBackend(EMAIL, 'TestApp'))


# setup our own function to collect system info and application log
qcrash.get_application_log = get_application_log
qcrash.get_system_information = get_system_info


# show report dialog manually
qcrash.show_report_dialog()


# create a window
win = QtWidgets.QMainWindow()
label = QtWidgets.QLabel()
label.setText('Wait a few seconds for an unhandled exception to occur...')
label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
win.setCentralWidget(label)
win.showMaximized()


# install our own except hook.
def except_hook(exc, tb):
    res = QtWidgets.QMessageBox.question(
        win, "Unhandled exception", "An unhandled exception has occured. Do "
        "you want to report")
    if res == QtWidgets.QMessageBox.Yes:
        qcrash.show_report_dialog(
            window_title='Report unhandled exception',
            issue_title=str(exc), traceback=tb)

qcrash.install_except_hook(except_hook=except_hook)


# raise an unhandled exception in a few seconds
def raise_unhandled_exception():
    raise Exception('this is an unhandled exception')
QtCore.QTimer.singleShot(2000, raise_unhandled_exception)

# run qt app
app.exec_()
