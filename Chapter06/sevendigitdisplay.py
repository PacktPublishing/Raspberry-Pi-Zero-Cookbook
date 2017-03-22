import wiringpi
from time import sleep
#Define LED pins to letters
wiringpi.wiringPiSetupGpio()
def main():
	one = setdisplay(0,0,0,1,0,0,1,0)
	sleep(1)
	two  = setdisplay(0,1,1,1,1,1,0,0)
	sleep(1)
	three = setdisplay(0,1,1,1,0,1,1,0)
	sleep(1)
	four = setdisplay(1,1,0,1,0,0,1,0)
	sleep(1)
	five = setdisplay(1,1,1,0,0,1,1,0)
	sleep(1)
	six = setdisplay(1,1,0,0,1,1,1,0)
	sleep(1)
	seven = setdisplay(0,0,1,1,0,0,1,0)
	sleep(1)
	eight = setdisplay(1,1,1,1,1,1,1,0)
	sleep(1)
	nine = setdisplay(1,1,1,1,0,0,1,0)
	sleep(1)
	zero = setdisplay(1,0,1,1,1,1,1,0)
	sleep(1)
	off = setdisplay(0,0,0,0,0,0,0,0)
def setdisplay(b1,b2,b3,b4,b5,b6,b7,b8):
	a = 5   #Top Left
	b = 6	#Middle
	c = 21  #Top
	d = 22	#TopRight
	e = 23	#BottomLeft
	f = 24  #Bottom
	g = 25	#BottomRight
	h = 26  #Decimal
	wiringpi.digitalWrite(a,b1)
	wiringpi.digitalWrite(b,b2)
	wiringpi.digitalWrite(c,b3)
	wiringpi.digitalWrite(d,b4)
	wiringpi.digitalWrite(e,b5)
	wiringpi.digitalWrite(f,b6)
	wiringpi.digitalWrite(g,b7)
	wiringpi.digitalWrite(h,b8)
if __name__ == "__main__":
	main()
