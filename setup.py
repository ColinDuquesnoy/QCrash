#!/usr/bin/env python
"""
Setup script for QCrash
"""
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from qcrash import __version__

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    build_ui = None
    cmdclass = {}


class PyTest(TestCommand, object):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        super(PyTest, self).initialize_options()
        self.pytest_args = []

    def finalize_options(self):
        super(PyTest, self).finalize_options()

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


cmdclass['test'] = PyTest


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
    tests_require=['pytest', 'pytest-qt', 'pytest-cov', 'pytest-flake8'],
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets']
)
