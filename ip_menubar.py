#!/usr/bin/env python3
"""
IP Menu Bar — shows your global IP address in the macOS menu bar.
Logs every IP change with a timestamp to ~/Library/Logs/IPMenuBar/ip_changes.csv
Auto-refreshes every 5 minutes.
"""

import csv
import json
import os
import subprocess
import threading
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import rumps

LOG_DIR = Path.home() / "Library" / "Logs" / "IPMenuBar"
LOG_FILE = LOG_DIR / "ip_changes.csv"


def init_log():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["timestamp", "ip_address"])


def append_log(ip: str):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOG_FILE, "a", newline="") as f:
        csv.writer(f).writerow([ts, ip])


class IPMenuBarApp(rumps.App):
    def __init__(self):
        super().__init__("⌀ …", quit_button="Quit")
        self.ip = None
        self.menu = [
            rumps.MenuItem("Copy IP", callback=self.copy_ip),
            rumps.MenuItem("Refresh", callback=self.refresh),
            rumps.MenuItem("View IP Log", callback=self.open_log),
            None,  # separator
        ]
        init_log()
        self.fetch_ip()

    # ── IP fetching ────────────────────────────────────────────────────────

    def fetch_ip(self, _=None):
        self.title = "⌀ …"
        t = threading.Thread(target=self._do_fetch, daemon=True)
        t.start()

    def _do_fetch(self):
        try:
            req = urllib.request.urlopen(
                "https://api.ipify.org?format=json", timeout=8
            )
            data = json.loads(req.read().decode())
            new_ip = data["ip"]

            if new_ip != self.ip:        # only log on actual change
                append_log(new_ip)
                if self.ip is not None:  # skip silent first-run log
                    rumps.notification(
                        title="IP address changed",
                        subtitle="",
                        message=f"{self.ip}  →  {new_ip}",
                        sound=False,
                    )
                self.ip = new_ip

            self.title = f"⌀ {self.ip}"
        except Exception:
            self.ip = None
            self.title = "⌀ Error"

    # ── Menu actions ───────────────────────────────────────────────────────

    def copy_ip(self, _):
        if self.ip:
            subprocess.run(["pbcopy"], input=self.ip.encode(), check=True)
            rumps.notification(
                title="IP copied",
                subtitle="",
                message=self.ip,
                sound=False,
            )

    def refresh(self, _):
        self.fetch_ip()

    def open_log(self, _):
        subprocess.run(["open", str(LOG_FILE)])

    # ── Auto-refresh every 5 minutes ───────────────────────────────────────

    @rumps.timer(300)
    def auto_refresh(self, _):
        self.fetch_ip()


if __name__ == "__main__":
    IPMenuBarApp().run()
