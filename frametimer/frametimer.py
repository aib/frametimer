import sys
import time

class FrameTimer:
	def __init__(self, target_fps=60, spin_time=None):
		self.target_fps = target_fps
		if spin_time is None:
			self.spin_time = self._guess_spin_time()
		else:
			self.spin_time = spin_time
		self.time_between_frames = 1. / self.target_fps
		self.last_tick_time = None

	def _guess_spin_time(self):
		if sys.platform.startswith('linux'):
			return 0.001
		else:
			return 0.01

	def tick(self):
		if self.last_tick_time is None:
			self.last_tick_time = self.now()
			return 0.0

		self.accurate_sleep_until(self.last_tick_time + self.time_between_frames)

		now = self.now()
		dt = now - self.last_tick_time
		self.last_tick_time = now
		return dt

	def accurate_sleep_until(self, target_time):
		sleep_time = target_time - self.now() - self.spin_time
		if sleep_time > 0:
			self.sleep(sleep_time)

		while self.now() < target_time:
			pass

	def sleep(self, seconds):
		time.sleep(seconds)

	def now(self):
		return time.perf_counter()
