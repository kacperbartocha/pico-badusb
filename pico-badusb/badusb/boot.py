from board import GP1
from digitalio import DigitalInOut, Pull
from storage import disable_usb_drive
from usb_cdc import disable as disable_usb_cdc
from usb_midi import disable as disable_usb_midi
import usb_hid

# Boot handler class
class Boot:
    
    # Initial setup
    def __init__(self) -> None:
        gp1 = DigitalInOut(GP1)
        gp1.switch_to_input(pull=Pull.UP)
        
        if not gp1.value:
            disable_usb_drive()
            disable_usb_cdc()
            disable_usb_midi()
            usb_hid.disable()
            usb_hid.enable((usb_hid.Device.KEYBOARD,))
