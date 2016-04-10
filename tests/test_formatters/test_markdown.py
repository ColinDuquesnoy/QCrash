from qcrash.formatters.markdown import MardownFormatter


def test_format_body():
    description = 'A description'
    traceback = 'A traceback'
    sys_info = '''OS: Linux
Python: 3.4.1
Qt: 5.5.1'''
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

''' % (description, traceback)

    assert MardownFormatter().format_body(
        description, sys_info, traceback) == expected


def test_format_body_no_log_no_sys_info():
    description = 'A description'
    traceback = 'A traceback'
    sys_info = None
    expected = '''### Description

%s

### Traceback

```
%s
```

''' % (description, traceback)

    assert MardownFormatter().format_body(
        description, sys_info, traceback) == expected
