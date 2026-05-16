"""Desktop Notifier for studying/practicing Data Science.

Features:
- Cross-platform notification using `win10toast` (Windows) or `plyer` if available.
- CLI options: interval, count, custom messages/resources, test mode (no GUI notifications).
- Default Data Science practice prompts included.

Usage examples:
  # Test mode: don't show OS notifications, just print/log 3 reminders every 1s
  python 15_Desktop_Notifier.py --test --interval 1 --count 3

  # Real mode: send reminder every hour until stopped
  python 15_Desktop_Notifier.py --interval 3600
"""

from __future__ import annotations

import argparse
import random
import time
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional

try:
	# Windows toast
	from win10toast import ToastNotifier
except Exception:
	ToastNotifier = None

try:
	# cross platform (may work on many OSes)
	from plyer import notification as plyer_notification
except Exception:
	plyer_notification = None


DEFAULT_MESSAGES: List[str] = [
	"Do a 15-minute Kaggle micro-challenge",
	"Practice a pandas DataFrame exercise",
	"Review probability and statistics notes for 10 minutes",
	"Try a short machine learning concept (e.g., regularization)",
	"Read one section of a Data Science blog or paper",
	"Implement one small algorithm from scratch (e.g., gradient descent)",
	"Solve a quick coding problem involving arrays or data parsing",
]

DEFAULT_RESOURCES: List[str] = [
	"https://www.kaggle.com/learn/overview",
	"https://pandas.pydata.org/docs/getting_started/index.html",
	"https://www.statlearning.com/",
	"https://scikit-learn.org/stable/tutorial/index.html",
]


class Notifier:
	"""Wrapper that picks an available notification backend."""

	def __init__(self):
		self.backend = None
		if ToastNotifier is not None:
			try:
				self.win_toast = ToastNotifier()
				self.backend = "win10toast"
			except Exception:
				self.win_toast = None
		if self.backend is None and plyer_notification is not None:
			self.backend = "plyer"

	def available(self) -> bool:
		return self.backend is not None

	def notify(self, title: str, message: str, duration: int = 6) -> None:
		"""Send a desktop notification using the best available backend.

		duration is in seconds and is advisory for some backends.
		"""
		if self.backend == "win10toast" and self.win_toast is not None:
			try:
				# threaded=False to ensure method blocks until shown
				self.win_toast.show_toast(title, message, duration=duration, threaded=False)
				return
			except Exception:
				pass
		if self.backend == "plyer":
			try:
				plyer_notification.notify(title=title, message=message, timeout=duration)
				return
			except Exception:
				pass
		# fallback: no GUI notification available
		raise RuntimeError("No desktop notification backend available")


def send_reminder(notifier: Optional[Notifier], title: str, message: str, resource: Optional[str], duration: int, test: bool, log_path: Optional[Path]) -> None:
	ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	line = f"[{ts}] {title} - {message}"
	if resource:
		line += f" (resource: {resource})"
	# test mode: print and optionally log
	if test:
		print(line)
		if log_path:
			with open(log_path, "a", encoding="utf-8") as f:
				f.write(line + "\n")
		return

	# try to send a GUI notification, otherwise fallback to printing
	try:
		if notifier is None:
			raise RuntimeError("No notifier provided")
		notifier.notify(title, message, duration=duration)
	except Exception:
		# fallback
		print(line)

	if resource:
		# Optionally open resource in browser — not on every platform click is available.
		try:
			webbrowser.open(resource)
		except Exception:
			pass


def run_loop(interval: float, count: Optional[int], messages: Iterable[str], resources: Iterable[str], title: str, duration: int, test: bool, log_path: Optional[Path]) -> None:
	notifier = Notifier() if not test else None
	if not test and not notifier.available():
		print("Warning: No desktop notification backend detected. Falling back to console output.")

	msg_list = list(messages)
	res_list = list(resources)

	i = 0
	try:
		while True:
			i += 1
			msg = random.choice(msg_list) if msg_list else "Time to practice Data Science!"
			resource = random.choice(res_list) if res_list else None
			send_reminder(notifier, title, msg, resource, duration, test, log_path)

			if count is not None and i >= count:
				break

			# sleep with small increments so ctrl-c is responsive
			slept = 0.0
			while slept < interval:
				to_sleep = min(0.5, interval - slept)
				time.sleep(to_sleep)
				slept += to_sleep
	except KeyboardInterrupt:
		print("\nStopped by user.")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Desktop notifier for Data Science practice reminders")
	parser.add_argument("--interval", type=float, default=3600.0, help="Seconds between reminders (default: 3600)")
	parser.add_argument("--count", type=int, default=None, help="Number of reminders to send (default: infinite until Ctrl-C)")
	parser.add_argument("--title", type=str, default="Practice Data Science", help="Notification title")
	parser.add_argument("--duration", type=int, default=6, help="Notification display duration in seconds")
	parser.add_argument("--message", action="append", help="Custom reminder message. Can be repeated.")
	parser.add_argument("--resource", action="append", help="Resource URL to open with the reminder. Can be repeated.")
	parser.add_argument("--test", action="store_true", help="Test mode: print/log reminders instead of sending desktop notifications")
	parser.add_argument("--log", type=str, default=None, help="Path to append a log of reminders (used in --test to record output)")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	messages = args.message if args.message else DEFAULT_MESSAGES
	resources = args.resource if args.resource else DEFAULT_RESOURCES
	log_path = Path(args.log) if args.log else None

	if args.test:
		print("Running in test mode — no GUI notifications will be shown.")
		if log_path:
			# clear log
			log_path.write_text("")

	print(f"Notifier starting: interval={args.interval}s, count={args.count or 'infinite'}, test={args.test}")
	run_loop(args.interval, args.count, messages, resources, args.title, args.duration, args.test, log_path)


if __name__ == '__main__':
	main()

    