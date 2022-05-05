# frametimer

An accurate clock/timer that can be used to help obtain constant framerates. It uses a hybrid approach of sleeping for *most* of the required duration, then spin-waiting for the rest.

## Installation

```pip install frametimer```

(Or just grab the .py file, it's a simple module)

## Usage

```python
timer = frametimer.FrameTimer(60)

while run_main_loop:
	dt = timer.tick()

	update(dt)
	...
```
