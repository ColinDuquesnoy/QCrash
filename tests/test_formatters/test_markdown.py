from qcrash.formatters.markdown import MardownFormatter


def test_format_body():
    description = 'A description'
    traceback = 'A traceback'
    sys_info = '''OS: Linux
Python: 3.4.1
Qt: 5.5.1'''
    log = 'blabla'
    expected = '''### Description

%s

### Traceback

```
%s
```

### System information

- OS: Linux
- Python: 3.4.1
- Qt: 5.5.1

### Application log

```
%s
```

''' % (description, traceback, log)

    assert MardownFormatter().format_body(
        description, sys_info, log, traceback) == expected


def test_format_body_no_log_no_sys_info():
    description = 'A description'
    traceback = 'A traceback'
    sys_info = None
    log = None
    expected = '''### Description

%s

### Traceback

```
%s
```

''' % (description, traceback)

    assert MardownFormatter().format_body(
        description, sys_info, log, traceback) == expected
