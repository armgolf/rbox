import RPi.GPIO as GPIO
import time
from time import sleep
import os
import datetime
from picamera import PiCamera
import requests
import json
import VL53L0X
import lcddriver

def main():
    def lights(a):
        if a == "Clearplasticbottle":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Cans":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Card":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Colouredplastic":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Paper":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Plastictray":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Yoghurt":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "HDPEmilk":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        elif a == "Foils":
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()
        else:
            print("Writing to display")
            display.lcd_display_string("Clear Plastic Bottle", 1) # Write line of text to first line of display
            display.lcd_display_string("Please Recycle", 2) # Write line of text to second line of display
            #display.lcd_display_string("in the white recycling bag", 3)  # Refresh the first line of display with a different message
            time.sleep(5)                                     # Give time for the message to be read
            display.lcd_clear()                               # Clear the display of any data
            time.sleep(2)                                     # Give time for the message to be read
            GPIO.cleanup()
            main()

    def identify():
        url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
        path = '/home/pi/Documents/SBDev/images'
        name_list = os.listdir(path)
        full_list = [os.path.join(path,i) for i in name_list]
        time_sorted_list = sorted(full_list, key=os.path.getmtime)
        sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
        lastfile = sorted_filename_list[-1]
        data = {'file': open('/home/pi/Documents/SBDev/images/'+lastfile, 'rb'), 'modelId': ('', 'fa42fc44-6319-4a32-ac97-04441896e9dd')}
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth('GvqHLwBkqU4tpSyXDU471CG6K1y5XYw8', ''), files=data)
        #print(response.text)
        data = json.loads(response.text)
        a = data["result"][0]["prediction"][0]["label"]
        #GPIO.output(18,GPIO.LOW)
        print(a)
        lights(a)


    def photo():
        path = '/home/pi/Documents/SBDev/images'
        name_list = os.listdir(path)
        full_list = [os.path.join(path,i) for i in name_list]
        time_sorted_list = sorted(full_list, key=os.path.getmtime)
        sorted_filename_list = [ os.path.basename(i) for i in time_sorted_list]
        lastfile = sorted_filename_list[-1]
        ending = lastfile[6:]
        string = ending[:-4]
        number = int(float(string))
        imagename = "-image"+str(number+1)+".jpg"
        print(imagename)
        camera = PiCamera()
        camera.resolution = (1200, 800)
        camera.rotation = 180
        #time.sleep(1)
        camera.capture('/home/pi/Documents/SBDev/images/'+imagename)
        camera.close()
        #GPIO.output(22,GPIO.LOW)
        #GPIO.output(18,GPIO.HIGH)
        try:
            identify()
        except: #ConnectionError as error:
            #print(error)
            print("Continuing script from the start")
            sleep(5)
            GPIO.cleanup()
            main()


    def distance():
        # Create a VL53L0X object
        tof = VL53L0X.VL53L0X()

        # Start ranging
        tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        timing = tof.get_timing()
        if (timing < 20000):
            timing = 20000
        print ("Timing %d ms" % (timing/1000))
        county = 0
        while 1:
            distance = tof.get_distance()
            print(distance)
            #print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
            if (distance < 330):
                print ("%d mm, %d cm" % (distance, (distance/10)))
                county = county + 1
                if county == 2:
                    object = True
                    print(object)
                    #GPIO.output(22,GPIO.HIGH)
                    county=0
                    tof.stop_ranging()
                    photo()
            time.sleep(timing/1000000.00)

        tof.stop_ranging()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    display = lcddriver.lcd()

    distance()

sleep(5)
main()
