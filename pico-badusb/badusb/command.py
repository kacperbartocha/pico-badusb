from time import sleep
from board import LED
from digitalio import DigitalInOut, Direction
from .keyboard import Keyboard

# Command handler class
class Command:
    
    # Initial setup
    def __init__(self) -> None:
        self._keyboard = Keyboard()
        self._led = DigitalInOut(LED)
        self._led.direction = Direction.OUTPUT
        self._delay = 500
        self._string = ""
        self._arguments = []
        
    # Alias to HOTKEY
    def press(self) -> None:
        self.hotkey()

    # Enters a key combination
    def hotkey(self) -> None:
        keycodes = []

        for argument in self._arguments:
            if len(argument) == 1:
                ordinal = ord(argument)
        
                if ordinal < 0x80:
                    keycode = self._keyboard.ASCII[ordinal]
                    
                    if keycode > 0x80:
                        keycode ^= 0x80
                    
                    keycodes.append(keycode)
            
            elif hasattr(Keyboard, argument.upper()):
                keycodes.append(getattr(Keyboard, argument.upper()))
        
        self._keyboard.hotkey(*keycodes)
    
    # Enters a string of ASCII characters
    def string(self) -> None:
        self._keyboard.string(self._string)
        
    # Sets the delay between commands
    def delay(self) -> None:
        if len(self._arguments) > 0:
            time = int(self._arguments[0])
        
        else:
            time = self._delay

        sleep(int(time) / 1000)
    
    # Turns on/off the onboard diode
    def led(self) -> None:
        if len(self._arguments) > 0:
            if self._arguments[0].lower() == "on":
                self._led.value = True
                
            else:
                self._led.value = False

    # Executes instructions and validates them
    def execute(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as payload:
            for string in payload.readlines():
                self._string = string.replace("\n", "").replace("\r", "")
                self._arguments = self._string.split(" ")

                if len(self._arguments) > 0:
                    command = self._arguments.pop(0).lower()
                    
                    if hasattr(Command, command):
                        self._string = self._string[len(command) + 1:]
                        
                        try:       
                            getattr(Command, command)(self)
                        
                        except Exception as e:
                            self._keyboard.release()
