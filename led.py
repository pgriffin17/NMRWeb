#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Philip Griffin

import board
import os
import signal
import subprocess
import time
import sys
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 283       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)


# WARNING
# NEVER SET BRIGHTNESS ABOVE 127!!! This could overload the power
# supply unit or burn electrical connections (and potentially the building).
LED_BRIGHTNESS = 100  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53




def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
    
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        
def rainbowCycle(strip, wait_ms=10, iterations=1, start=0, count=None):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    if count==None:
        count = strip.numPixels()
    for j in range(256 * iterations):
        for i in range(start, count):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / count) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)
        
    colorWipe(strip, Color(0,0,0), 20)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    strip.show()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print('Rainbow animations.')
            rainbowCycle(strip, 0, 6)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)


