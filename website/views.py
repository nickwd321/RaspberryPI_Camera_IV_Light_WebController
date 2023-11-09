from flask import Blueprint , render_template
import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import os
import cv2
#GPIO
pinout = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinout,GPIO.OUT)

camera = PiCamera()
camera.close()

#camera = PiCamera()


##
views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("base.html")
	
@views.route('/base.html')
def base():
	GPIO.output(pinout, GPIO.HIGH)
	return render_template("base.html")
@views.route('/LightOn.html')
def lighton():
	GPIO.output(pinout, GPIO.LOW)
	return render_template("base.html")
@views.route('/TakePhoto.html')
def photo():
	camera = PiCamera()
	GPIO.output(pinout, GPIO.HIGH)
	camera.start_preview()
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image1.jpg')
	time.sleep(1)
	camera.stop_preview()
	camera.close()
	return render_template("base.html")
@views.route('/TakePhotoWithLight.html')
def photolight():
	camera = PiCamera()
	GPIO.output(pinout, GPIO.LOW)
	camera.start_preview()
	time.sleep(1)
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image2.jpg')
	camera.stop_preview()
	time.sleep(1)
	GPIO.output(pinout, GPIO.HIGH)
	camera.close()
	return render_template("base.html")

@views.route('/Comp2.html')
def comp2():
	camera = PiCamera()
	GPIO.output(pinout, GPIO.HIGH)
	camera.start_preview()
	time.sleep(1)
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image1.jpg')
	GPIO.output(pinout, GPIO.LOW)
	time.sleep(1)
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image2.jpg')
	GPIO.output(pinout, GPIO.HIGH)
	camera.stop_preview()
	camera.close()
	img1 = cv2.imread('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image1.jpg')
	img2 = cv2.imread('/home/nicho/Desktop/5VLEDWEBSITE/website/static/image2.jpg')
	subtracted = cv2.subtract(img1 , img2)
	cv2.imwrite('/home/nicho/Desktop/5VLEDWEBSITE/website/static/subimage.jpg', subtracted)
	return render_template("base.html")

@views.route('/Comp2Invert.html')
def comp2invert():
	camera = PiCamera()
	camera.image_effect = 'negative'
	GPIO.output(pinout, GPIO.HIGH)
	camera.start_preview()
	time.sleep(1)
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/negimage1.jpg')
	GPIO.output(pinout, GPIO.LOW)
	time.sleep(1)
	camera.capture('/home/nicho/Desktop/5VLEDWEBSITE/website/static/negimage2.jpg')
	GPIO.output(pinout, GPIO.HIGH)
	camera.stop_preview()
	camera.close()
	img1 = cv2.imread('/home/nicho/Desktop/5VLEDWEBSITE/website/static/negimage1.jpg')
	img2 = cv2.imread('/home/nicho/Desktop/5VLEDWEBSITE/website/static/negimage2.jpg')
	subtracted = cv2.subtract(img1 , img2)
	cv2.imwrite('/home/nicho/Desktop/5VLEDWEBSITE/website/static/negsubimage.jpg', subtracted)
	return render_template("base.html")
	
