import ctypes, sys


FRAME_WIDTH = 1280
FRAME_HEIGHT = 720


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

