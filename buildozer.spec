[app]
# Application name and package details
title = CryptoMasterX1
package.name = cryptomasterx1
package.domain = org.cmx1

# Source directory and file types to include
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,html,ttf,otf
source.exclude_dirs = .git,.github,.buildozer,bin,build,app,venv,__pycache__

# App version
version = 1.0.0

# Python requirements (add only what your app imports)
requirements = python3,kivy,requests,urllib3,websocket-client
# Android specific settings
android.ndk = 25b
android.minapi = 21
android.ndk_api = 21
android.api = 33
android.python_version = 3.11
android.accept_sdk_license = True
android.archs = arm64-v8a
android.use_androidx = True
android.allow_backup = True

# Permissions (keep only what you need)
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK

# Display settings
orientation = portrait
fullscreen = 0

# iOS / macOS settings (optional, but included for completeness)
osx.python_version = 3
osx.kivy_version = 2.2.1

[buildozer]

# Build and output directories
log_level = 2
build_dir = ./.buildozer
bin_dir = ./bin

# Host Python version (should match your system's Python 3.11)
p4a.source_dir = /data/data/com.termux/files/home/p4a_fixed
