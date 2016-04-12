from qcrash._dialogs.review import DlgReview


def test_review(qtbot):
    dlg = DlgReview('some content', 'log content', None, None)
    assert dlg.ui.edit_main.toPlainText() == 'some content'
    assert dlg.ui.edit_log.toPlainText() == 'log content'
    qtbot.keyPress(dlg.ui.edit_main, 'A')
    assert dlg.ui.edit_main.toPlainText() == 'Asome content'
    qtbot.keyPress(dlg.ui.edit_log, 'A')
    assert dlg.ui.edit_log.toPlainText() == 'Alog content'
