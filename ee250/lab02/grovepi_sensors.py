""" EE 250L Lab 02: GrovePi Sensors
List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    PORT = 4    # D4
    potentiometer = 0
    grovepi.pinMode(potentiometer,"INPUT")
    full_angle = 300

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        distance = grovepi.ultrasonicRead(PORT)
        #read value from potentiometer [0,1023]
        rotary_value = int(grovepi.analogRead(potentiometer))
        #Calculate threshold distance [0,517]
        threshold = int(rotary_value /1023 *517)
        #
        if (threshold >= distance ):
        #print on lcd without freshing
            setText_norefresh(str(threshold) + "cm" + "  OBJ PRES \n" + str(distance) + "cm")
        else:
            setText_norefresh(str(threshold) + "cm" + "          \n" + str(distance) + "cm")

