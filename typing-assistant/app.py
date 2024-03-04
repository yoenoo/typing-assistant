import time
import pyperclip
from pynput import keyboard
from pynput.keyboard import Key, Controller
from utils import text_correct

controller = Controller()

def fix_current_line():
  # Cmd + Shift + Left
  controller.press(Key.cmd)
  controller.press(Key.shift)
  controller.press(Key.left)

  controller.release(Key.cmd)
  controller.release(Key.shift)
  controller.release(Key.left)
  fix_selection()

def fix_selection():
  # 1. copy to clipboard  (ctrl+c)
  with controller.pressed(Key.cmd):
    controller.tap('c')
  # 2. get the text from clipboard
  time.sleep(0.1)
  txt = pyperclip.paste()
  print(txt)
  # 3. fix the text
  fixed_txt = text_correct(txt)
  print(fixed_txt)
  # 4. copy back to clipboard
  pyperclip.copy(fixed_txt)
  time.sleep(0.1)
  # 5. insert text back (ctrl+v)
  with controller.pressed(Key.cmd):
    controller.tap('v')

def on_f9():
  fix_current_line()

def on_f10():
  fix_selection()

with keyboard.GlobalHotKeys({'<101>': on_f9, '<109>': on_f10}) as h:
  h.join()
