from badusb.command import Command

# Loads and executes commands from the payload
if __name__ == "__main__":
    Command().execute("./payload.txt")
