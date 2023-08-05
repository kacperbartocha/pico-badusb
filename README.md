# Raspberry Pi Pico BadUSB

Pico BadUSB is a simple implementation of the [BadUSB](https://en.wikipedia.org/wiki/BadUSB) idea. The features it has
will certainly prove themselves in most of less and more demanding tasks. What characterizes Pico BadUSB is a
simple [setup](https://github.com/kacperbartocha/pico-badusb#setup). Additionally, it uses a similar syntax as
[DuckyScript](https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference), so writing the payload will
be more intuitive for experienced Rubber Ducky users.

If you want to learn more about the Raspberry Pi Pico, reach out to the 
[documentation](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) or visit the 
[website](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

## Overview
The program was created with a view to automating tasks by performing previously prepared payloads. During the
development process, the [CircuitPython documentation](https://docs.circuitpython.org) and the 
[Adafruit HID library](https://docs.circuitpython.org/projects/hid) was very helpful. Pico BadUSB was designed to be
used on a base Raspberry Pi Pico board, but it should also work on Pico W, a board with wireless module. The repository
includes a ```pico-badusb.uf2``` file which is used for setup purpose. It contains a build of customized
```CircuitPython 8.2.0``` with own packages and filesystem initialization instructions.

## Setup
To set up everything correctly, just hold down the Boot Select ```BOTSEL``` button while connecting the ```micro USB```
cable to the microcontroller. After a while, the mounted media should appear in the system, to which you just need to
drag and drop the file ```pico-badusb.uf2```, and then wait a moment. If the board has been used before, it may be
necessary to [reset](https://github.com/kacperbartocha/pico-badusb#reset) the Flash memory.

### Installation in steps:
0. [Reset Flash](https://github.com/kacperbartocha/pico-badusb#reset) memory if you have used the device before
1. Hold down the ```BOOTSEL``` button while connecting the ```micro USB``` cable
2. Drag and drop the file ```pico-badusb.uf2``` onto the media
3. Wait for the media to be remounted with the following files:
    * ```boot.py```
    * ```boot_out.txt```
    * ```main.py```
    * ```payload.txt```

If you run into a problem at some point, or if the ```pico-badusb.uf2``` file doesn't work, the source code is available
in the [pico-badusb directory](https://github.com/kacperbartocha/pico-badusb/tree/main/pico-badusb). To run the program,
prepare the board preferably using [Thonny IDE](https://thonny.org) or yourself to work with ```CircuitPython``` in any
version. Then move the ```boot.py```, ```main.py``` and ```payload.txt``` files to the root directory ```/```, and the
```badusb``` directory move to the ```lib``` subdirectory on the Pico media.

## Manual
The whole program is based on the content of the file ```payload.txt```, or another depending on whether you changed the
path to the file in ```main.py```. The syntax should follow certain rules to execute correctly. In theory, the program
will not stop when it detects a syntax error, but it will ignore the given code fragment, so make sure that the syntax
is correct. Each time you save the ```payload.txt``` file, its content will be automatically executed, so quickly remove
the medium if you do not want to run the instructions on your computer.

### Commands
Compared to DuckyScript, Pico BadUSB's syntax is significantly simplified, leaving only elementary functions. Another
difference is the appearance of the keyword ```PRESS``` and ```HOTKEY``` which are required before using keys like
```CONTROL```, ```ALT``` or ```DELETE``` and their combinations. Syntactically incorrect elements will be skipped but
will not interfere with the execution of the program. Keywords such as 
[commands](https://github.com/kacperbartocha/pico-badusb#commands) or
[keycodes](https://github.com/kacperbartocha/pico-badusb#keycodes) can be written with any combination of lowercase and
uppercase letters. 

| Command | Description                         | Example                       |
|:--------|:------------------------------------|:------------------------------|
| REM     | Adds a comment                      | ```REM This is a comment```   |
| PRESS   | Alias to ```HOTKEY``` command       | ```PRESS ENTER```             |
| HOTKEY  | Enters key combination              | ```HOTKEY GUI R```            |
| STRING  | Enters a string of ASCII characters | ```STRING This is a string``` |
| LED     | Turns on/off the onboard diode      | ```LED OFF ```                |

##### REM
This command is discretionary, in fact, to get the effect of a comment, it is enough to type anything at the beginning
of the line that is not a keyword of the command ```PRESS```, ```HOTKEY```, ```STRING``` or ```LED```. After the fixed
word, enter the comment content.

##### PRESS
After the keyword ```PRESS``` put up to 6 keys, they can be provided as keycodes as well as characters from the ASCII 
table. The keys are pressed in the order in which they were entered and simultaneously released. The ```PRESS``` command
is an alias for the ```HOTKEY``` command.

##### HOTKEY
After the keyword ```HOTKEY``` put up to 6 keys, they can be provided as keycodes as well as characters from the ASCII 
table. The keys are pressed in the order in which they were entered and simultaneously released.

##### STRING
The ```STRING``` command converts the following string from the ASCII table (except ```\n``` and ```\r```) into a string
of keystrokes. Make sure that when writing the payload you do not include characters from outside the ASCII table,
otherwise they will be ignored.

##### LED
The comment allows you to enable or disable the built-in LED. The command ```LED ON``` is used to turn on the diode, and
```LED OFF``` to turn it off. The keyword ```OFF``` is discretionary, the LED will go off if there is no additional
value or if a value other than ```ON``` is entered.

### Keycodes
Keycodes allow you to refer to a key that cannot be represented as an ASCII character. Their use is only allowed in
conjunction with the keyword ```PRESS``` or ```HOTKEY``` at the beginning of a line. For formality, they are written in
capital letters, but the program will interpret them correctly even if they are written in lower case. 

#### Cursor Keys
```UP``` ```DOWN``` ```LEFT``` ```RIGHT```\
```PAGEUP``` ```PAGEDOWN``` ```HOME``` ```END```\
```INSERT``` ```DELETE``` ```BACKSPACE```\
```SPACE``` ```TAB```

#### System Keys
```ENTER``` ```ESCAPE``` ```PAUSE``` ```PRINTSCREEN``` ```MENU```\
```F1``` ```F2``` ```F3``` ```F4``` ```F5``` ```F6``` ```F7```\
```F8``` ```F9``` ```F10``` ```F11``` ```F12```

#### Modifier Keys
```SHIFT``` ```CONTROL``` ```CTRL``` ```ALT```\
```GUI``` ```COMMAND``` ```WINDOWS```

#### Lock Keys
```CAPSLOCK``` ```NUMLOCK``` ```SCROLLOCK```

### Example
The following example shows the full functionality of Pico BadUSB. First, it launches the built-in LED, then using
[Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) features,
we run the defined link in the default browser. Finally, the LED turns off.

```bash
REM This is an example of a payload file
DELAY 1000
LED ON
HOTKEY GUI R
DELAY 500
STRING cmd.exe
PRESS ENTER
DELAY 500
STRING start https://youtu.be/dQw4w9WgXcQ
PRESS ENTER
LED OFF
```

## Storage
In order to hide the device actions, the mass memory can be turned off by shorting the ```GP1``` pin to the ground 
```GND```. It is recommended to connect the pin ```GP1``` in position ```2``` with the pin ```GND``` in position ```3```
, referring to the markings on the Raspberry Pi Pico
[pinout diagram](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf).

If you encounter a problem, and you are sure that you have jumpers connected properly, make sure that a file named
```boot.py``` is available in storage with the following code.

```python
from badusb.boot import Boot

# You can omit the if-else statement
if __name__ == "__main__":
    Boot()
```

## Reset
In order to reset the flash memory of the device, simply hold down the ```BOOTSEL``` button while plugging in the
```micro USB``` cable. Then drag and drop the file ```flash_nuke.uf2``` to the storage. The file can be downloaded from
the Raspberry Pi [website](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2). If you don't see mass memory, make
sure you removed the jumper link between pin ```GP1``` and ```GND```.
