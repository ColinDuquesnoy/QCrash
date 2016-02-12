from qcrash.formatters.base import BaseFormatter
import pytest


def test_format_title():
    title = 'test'
    assert BaseFormatter().format_title(title) == title


def test_format_body():
    with pytest.raises(NotImplementedError):
        assert BaseFormatter().format_body('')
