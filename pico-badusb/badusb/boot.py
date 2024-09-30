from board import GP1
from digitalio import DigitalInOut, Pull
from storage import disable_usb_drive

# Boot handler class
class Boot:
    
    # Initial setup
    def __init__(self) -> None:
        gp1 = DigitalInOut(GP1)
        gp1.switch_to_input(pull=Pull.UP)
        
        if not gp1.value:
            disable_usb_drive()
