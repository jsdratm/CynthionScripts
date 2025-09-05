#!/usr/bin/env python3

# This script is designed to use the Cynthion to act as a USB keyboard and repeatedly send a user-specified keyboard command at a high frequency.  It is useful to test specific commands while a device is rebooting.

import asyncio
  
from facedancer                   import main
from facedancer.devices.keyboard  import USBKeyboardDevice
from facedancer.classes.hid.keyboard import KeyboardKeys, KeyboardModifiers
  
device = USBKeyboardDevice()

# This function prompts the user for a selection, then enters an infinite loop where it repeatedly sends the specified button(s)
async def send_keyboard_command():
    # Wait for device to connect
    await asyncio.sleep(2)
  
    user_input = input("Select an option:\n1. ctrl+alt+del\n2. del\n3. f2\n4. ESC\n5. F10\n6. ctrl+c\n7. alt+tab\n8. meta+d\n9. alt+f4\n10. ctrl+alt+t\n11. ctrl+alt+f1\n12. ctrl+alt+f2\n13. alt+shift+tab\n14. meta+d\n15. prtscr\n16. volume down\n17. power\n")
    if user_input == '1':
        await ctrl_alt_del()
    elif user_input == '2':
        await delete()
    elif user_input == '3':
        await F2()
    elif user_input == '4':
        await ESC()
    elif user_input == '5':
        await F10()
    elif user_input == '6':
        await ctrl_c()
    elif user_input == '7':
        await alt_tab()
    elif user_input == '8':
        await meta_d()
    elif user_input == '9':
        await alt_f4()
    elif user_input == '10':
        await ctrl_alt_t()
    elif user_input == '11':
        await ctrl_alt_f1()
    elif user_input == '12':
        await ctrl_alt_f2()
    elif user_input == '13':
        await alt_shift_tab()
    elif user_input == '14':
        await meta_a()
    elif user_input == '15':
        await prtscr()
    elif user_input == '16':
        await vol_down()
    elif user_input == '17':
        await power()
    else:
        print("Invalid option selected.")
        return
  
async def ctrl_alt_del():
    # press ctrl-alt-del rapidly
    while True:
        print("Pressing ctrl-alt-del for 0.1s")
        await device.type_scancode(KeyboardKeys.DELETE, modifiers=KeyboardModifiers.MOD_LEFT_CTRL | KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def ctrl_alt_t():
    # press ctrl-alt-t rapidly
    while True:
        print("Pressing ctrl-alt-t for 0.1s")
        await device.type_scancode(KeyboardKeys.T, modifiers=KeyboardModifiers.MOD_LEFT_CTRL | KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def ctrl_alt_f1():
    # press ctrl-alt-f1 rapidly
    while True:
        print("Pressing ctrl-alt-f1 for 0.1s")
        await device.type_scancode(KeyboardKeys.F1, modifiers=KeyboardModifiers.MOD_LEFT_CTRL | KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def ctrl_alt_f2():
    # press ctrl-alt-f2 rapidly
    while True:
        print("Pressing ctrl-alt-f2 for 0.1s")
        await device.type_scancode(KeyboardKeys.F2, modifiers=KeyboardModifiers.MOD_LEFT_CTRL | KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def ctrl_c():
    # press ctrl-c rapidly
    while True:
        print("Pressing ctrl-c for 0.1s")
        await device.type_scancode(KeyboardKeys.C, modifiers=KeyboardModifiers.MOD_LEFT_CTRL, duration=0.1)
        asyncio.sleep(0.1)
  
async def alt_tab():
    # press alt-tab rapidly
    while True:
        print("Pressing alt-tab for 0.1s")
        await device.type_scancode(KeyboardKeys.TAB, modifiers=KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def alt_f4():
    # press alt-f4 rapidly
    while True:
        print("Pressing alt-f4 for 0.1s")
        await device.type_scancode(KeyboardKeys.F4, modifiers=KeyboardModifiers.MOD_LEFT_ALT, duration=0.1)
        asyncio.sleep(0.1)
  
async def meta_d():
    # press meta-d rapidly
    while True:
        print("Pressing meta-d for 0.1s")
        await device.type_scancode(KeyboardKeys.D, modifiers=KeyboardModifiers.MOD_LEFT_META, duration=0.1)
        asyncio.sleep(0.1)
  
async def meta_a():
    # press meta-a rapidly
    while True:
        print("Pressing meta-a for 0.1s")
        await device.type_scancode(KeyboardKeys.A, modifiers=KeyboardModifiers.MOD_LEFT_META, duration=0.1)
        asyncio.sleep(0.1)
  
async def delete():
    # press del rapidly
    while True:
        print("Pressing del for 0.1s")
        await device.type_scancode(KeyboardKeys.DELETE, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def ESC():
    # press ESC rapidly
    while True:
        print("Pressing esc for 0.1s")
        await device.type_scancode(KeyboardKeys.ESC, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def prtscr():
    # press prtscr rapidly
    while True:
        print("Pressing printscr for 0.1s")
        await device.type_scancode(KeyboardKeys.SYSRQ, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def vol_down():
    # press volume down rapidly
    while True:
        print("Pressing volume down for 0.1s")
        await device.type_scancode(KeyboardKeys.VOLUMEDOWN, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def F2():
    # press F2 rapidly
    while True:
        print("Pressing f2 for 0.1s")
        await device.type_scancode(KeyboardKeys.F2, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def F10():
    # press F10 rapidly
    while True:
        print("Pressing f10 for 0.1s")
        await device.type_scancode(KeyboardKeys.F10, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def power():
    # press power rapidly
    while True:
        print("Pressing power for 0.1s")
        await device.type_scancode(KeyboardKeys.POWER, modifiers=None, duration=0.1)
        asyncio.sleep(0.1)
  
async def alt_shift_tab():
    # press alt-shift-tab rapidly
    while True:
        print("Pressing alt-shift-tab for 0.1s")
        await device.type_scancode(KeyboardKeys.TAB, modifiers=KeyboardModifiers.MOD_LEFT_ALT | KeyboardModifiers.MOD_LEFT_SHIFT, duration=0.1)
        asyncio.sleep(0.1)
  
main(device, send_keyboard_command())
