from board import GP1
from digitalio import DigitalInOut, Pull
from storage import disable_usb_drive

# Boot handler class
class Boot:
    def __init__(self) -> None:
        control = DigitalInOut(GP1)
        control.switch_to_input(pull=Pull.UP)
        
        if not control.value:
            disable_usb_drive()
