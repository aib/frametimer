import frametimer
import time

SLEEP_TIMES = [
#	1, .8, .667, .5, .4, .333, .2, .1667, .1, .08, .0667,
	.05, .04, .0333, .02, .01667, .01, .008, .00667, .005, .004, .00333, .002, .001, .0001, .00001,
]
MEASURE_DURATION = 10

ft = frametimer.FrameTimer()

def do_sleep(t):
	ss = time.perf_counter()
#	time.sleep(t)
	ft.accurate_sleep_until(ss + t)
	se = time.perf_counter()
	return se - ss

def main():
	for sleep_time in SLEEP_TIMES:
		start_time = time.monotonic()
		times = []

		while True:
			now = time.monotonic()
			if now - start_time >= MEASURE_DURATION:
				break

			d = do_sleep(sleep_time)
			times.append(d)

		errs = [abs(t - sleep_time) for t in times]
		avgerr = sum(errs) / len(errs)
		print(f"target: {sleep_time:.5f}, avg: {sum(times) / len(times):.5f}, min: {min(times):.5f}, max: {max(times):.5f}, err: {avgerr:.5f} avg ({avgerr * 100 / sleep_time:6.2f}%), {max(errs):.5f} max ({max(errs) * 100 / sleep_time:6.2f}%)")

if __name__ == '__main__':
	main()
