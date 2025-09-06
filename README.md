# CynthionScripts
Python scripts written for the Cynthion by Great Scott Gadgets (https://greatscottgadgets.com/cynthion/)

USB HID Reference https://www.usb.org/sites/default/files/hid1_11.pdf

Before running a script, make sure you connect the Cynthion to host and target using USB cables and run the "cynthion run facedancer" command from your host

* usb-keyboard-random-fuzz.py - This script is designed to use the Cynthion device to simulate a USB keyboard, with random buttons and modifiers (ctrl, alt, etc.) being pressed repeatedly
* usb-keyboard-command-spamming.py - This script is designed to use the Cynthion to act as a USB keyboard and repeatedly send a user-specified keyboard command at a high frequency.  It is useful to test specific keyboard commands while a device is rebooting.
* usb-mouse-random-fuzz.py - [IN PROGRESS] This script is designed to use the Cynthion to act as a USB mouse, with random movement and button clicks
