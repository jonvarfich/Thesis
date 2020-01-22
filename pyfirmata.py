import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyUSB0')
pin2 - board.get_pin('d:2:o')
while True:
	time.sleep(1)
	print("on")
	pin2.write(1)
	time.sleep(1)
	print("off")
	pin2.write(0)
