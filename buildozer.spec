[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.yehao.mykivyapp
version = 0.1

package.main = work.py
source.dir = .
source.include_exts = py,png,jpg,json,atlas,ttf

android.api = 33
android.ndk = 25b

requirements = python3,kivy
orientation = portrait
fullscreen = 0

# 没有图标就保留注释
# icon.filename = icon.png
# presplash.filename = splash.png

[buildozer]
log_level = 2
warn_on_root = 1
