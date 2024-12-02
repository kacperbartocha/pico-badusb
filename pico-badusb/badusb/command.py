from time import sleep
from board import LED, GP5
from digitalio import DigitalInOut, Direction, Pull
from .keyboard import Keyboard
import storage

# Command handler class
class Command:
    
    # Initial setup
    def __init__(self) -> None:
        self.__keyboard = Keyboard()
        self.__led = DigitalInOut(LED)
        self.__led.direction = Direction.OUTPUT
        self.__typespeed = 0.0
        self.__delay = 0.5
        self.__string = ""
        self.__arguments = []
        self.__pause()

    # Pauses the load execution
    def __pause(self) -> None:
        gp5 = DigitalInOut(GP5)
        gp5.switch_to_input(pull=Pull.UP)
        
        while not gp5.value:
            pass

    # Alias to HOTKEY
    def press(self) -> None:
        self.hotkey()
    
    # Enters a key combination
    def hotkey(self) -> None:
        keycodes = []
        
        for argument in self.__arguments:
            if len(argument) == 1:
                ordinal = ord(argument.lower())
                
                if ordinal < 0x80:
                    keycode = self.__keyboard.ASCII[ordinal]
                    
                    keycodes.append(*keycode)
            
            elif hasattr(Keyboard, argument.upper()):
                keycodes.append(getattr(Keyboard, argument.upper()))
        
        self.__keyboard.hotkey(*keycodes)
    
    # Enters a string of ASCII characters
    def string(self) -> None:
        self.__keyboard.string(self.__string, self.__typespeed )
    
    # Sets the type speed of strings
    def typespeed(self) -> None:
        if len(self.__arguments) > 0:
            self.__typespeed = int(self.__arguments[0]) / 1000
    
    # Sets the delay between commands
    def delay(self) -> None:
        if len(self.__arguments) > 0:
            time = int(self.__arguments[0]) / 1000
        
        else:
            time = self.__delay
        
        sleep(time)
    
    # Turns on/off the onboard LED diode
    def led(self) -> None:
        if len(self.__arguments) > 0:
            if self.__arguments[0].lower() == "on":
                self.__led.value = True
            
            else:
                self.__led.value = False
    
    # Executes instructions and validates them
    def execute(self, path: str) -> None:
        with open(path, "r", encoding="utf-8") as f:
            payload = f.readlines()
        storage.umount('/')
        for string in payload:
            self.__string = string.rstrip('\n\r')
            if self.__string.startswith('STRING'):
                self.__arguments = ['STRING']
            else:
                self.__arguments = self.__string.split(" ")
            if len(self.__arguments) > 0:
                command = self.__arguments.pop(0).lower()
                
                if hasattr(Command, command):
                    self.__string = self.__string[len(command) + 1:]
                    
                    try:       
                        getattr(Command, command)(self)
                    
                    except Exception as e:
                        self.__keyboard.release()
