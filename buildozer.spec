[app]

# 应用名称（手机桌面显示的名字）
package.name = mykivyapp
# 包域名，必须三段式，随便写，不要用中文
package.domain = org.yehao.mykivyapp

# 入口python文件，你的主程序是work.py就写work.py！！！
package.main = work.py

source.dir = .
source.include_exts = py,png,jpg,json,atlas,ttf

# Android SDK版本要求
android.sdk = 24
android.ndk = 25b
android.api = 33

# 开启kivy
requirements = python3,kivy

# 应用方向 portrait竖屏 / landscape横屏
orientation = portrait

# 是否全屏
fullscreen = 0

# 应用图标（没有图标就注释掉这两行，前面加#）
# icon.filename = icon.png
# presplash.filename = splash.png

[buildozer]
log_level = 2
warn_on_root = 1
