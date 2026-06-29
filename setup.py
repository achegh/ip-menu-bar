from setuptools import setup

APP = ["ip_menubar.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": False,
    "plist": {
        "LSUIElement": True,           # hides the Dock icon — menu bar only
        "CFBundleName": "IP Menu Bar",
        "CFBundleDisplayName": "IP Menu Bar",
        "CFBundleIdentifier": "com.user.ipmenubar",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
        "NSAppTransportSecurity": {
            "NSAllowsArbitraryLoads": True,
        },
    },
    "packages": ["rumps"],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
