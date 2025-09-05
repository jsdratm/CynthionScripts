#!/usr/bin/env python3

# This script is designed to use the Cynthion device to simulate a USB keyboard, with random buttons and modifiers (ctrl, alt, etc.) being pressed repeatedly

import random
import asyncio

from facedancer                      import main
from facedancer.devices.keyboard     import USBKeyboardDevice
from facedancer.classes.hid.keyboard import KeyboardKeys, KeyboardModifiers
  
device = USBKeyboardDevice()
  
# This function randomly selects and types key combinations (including modifiers) indefinitely.
async def fuzz_usb_keyboard(): 
    # Wait for device to connect
    await asyncio.sleep(2)
  
    # Get all possible KeyboardKeys
    all_keys = [(name, value) for name, value in KeyboardKeys.__members__.items()]
  
    while True:
        # Randomly select a key
        key_name, random_key = random.choice(all_keys)
  
        # Randomly select a combination of modifiers (could be none)
        selected_mods = select_random_modifiers()
        random_modifiers = combine_modifiers(selected_mods)
        mod_names = ", ".join(selected_mods)
        print(f"Pressing key {key_name} with modifiers {mod_names} for 0.1s")
  
        # Type the selected key with the selected modifiers
        await device.type_scancode(random_key, modifiers = random_modifiers if random_modifiers != 0 else None, duration=0.1)
        await asyncio.sleep(0.1)
  
# Returns a list of KeyboardModifiers keys selected randomly (1-3)
def select_random_modifiers():
    all_mod_keys = list(KeyboardModifiers.__members__.keys())
    count = random.randint(0, min(3, len(all_mod_keys)))
    return random.sample(all_mod_keys, count)
  
# Combines KeyboardModifiers values for the given keys using OR operation. Returns 0 if no keys are provided.
def combine_modifiers(mod_keys):
    if not mod_keys:
        return 0
    result = KeyboardModifiers.__members__[mod_keys[0]]
    for key in mod_keys[1:]:
        result |= KeyboardModifiers.__members__[key]
    return result
  
main(device, fuzz_usb_keyboard())
