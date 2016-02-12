from qcrash.backends.base import BaseBackend
from qcrash.formatters.email import EmailFormatter

import pytest


def test_qsettings():
    b = BaseBackend(None, '', '', None)
    assert b.qsettings() is not None


def test_set_formatter():
    b = BaseBackend(None, '', '', None)
    assert b.formatter is None
    b.set_formatter(EmailFormatter("test"))
    assert isinstance(b.formatter, EmailFormatter)


def test_send_report():
    b = BaseBackend(None, '', '', None)
    with pytest.raises(NotImplementedError):
        b.send_report('', '')
