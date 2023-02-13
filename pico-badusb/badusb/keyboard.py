from usb_hid import Device

# Keyboard handler class
class Keyboard:
    
    # Keycodes
    UP = 0x52
    DOWN = 0x51
    LEFT = 0x50
    RIGHT = 0x4F
    PAGEUP = 0x4B
    PAGEDOWN = 0x4E
    HOME = 0x4A
    END = 0x4D
    INSERT = 0x49
    DELETE = 0x4C
    BACKSPACE = 0x2A
    TAB = 0x2B
    SPACE = 0x2C
    ENTER = 0x28
    ESCAPE = 0x29
    PAUSE = 0x48
    PRINTSCREEN = 0x46
    MENU = 0x65
    F1 = 0x3A
    F2 = 0x3B
    F3 = 0x3C
    F4 = 0x3D
    F5 = 0x3E
    F6 = 0x3F
    F7 = 0x40
    F8 = 0x41
    F9 = 0x42
    F10 = 0x43
    F11 = 0x44
    F12 = 0x45
    SHIFT = 0xE1
    ALT = 0xE2
    CONTROL = 0xE0
    CTRL = CONTROL
    GUI = 0xE3
    COMMAND = GUI
    WINDOWS = GUI
    CAPSLOCK = 0x39
    NUMLOCK = 0x53
    SCROLLOCK = 0x47
    
    # ASCII Layout
    ASCII = (
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x2a"
        b"\x2b"
        b"\x28"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x29"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x00"
        b"\x2c"
        b"\x9e"
        b"\xb4"
        b"\xa0"
        b"\xa1"
        b"\xa2"
        b"\xa4"
        b"\x34"
        b"\xa6"
        b"\xa7"
        b"\xa5"
        b"\xae"
        b"\x36"
        b"\x2d"
        b"\x37"
        b"\x38"
        b"\x27"
        b"\x1e"
        b"\x1f"
        b"\x20"
        b"\x21"
        b"\x22"
        b"\x23"
        b"\x24"
        b"\x25"
        b"\x26"
        b"\xb3"
        b"\x33"
        b"\xb6"
        b"\x2e"
        b"\xb7"
        b"\xb8"
        b"\x9f"
        b"\x84"
        b"\x85"
        b"\x86"
        b"\x87"
        b"\x88"
        b"\x89"
        b"\x8a"
        b"\x8b"
        b"\x8c"
        b"\x8d"
        b"\x8e"
        b"\x8f"
        b"\x90"
        b"\x91"
        b"\x92"
        b"\x93"
        b"\x94"
        b"\x95"
        b"\x96"
        b"\x97"
        b"\x98"
        b"\x99"
        b"\x9a"
        b"\x9b"
        b"\x9c"
        b"\x9d"
        b"\x2f"
        b"\x31"
        b"\x30"
        b"\xa3"
        b"\xad"
        b"\x35"
        b"\x04"
        b"\x05"
        b"\x06"
        b"\x07"
        b"\x08"
        b"\x09"
        b"\x0a"
        b"\x0b"
        b"\x0c"
        b"\x0d"
        b"\x0e"
        b"\x0f"
        b"\x10"
        b"\x11"
        b"\x12"
        b"\x13"
        b"\x14"
        b"\x15"
        b"\x16"
        b"\x17"
        b"\x18"
        b"\x19"
        b"\x1a"
        b"\x1b"
        b"\x1c"
        b"\x1d"
        b"\xaf"
        b"\xb1"
        b"\xb0"
        b"\xb5"
        b"\x4c"
    )
    
    # Initial setup
    def __init__(self) -> None:
        self._keyboard = Device.KEYBOARD
        self._report = bytearray(8)
        self._report_modifier = memoryview(self._report)[0:1]
        self._report_keys = memoryview(self._report)[2:]
        
        self.release()
    
    # Presses up to 6 unique keys
    def press(self, *keycodes: int) -> None:
        for keycode in keycodes:
            if 0xE0 <= keycode <= 0xE7:
                self._report_modifier[0] |= 1 << (keycode - 0xE0)
                
            else:
                report_keys = self._report_keys
                for i in range(6):
                    report_key = report_keys[i]
                    
                    if report_key == 0:
                        report_keys[i] = keycode
                        break
                    
                    if report_key == keycode:
                        break
            
        self._keyboard.send_report(self._report)
    
    # Enters a key combination
    def hotkey(self, *keycodes: int) -> None:
        self.press(*keycodes)
        self.release()
    
    # Enters an ASCII character string
    def string(self, string: str) -> None:
        for char in string:
            ordinal = ord(char)
            
            if ordinal < 0x80:
                keycode = self.ASCII[ordinal]
                
                if keycode > 0x80:
                    keycode ^= 0x80
                    self.press(*[self.SHIFT, keycode])
                    
                else:
                    self.press(*[keycode])
                
                self.release()
        
    # Releases all pressed keys
    def release(self) -> None:
        for i in range(8):
            self._report[i] = 0
            
        self._keyboard.send_report(self._report)
