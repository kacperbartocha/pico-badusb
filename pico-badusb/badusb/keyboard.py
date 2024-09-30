from time import sleep
from usb_hid import Device
from .layouts import QWERTY

# Keyboard handler class
class Keyboard:
    
    # ASCII layout
    ASCII = QWERTY
    
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
    ALTGR = 0xE6
    CONTROL = 0xE0
    CTRL = CONTROL
    GUI = 0xE3
    COMMAND = GUI
    WINDOWS = GUI
    CAPSLOCK = 0x39
    NUMLOCK = 0x53
    SCROLLOCK = 0x47
    
    # Initial setup
    def __init__(self) -> None:
        self.__keyboard = Device.KEYBOARD
        self.__report = bytearray(8)
        self.__report_modifier = memoryview(self.__report)[0:1]
        self.__report_keys = memoryview(self.__report)[2:]
        
        self.release()
    
    # Presses up to 6 unique keys
    def press(self, *keycodes: int) -> None:
        for keycode in keycodes:
            if 0xE0 <= keycode <= 0xE7:
                self.__report_modifier[0] |= 1 << (keycode - 0xE0)
            
            else:
                report_keys = self.__report_keys
                for i in range(6):
                    report_key = report_keys[i]
                    
                    if report_key == 0:
                        report_keys[i] = keycode
                        break
                    
                    if report_key == keycode:
                        break
        
        self.__keyboard.send_report(self.__report)
    
    # Enters a key combination
    def hotkey(self, *keycodes: int) -> None:
        self.press(*keycodes)
        self.release()
    
    # Enters an ASCII character string
    def string(self, string: str, typespeed: float) -> None:
        for char in string:
            ordinal = ord(char)
            
            if ordinal < 0x80:
                keycode = self.ASCII[ordinal]
                
                self.press(*keycode)
                self.release()
                
                sleep(typespeed)
    
    # Releases all pressed keys
    def release(self) -> None:
        for i in range(8):
            self.__report[i] = 0
            
        self.__keyboard.send_report(self.__report)
