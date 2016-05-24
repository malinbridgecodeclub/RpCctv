from gpiozero import MotionSensor,LightSensor
import sys
import picamera

def lights_On():
    print("I can see! :)")

def lights_Off():
    print("Who turned out the lights? >:(")

def start_camera():
        print("hello out there")
        myCamera.start_preview()

def stop_camera():
        print("i'm alown now you left, except how are you meant to see this message??")
        myCamera.stop_preview()

pir = MotionSensor(23)
myCamera = picamera.PiCamera()
myCamera.vflip = True
myCamera.brightness = 50
lightSensor = LightSensor(17)

while True:
    try:
        pir.when_motion = start_camera
        pir.when_no_motion = stop_camera
        #lightSensor.when_dark = stop_camera
        #lightSensor.when_light = start_camera
    except:
        type, value, traceback = sys.exc_info()
        print('Error opening %s' % (value))
        print("Stopping due to keyboard interrupt")
        break
