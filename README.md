# IP Menu Bar

A lightweight macOS menu bar app that displays your current global IP address at a glance.

![macOS menu bar showing ⌀ 203.0.113.42](https://img.shields.io/badge/platform-macOS-lightgrey)
![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

## Features

- Shows your external IP address in the menu bar at all times
- Logs every IP change with a UTC timestamp to `~/Library/Logs/IPMenuBar/ip_changes.csv`
- Sends a macOS notification when your IP changes
- Copy IP to clipboard with one click
- Auto-refreshes every 5 minutes
- No Dock icon — lives quietly in the menu bar

## Requirements

- macOS 11+
- Python 3.8+
- [Homebrew](https://brew.sh) (recommended)

## Build & Install

```bash
git clone https://github.com/YOUR_USERNAME/ip-menu-bar.git
cd ip-menu-bar
chmod +x build.sh && ./build.sh
```

Then drag `dist/IP Menu Bar.app` to your `/Applications` folder and double-click it.

**Auto-start on login:** System Settings → General → Login Items → "+" → select `IP Menu Bar.app`

## IP Change Log

Every time your external IP changes, a row is appended to:

```
~/Library/Logs/IPMenuBar/ip_changes.csv
```

Format:
```
timestamp,ip_address
2026-06-28 14:00:00 UTC,203.0.113.42
2026-06-28 19:30:00 UTC,203.0.113.99
```

You can open the log from the menu bar icon → **View IP Log**.

## Project Structure

```
ip-menu-bar/
├── ip_menubar.py   # Main app
├── setup.py        # py2app packaging config
├── build.sh        # One-command build script
└── README.md
```

## License

MIT — see [LICENSE](LICENSE).
