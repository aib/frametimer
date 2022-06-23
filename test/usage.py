import frametimer
import time

total_elapsed = 0

def update(dt):
	global total_elapsed
	total_elapsed += dt

def main():
	timer = frametimer.FrameTimer(120)
	timer.tick()
	start_time = time.monotonic()

	frames = 0
	last_fps_time = start_time
	while True:
		dt = timer.tick()

		update(dt)

		frames += 1
		now = time.monotonic()
		if now - last_fps_time > 1:
			fps = frames / (now - last_fps_time)
			frames = 0
			last_fps_time = now
			wall_elapsed = now - start_time
			print(f"{fps:.5f} FPS, wall: {wall_elapsed:.6f} frametimer: {total_elapsed:.6f} diff: {total_elapsed - wall_elapsed:.9f}")

if __name__ == '__main__':
	main()
