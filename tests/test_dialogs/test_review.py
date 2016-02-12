from qcrash._dialogs.review import DlgReview


def test_review(qtbot):
    dlg = DlgReview('some content', None)
    assert dlg.ui.plainTextEdit.toPlainText() == 'some content'
    qtbot.keyPress(dlg.ui.plainTextEdit, 'A')
    assert dlg.ui.plainTextEdit.toPlainText() == 'Asome content'
