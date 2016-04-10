from qcrash.formatters.email import EmailFormatter


def test_format_title():
    title = 'test'
    appname = 'TestQCrash'
    expected = '[%s] %s' % (appname, title)
    assert EmailFormatter(app_name=appname).format_title(title) == expected
    assert EmailFormatter().format_title(title) == title


def test_format_body():
    appname = 'TestQCrash'
    description = 'A description'
    traceback = 'A traceback'
    sys_info = '''OS: Linux
Python: 3.4.1
Qt: 5.5.1'''
    expected = '''Description
----------------------------------------

%s


Traceback
----------------------------------------

%s


System information
----------------------------------------

%s


''' % (description, traceback, sys_info)

    assert EmailFormatter(app_name=appname).format_body(
        description, sys_info, traceback) == expected


def test_format_body_no_log_no_sys_info():
    appname = 'TestQCrash'
    description = 'A description'
    traceback = 'A traceback'
    sys_info = None
    expected = '''Description
----------------------------------------

%s


Traceback
----------------------------------------

%s


''' % (description, traceback)

    assert EmailFormatter(app_name=appname).format_body(
        description, sys_info, traceback) == expected
