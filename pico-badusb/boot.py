from badusb.boot import Boot

try:
    from supervisor import set_usb_identification
except ModuleNotFoundError:
    set_usb_identification = lambda **kwargs: print(kwargs)

set_usb_identification(
    manufacturer = 'limour',
    product = 'keyboard',
    vid = 0x1d6b,
    pid = 0x1347
)

# Loads default device setup
if __name__ == "__main__":
    Boot()
