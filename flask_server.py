from flask import Flask
from flask_cors import CORS, cross_origin
import faulthandler
import serial
import re, sys, signal, os, time, datetime
import RPi.GPIO as GPIO

BITRATE = 19200
relay1_pin = 38
relay2_pin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(relay1_pin, GPIO.OUT)
GPIO.output(relay1_pin, GPIO.HIGH)
GPIO.setup(relay2_pin, GPIO.OUT)
GPIO.output(relay2_pin, GPIO.LOW)


def unlock_door_in(duration):
    print("Unlock turntile for entrance")
    GPIO.output(relay2_pin, GPIO.HIGH)
    time.sleep(duration)
    print("unlocked")
    GPIO.output(relay2_pin, GPIO.LOW)


def unlock_door_out(duration):
    print("Unlock turntile for exit")
    GPIO.output(relay1_pin, GPIO.HIGH)
    time.sleep(duration)
    print("unlocked")
    GPIO.output(relay1_pin, GPIO.LOW)


faulthandler.enable()
app = Flask(__name__)
cors = CORS(app)


@cross_origin()
@app.route('/open_turntile_entrance', methods=['GET', 'POST'])
def open_turntile_entrance():
    try:
        unlock_door_in(3)
        return True
    except:
        return False


@app.route('/open_turntile_exit', methods=['GET', 'POST'])
def open_turntile_exit():
    try:
        unlock_door_out(3)
        return True
    except:
        return False


if __name__ == '__main__':
    # load_model()

    # app.run(host="192.168.1.61", port=3005, debug=False)

    app.run()