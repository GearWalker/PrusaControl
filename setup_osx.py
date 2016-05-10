# -*- coding: utf-8 -*-
"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
APP_NAME = 'PrusaControl'
DATA_FILES = [('', ['translation', 'data'])]
OPTIONS = {'argv_emulation': True,
	    'plist':{
		'CFBundleName': APP_NAME,
		'CFBundleDisplayName': APP_NAME,
		'CFBundleGetInfoString': '3D printing tool',
		'CFBundleIdentifier': 'com.prusa3d.osx.prusacontroll',
		'CFBundleVersion': '0.1.0',
		'CFBundleShortVersion': '0.1.0',
		'NSHumanReadebleCopyright': u"Copyleft (c) 2016, Tibor Vavra"
	}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
