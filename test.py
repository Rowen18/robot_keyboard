import keyboard
keyboard.add_hotkey('w+a',print,args=("2"),timeout=1)
keyboard.add_hotkey('w',print,args=("1"),timeout=1)

while True:
    keypress = keyboard.read_key()
    print("0")

    if keypress == "p":
        break
