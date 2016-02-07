#!/usr/bin/env python3
"""
Setup script for OpenCobolIDE

You will need to install PyQt4 (or PyQt5) and GnuCOBOL on your own.

"""
from setuptools import setup, find_packages
from qcrash import __version__

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    build_ui = None
    cmdclass = {}

# Get long description
with open('README.rst', 'r') as readme:
    long_desc = readme.read()

setup(
    name='qcrash',
    version=__version__,
    keywords=['Github', 'PyQt4', 'PyQt5', 'PySide', 'Issue', 'Report', 'Crash',
              'Tool'],
    url='https://github.com/ColinDuquesnoy/qcrash',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A crash report framework for PyQt/PySide applications',
    long_description=long_desc,
    packages=find_packages(),
    cmdclass=cmdclass,
    install_requires=['keyring'],
    entry_points={
        'pyqt_distutils_hooks': [
            'fix_qt_imports = qcrash._hooks:fix_qt_imports']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Editors :: Integrated Development Environments (IDE)']
)
