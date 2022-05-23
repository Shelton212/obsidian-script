import webbrowser
import pyperclip
from pynput.keyboard import Key, Controller

#创建键盘实例
keyboard = Controller()
keyboard.press(Key.ctrl.value)
keyboard.press('c')
keyboard.release(Key.ctrl.value)
keyboard.release('c')

#获取剪切板
str = pyperclip.paste()

#浏览器访问地址
webbrowser.open(str)

