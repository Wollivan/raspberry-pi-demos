from sense_hat import SenseHat

sense = SenseHat()

sense.clear(0,0,0)
     
while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)

	if x == 0 and y == 0 and z == 1:
		sense.clear(0,255,0)
	else:
		sense.clear(255,0,0)

	print("x={0}, y={1}, z={2}".format(x, y, z))

