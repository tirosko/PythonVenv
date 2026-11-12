"""Convert text typed with the wrong keyboard layout to Slovak."""
# Možno sa na budúci t76de\ trochu schlad9 

from __future__ import annotations

import sys
import tkinter as tk


# Extend this mapping when another key or typed sequence needs correction.
MAP = {
	"c'": "č",
	"s'": "š",
	"z'": "ž",
	"a'": "á",
	"e'": "é",
	"i'": "í",
	"o'": "ó",
	"u'": "ú",
	"y'": "ý",
	"l'": "ľ",
	"t'": "ť",
	"d'": "ď",
	"n'": "ň",
	"r'": "ŕ",
	"a:": "ä",
	# Characters produced when Slovak keyboard keys are interpreted as EN.
	"4": "č",
	"5": "ľ",
	"7": "ý",
	"6": "ž",
	"\\": "ň",
	"9": "í",
	"8": "á",
	"2": "ľ",
	"3": "š",
	"1": "+",
	"0": "é",
	"/": "ú",
	"[": "ú",
}


def fix_slovak(text: str) -> str:
	"""Replace configured miss-typed sequences with Slovak characters."""
	for source, replacement in MAP.items():
		text = text.replace(source, replacement)
	return text


def fix_clipboard() -> str:
	"""Replace the current clipboard text and return the converted text."""
	root = tk.Tk()
	root.withdraw()
	try:
		text = root.clipboard_get()
		converted_text = fix_slovak(text)
		root.clipboard_clear()
		root.clipboard_append(converted_text)
		root.update()
		return converted_text
	finally:
		root.destroy()


def main() -> None:
	if sys.argv[1:] == ["--clipboard"]:
		print(fix_clipboard())
		return

	text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else input("Text: ")
	print(fix_slovak(text))


if __name__ == "__main__":
	main()
