#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# build.sh — Build "IP Menu Bar.app" from ip_menubar.py
#
# Run once from this folder:
#   chmod +x build.sh && ./build.sh
#
# After a successful build, drag dist/"IP Menu Bar.app" to /Applications
# and double-click it. It will appear in the menu bar immediately.
# ─────────────────────────────────────────────────────────────────────────────

set -e

echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 Installing Python dependencies..."
pip install --quiet --upgrade pip rumps py2app

echo "🔨 Building app bundle..."
python setup.py py2app --quiet 2>/dev/null || python setup.py py2app

echo ""
echo "✅  Build complete!"
echo ""
echo "👉 Next steps:"
echo "   1. Drag  dist/IP Menu Bar.app  to your Applications folder"
echo "   2. Double-click it — the ⌀ icon appears in the menu bar"
echo "   3. (Optional) Add it to Login Items so it starts automatically:"
echo "      System Settings → General → Login Items → +"
echo ""
