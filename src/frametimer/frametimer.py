import time

class FrameTimer:
	def __init__(self, target_fps=60, spin_time=0.001):
		self.target_fps = target_fps
		self.spin_time = spin_time
		self.last_tick_time = None

	def tick(self):
		if self.last_tick_time is None:
			self.last_tick_time = self.now()
			return 0.0

		next_tick_time = self.last_tick_time + (1 / self.target_fps)

		sleep_time = next_tick_time - self.now() - self.spin_time
		if sleep_time > 0:
			self.sleep(sleep_time)

		while True:
			now = self.now()
			if now >= next_tick_time:
				dt = now - self.last_tick_time
				self.last_tick_time = now
				return dt

	def sleep(self, seconds):
		time.sleep(seconds)

	def now(self):
		return time.perf_counter()
