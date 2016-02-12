from qcrash._dialogs.report import DlgReport

import pytest


@pytest.mark.parametrize('include_log', [True, False])
def test_include_log_param(include_log):
    dlg = DlgReport([], include_log=include_log)
    assert dlg.ui.cb_include_application_log.isChecked() == include_log


@pytest.mark.parametrize('include_sys_info', [True, False])
def test_include_sys_info_param(include_sys_info):
    dlg = DlgReport([], include_sys_info=include_sys_info)
    assert dlg.ui.cb_include_sys_info.isChecked() == include_sys_info
