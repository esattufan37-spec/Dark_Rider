import RPi.GPIO as GPIO
import time

pinler=[40,38,37,36,35]


GPIO.setmode(GPIO.BOARD)
for i in pinler:
    GPIO.setup(i,GPIO.OUT)

try:
    while True:
        for i in pinler:
            GPIO.output(i,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(i,GPIO.LOW)
        
        
        for i in reversed(pinler[1:-1]):
            GPIO.output(i,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(i,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()