#!/usr/bin/env python

PROJECT = 'virtualenvwrapper-win'
AUTHOR = 'davidmarble'
EMAIL = ''
DESCRIPTION = ('Port of Doug Hellmann\'s virtualenvwrapper '
        'to Windows batch scripts')
VERSION = '1.0.0'
PROJECT_URL = 'https://github.com/%s/%s/' % (AUTHOR, PROJECT)


from setuptools import setup

import os
import sys


long_description = ''
try:
    long_description = open('README.txt', 'rt').read()
except IOError:
    pass


setup(
    name = PROJECT,
    version = VERSION,

    description = DESCRIPTION,
    long_description = long_description,

    author = AUTHOR,
    author_email = EMAIL,
    url = PROJECT_URL,

    platforms = ['WIN32', 'WIN64', ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Environment :: Console', ],

    scripts = [
        'add2virtualenv.bat',
        'cd-.bat',
        'cdsitepackages.bat',
        'cdvirtualenv.bat',
        'folder_delete.bat',
        'lssitepackages.bat',
        'lsvirtualenv.bat',
        'mkvirtualenv.bat',
        'rmvirtualenv.bat',
        'workon.bat', ],

    install_requires=['virtualenv', ],

    zip_safe=False, )
