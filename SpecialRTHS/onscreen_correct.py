"""Correct selected miss-typed text in the active Windows application."""

from __future__ import annotations

import ctypes
import sys
import time
import tkinter as tk
from ctypes import wintypes

from change_misstyped_ENGSK import fix_slovak


user32 = ctypes.windll.user32
MOD_CONTROL = 0x0002
MOD_ALT = 0x0001
WM_HOTKEY = 0x0312
HOTKEY_ID = 1
VK_CONTROL = 0x11
VK_C = 0x43
VK_V = 0x56
KEYEVENTF_KEYUP = 0x0002


def press_key(key_code: int) -> None:
	user32.keybd_event(key_code, 0, 0, 0)
	user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)


def press_shortcut(key_code: int) -> None:
	user32.keybd_event(VK_CONTROL, 0, 0, 0)
	press_key(key_code)
	user32.keybd_event(VK_CONTROL, 0, KEYEVENTF_KEYUP, 0)


def replace_selected_text(root: tk.Tk) -> None:
	"""Copy, correct, and replace the selection in the previously active window."""
	try:
		clipboard = root.clipboard_get()
	except tk.TclError:
		clipboard = None
	root.clipboard_clear()
	root.update()
	press_shortcut(VK_C)
	time.sleep(0.15)

	try:
		selected_text = root.clipboard_get()
	except tk.TclError:
		if clipboard is not None:
			root.clipboard_append(clipboard)
			root.update()
		return

	corrected_text = fix_slovak(selected_text)
	root.clipboard_clear()
	root.clipboard_append(corrected_text)
	root.update()
	press_shortcut(VK_V)
	time.sleep(0.15)

	if clipboard is not None:
		root.clipboard_clear()
		root.clipboard_append(clipboard)
		root.update()

	print(corrected_text, flush=True)


def run_hotkey_mode() -> None:
	root = tk.Tk()
	root.withdraw()
	if not user32.RegisterHotKey(None, HOTKEY_ID, MOD_CONTROL | MOD_ALT, ord("S")):
		root.destroy()
		raise RuntimeError("Could not register Ctrl+Alt+S. The shortcut may already be in use.")

	message = wintypes.MSG()
	print("Select text and press Ctrl+Alt+S. Press Ctrl+C in this window to stop.", flush=True)
	try:
		while user32.GetMessageW(ctypes.byref(message), None, 0, 0) > 0:
			if message.message == WM_HOTKEY and message.wParam == HOTKEY_ID:
				replace_selected_text(root)
	finally:
		user32.UnregisterHotKey(None, HOTKEY_ID)
		root.destroy()


def main() -> None:
	if sys.argv[1:] == ["--once"]:
		root = tk.Tk()
		root.withdraw()
		try:
			replace_selected_text(root)
		finally:
			root.destroy()
		return

	run_hotkey_mode()


if __name__ == "__main__":
	main()
