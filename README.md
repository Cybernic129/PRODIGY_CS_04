# PRODIGY_CS_04

Basic Keylogger

How It Works
~ Dependencies: The program requires the pynput library to capture keyboard events. Install it using:
pip install pynput

~ The keylogger listens for keyboard events using the pynput library.
When a key is pressed, it logs the key to a file named key_log.txt.
Alphanumeric keys are logged as-is, while special keys (e.g., Enter, Shift) are logged with their corresponding representations.

~ The keylogger continues to run until the Escape (Esc) key is pressed. At this point, the logging stops, and the program terminates.

~ All logged keystrokes are appended to key_log.txt. Special keys are recorded in a readable format, and spaces are logged as spaces.

