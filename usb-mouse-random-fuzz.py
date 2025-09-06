#!/usr/bin/env python3

# This script is designed to use the Cynthion device to simulate a USB mouse, with random buttons and movements
# NOTE: Currently the mouse emulation and random movement works, but still need to add the random clicking logic

import asyncio
import random

from math import trunc

from facedancer                        import main
from facedancer                        import *
from facedancer.classes                import *
from facedancer.classes.hid.descriptor import *
from facedancer.classes.hid.usage      import *

@use_inner_classes_automatically
class USBMouseDevice(USBDevice):
    """ Simple USB mouse device. """

    name           : str = "USB mouse device"
    product_string : str  = "Non-suspicious Mouse"
    device_class             : int = USBDeviceClass.HID
    device_subclass          : int  = 1
    protocol_revision_number : int  = 2

    class MouseConfiguration(USBConfiguration):
        """ Primary USB configuration: act as a mouse. """

        class MouseInterface(USBInterface):
            """ Core HID interface for our mouse. """

            name                   : str = "USB mouse interface"
            class_number           : int = USBDeviceClass.HID
            subclass_number        : int = 1
            protocol_number        : int = 2

            class MouseEventEndpoint(USBEndpoint):
                number        : int             = 3
                direction     : USBDirection    = USBDirection.IN
                transfer_type : USBTransferType = USBTransferType.INTERRUPT
                interval      : int             = 10

            #
            # Raw descriptors -- TODO: build these from their component parts.
            #

            # Referenced from https://www.usb.org/sites/default/files/hid1_11.pdf Appendix E.8
            class HIDDescriptor(USBDescriptor):
                number            : int   = 0
                type_number       : int   = USBDescriptorTypeNumber.HID
                raw               : bytes = b'\x09\x21\x10\x01\x00\x01\x22\x32\x00'
                include_in_config : bool  = True

            # Referenced from https://www.usb.org/sites/default/files/hid1_11.pdf Appendix E.10
            class ReportDescriptor(HIDReportDescriptor):
                number : int   =  0
                fields : tuple = (

                    # Identify ourselves as a mouse.
                    USAGE_PAGE       (HIDUsagePage.GENERIC_DESKTOP),
                    USAGE            (HIDGenericDesktopUsage.MOUSE),
                    COLLECTION       (HIDCollection.APPLICATION),
                    USAGE_PAGE       (HIDGenericDesktopUsage.POINTER),
                    COLLECTION       (HIDCollection.PHYSICAL),
                    USAGE_PAGE       (HIDUsagePage.BUTTONS),

                    # Mouse buttons.
                    # These span the three buttons (left, right, middle),
                    # and each has two possible values (0 = unpressed, 1 = pressed).
                    USAGE_MINIMUM    (1),
                    USAGE_MAXIMUM    (3),
                    LOGICAL_MINIMUM  (0),
                    LOGICAL_MAXIMUM  (1),
                    REPORT_COUNT     (3),
                    REPORT_SIZE      (1),
                    INPUT            (variable=True),
                    
                    # Padding
                    REPORT_COUNT     (1),
                    REPORT_SIZE      (5),
                    INPUT            (constant=True),

                    # X and Y axis movement.
                    # These are signed values, with a range of -127 to +127.
                    USAGE_PAGE       (HIDUsagePage.GENERIC_DESKTOP),
                    USAGE            (HIDGenericDesktopUsage.X),
                    USAGE            (HIDGenericDesktopUsage.Y),
                    LOGICAL_MINIMUM  (0x81), # -127
                    LOGICAL_MAXIMUM  (0x7f), # 127
                    REPORT_SIZE      (8),
                    REPORT_COUNT     (2),
                    INPUT            (variable=True, relative=True),

                    END_COLLECTION   (),

                    # End the report.
                    END_COLLECTION   (),
                )    

            @class_request_handler(number = USBStandardRequests.GET_INTERFACE)
            @to_this_interface
            def handle_get_interface_request(self, request):
                # Silently stall GET_INTERFACE class requests.
                request.stall()

    def __post_init__(self):
        super().__post_init__()

        # Keep track of any pressed buttons
        self.active_buttons = set()


    def _generate_hid_report(self) -> bytes:
        """ Generates a single HID report for the given mouse state. """

        # For now, just return a report with no buttons pressed
        buttons_byte = 0

        # Randomly generate x and y movement values between -20 and 20
        x_byte = random.randint(-20, 20)
        y_byte = random.randint(-20, 20)

        # Convert to bytes
        x_byte_converted = (trunc(x_byte)) % 255
        y_byte_converted = (trunc(y_byte)) % 255

        print(f"buttons_byte: {buttons_byte}, x_byte: {x_byte_converted}, y_byte: {y_byte_converted}")

        return bytes([buttons_byte, x_byte_converted, y_byte_converted])


    def handle_data_requested(self, endpoint: USBEndpoint):
        """ Provide data once per host request. """
        report = self._generate_hid_report()
        endpoint.send(report)

device = USBMouseDevice()
  
# This function randomly moves and clicks the mouse indefinitely.
async def fuzz_usb_mouse(): 
    # Wait for device to connect
    await asyncio.sleep(2)
  
    while True:
        # Let the device do its thing
        await asyncio.sleep(1)
  
main(device, fuzz_usb_mouse())
