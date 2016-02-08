from qcrash.formatters.base import BaseFormatter


def test_format_title():
    title = 'test'
    assert BaseFormatter().format_title(title) == title
