# Raspberry Pi Pico BadUSB
Pico BadUSB is a simple implementation of the [BadUSB](https://en.wikipedia.org/wiki/BadUSB) idea. The features it has will certainly prove themselves in most of the less and more demanding tasks. What characterizes Pico BadUSB is a simple [setup](https://github.com/kacperbartocha/pico-badusb#setup). Additionally, it uses a similar syntax as [DuckyScript](https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference), so writing the payload will be more intuitive for experienced Rubber Ducky users.

If you want to learn more about the Raspberry Pi Pico, refer to the [documentation](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf) or visit the [website](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico).

## Overview
The program was created to emulate USB devices, particularly keyboards, for the purpose of automating tasks by executing prepared payloads. Pico BadUSB was designed for use with Raspberry Pi Pico boards, such as the Pico, Pico W and Pico 2, but the program should also work on most boards that support CircuitPython. The ```Pico BadUSB v2.0.0``` release includes ```uf2``` files, which are used for setup purposes. They contain a build of customized ```CircuitPython 9.2.0``` with custom packages and filesystem initialization instructions for selected keyboard layouts such as ```QWERTY```, ```QWERTZ``` and ```AZERTY```.

## Setup
To correctly setup the device, hold the Boot Select ```BOOTSEL``` button while plugging the ```micro USB``` cable into the microcontroller. Once the device is detected by the system, drag and drop the ```uf2``` file of your choice onto the media, e.g. ```pico-badusb.uf2``` for the default ```QWERTY``` layout. After a moment, the device will reappear in the system with all the necessary files ready to go.

If the board has been used before, it may be necessary to [reset](https://github.com/kacperbartocha/pico-badusb#reset-flash) the device's Flash memory.

### Installation steps
0. [Reset Flash](https://github.com/kacperbartocha/pico-badusb#reset-flash) memory if you have used the device before
1. Hold down the ```BOOTSEL``` button while plugging in the ```micro USB``` cable
2. Drag and drop the file ```pico-badusb.uf2``` onto the media
3. Wait for the drive to remount with the following files:
    * ```boot.py```
    * ```boot_out.txt```
    * ```main.py```
    * ```payload.txt```
    * ```license.txt```

If you encounter a problem or if the selected ```uf2``` file doesn't work, the source code is available in the [pico-badusb directory](https://github.com/kacperbartocha/pico-badusb/tree/main/pico-badusb). To run the program, prepare the board using [Thonny IDE](https://thonny.org) or your own work environment with CircuitPython. Then move the ```boot.py```, ```main.py```, and ```payload.txt``` files to the root directory ```/```, and move the ```badusb``` directory to the ```lib``` subdirectory on the Raspberry Pi Pico drive.

### UF2 files
Pico BadUSB supports both the standard ```QWERTY``` keyboard layout and less common layouts like ```QWERTZ``` and ```AZERTY```. Due to this variety, the table below contains the ```uf2``` files for deployment on Raspberry Pi Pico boards.

| Board  | Layout       | File                                                                                                                        | MD5                                    |
|:-------|:-------------|:----------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| Pico   | ```QWERTY``` | [pico-badusb.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb.uf2)                   | ```78bd80bac2f451fd87a586460f52350c``` |
| Pico W | ```QWERTY``` | [pico-badusb-w.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-w.uf2)               | ```e53cef1f5bb97ca39ab976239854ada4``` |
| Pico 2 | ```QWERTY``` | [pico-badusb-2.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-2.uf2)               | ```a8b9f56ab1c26579a7f5551b57accdbe``` |
| Pico   | ```QWERTZ``` | [pico-badusb-qwertz.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-qwertz.uf2)     | ```662ccbcb6c9eab3b41ba6fa43aac6bd9``` |
| Pico W | ```QWERTZ``` | [pico-badusb-w-qwertz.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-w-qwertz.uf2) | ```2f4a04d8c68941d56648ab97785c09c2``` |
| Pico 2 | ```QWERTZ``` | [pico-badusb-2-qwertz.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-2-qwertz.uf2) | ```06263d2c851b2064a6e51800b1b4ab1a``` |
| Pico   | ```AZERTY``` | [pico-badusb-azerty.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-azerty.uf2)     | ```bca8af6048141ccb382e4824c4049ec8``` |
| Pico W | ```AZERTY``` | [pico-badusb-w-azerty.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-w-azerty.uf2) | ```99e63c5cd282ca5c87080b8d2f6e3748``` |
| Pico 2 | ```AZERTY``` | [pico-badusb-2-azerty.uf2](https://github.com/kacperbartocha/pico-badusb/releases/download/v2.0.0/pico-badusb-2-azerty.uf2) | ```aafad906286b0210efab990281b2deb5``` |

### Reset Flash
In order to reset the flash memory of the device, simply hold down the ```BOOTSEL``` button while plugging in the ```micro USB``` cable. Then, drag and drop the file ```flash_nuke.uf2``` onto the storage. The file can be downloaded from the Raspberry Pi [website](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2). If you don't see mass memory, make sure you removed the jumper link between pin ```GP1``` and ```GND```.

## Manual
The entire program is based on the content of the ```payload.txt``` file, or another file, depending on whether you changed the path to the file in ```main.py```. The syntax must follow certain rules to execute correctly. In theory, the program will not stop when it detects a syntax error, instead, it will ignore the problematic code fragment, so make sure that the syntax is correct. Each time you save the ```payload.txt``` file, its content will be automatically executed, so quickly remove the medium if you do not want to run the instructions on your computer or enable [development mode](https://github.com/kacperbartocha/pico-badusb#development).

### Commands
Compared to DuckyScript, Pico BadUSB's syntax is significantly simplified, leaving only basic functions. Another difference is the inclusion of the keywords ```PRESS``` and ```HOTKEY```, which are required before using keys like ```CONTROL```, ```ALT```, or ```DELETE```, as well as their combinations. Syntactically incorrect elements will be skipped but will not interfere with the execution of the program. Keywords such as [commands](https://github.com/kacperbartocha/pico-badusb#commands) and [keycodes](https://github.com/kacperbartocha/pico-badusb#keycodes) can be written with any combination of lowercase and uppercase letters.

| Command   | Description                         | Example                       |
|:----------|:------------------------------------|:------------------------------|
| REM       | Adds a comment                      | ```REM This is a comment```   |
| DELAY     | Adds a delay                        | ```DELAY 500```               |
| TYPESPEED | Changes the typing speed            | ```TYPESPEED 100```           |
| PRESS     | Alias to ```HOTKEY``` command       | ```PRESS ENTER```             |
| HOTKEY    | Enters key combination              | ```HOTKEY GUI R```            |
| STRING    | Enters a string of ASCII characters | ```STRING This is a string``` |
| LED       | Turns on/off the onboard diode      | ```LED ON ```                 |

##### REM
This command is discretionary, in fact, to achieve the effect of a comment, it is sufficient to type anything at the beginning of the line that is not a keyword of the commands ```DELAY```, ```TYPESPEED```, ```PRESS```, ```HOTKEY```, ```STRING```, or ```LED```. After the fixed word, enter the content of the comment.

##### DELAY
The ```DELAY``` command defines the delay in milliseconds between individual payload instructions. If no value is defined, the default delay value of ```500``` milliseconds will be used.

##### TYPESPEED
```TYPESPEED``` defines the delay in milliseconds between the characters entered from the string sequence within the ```STRING``` command. The default value is ```0```, which means no delay.

##### PRESS
After the keyword ```PRESS```, you can specify up to 6 keys, which can be provided as keycodes or as characters from the ASCII table. The keys are pressed in the order in which they are entered and released simultaneously. The ```PRESS``` command is an alias for the ```HOTKEY``` command.

##### HOTKEY
After the keyword ```PRESS```, you can specify up to 6 keys, which can be provided as keycodes or as characters from the ASCII table. The keys are pressed in the order in which they are entered and released simultaneously.

##### STRING
The ```STRING``` command converts the following string from the ASCII table (except for ```\n``` and ```\r```) into a series of keystrokes. Make sure that when writing the payload, you do not include characters outside the ASCII table, otherwise, they will be ignored.

##### LED
The command allows you to enable or disable the built-in LED. The command ```LED ON``` is used to turn on the diode, and ```LED OFF``` is used to turn it off. The keyword ```OFF``` is discretionary, the LED will turn off if there is no additional value or if a value other than ```ON``` is entered.

### Keycodes
Keycodes allow you to refer to a key that cannot be represented as an ASCII character. Their use is only permitted in conjunction with the keywords ```PRESS``` or ```HOTKEY``` at the beginning of a line. For formality, they are written in capital letters, but the program will interpret them correctly even if they are written in lowercase.

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
```ALTGR``` ```GUI``` ```COMMAND``` ```WINDOWS```

#### Lock Keys
```CAPSLOCK``` ```NUMLOCK``` ```SCROLLOCK```

### Example
The following example demonstrates the full functionality of Pico BadUSB. First, it activates the built-in LED, then, using [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) features, we open the defined link in the default browser. Finally, the LED turns off.

```text
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

## Other features
The functionality of the Pico BadUSB tool can be extended by creating a physical connection between individual pins as well as by making custom changes within the module's source code.

### Storage
In order to hide the visibility of the storage, the media memory can be turned off by shorting ```GP1``` pin to ground ```GND```. It is recommended to connect ```GP1``` pin in position ```2``` with ```GND``` pin in position ```3```, referring to the markings on the Raspberry Pi Pico [pinout diagram](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf).

If you encounter a problem and are sure that you have the jumpers connected properly, make sure that a file named ```boot.py``` is available in storage with the following code.

```python
from badusb.boot import Boot

# You can omit the if-else statement
if __name__ == "__main__":
    Boot()
```

### Development
Since the contents of the ```payload.txt``` file are executed each time it is saved, writing the payload may be difficult. For this reason, the ability to stop the payload execution has been added by shorting ```GP5``` pin in position ```7``` with ```GND``` pin in position ```8```, referring to the markings on the Raspberry Pi Pico [pinout diagram](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf). As long as the pins are connected, the payload will not execute. Once the jumper is removed, the device will start executing the instructions contained in the ```payload.txt``` file.

If you encounter a problem and are sure that you have the jumpers connected properly, make sure that a file named ```boot.py``` is available in storage.

### Layout
By using the source code, you can freely utilize the defined layouts ```QWERTY```, ```QWERTZ```, and ```AZERTY``` by modifying the contents of the file ```keyboard.py```. To make changes, you must first import the appropriate layout with ```from .layouts import QWERTY```, and then assign its values to the ```ASCII``` variable ```ASCII = QWERTY``` within the ```Keyboard``` class.

## References
\[1\] [Raspberry Pi Ltd. (2024). Raspberry Pi Pico Python SDK](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)\
\[2\] [Raspberry Pi Ltd. (2024). Getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico)\
\[3\] [Raspberry Pi Ltd. (2024). Raspberry Pi Pico Pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)\
\[4\] [MicroPython & CircuitPython contributors. (2024). Adafruit CircuitPython](https://docs.circuitpython.org)\
\[5\] [Scott Shawcroft. (2024). Adafruit HID library](https://docs.circuitpython.org/projects/hid)
