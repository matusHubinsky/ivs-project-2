import ctypes as ct
import tkinter as tk

def dark_title_bar(window, color):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = ct.c_wchar_p(color)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
