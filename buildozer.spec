[app]
title = WiFi File Transfer Pro
package.name = wifitransfer
package.domain = com.ikhlak.dev
source.dir = .
source.include_exts = py,kv,html,css,js,png,jpg,gif,ico,txt
version = 1.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0
icon.filename = assets/logo.png
presplash.filename = assets/loading.gif
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
