import pynput
from pynput.keyboard import Listener, Key
import ai

typing = ''  # Var Typing to hold what the user is typing or has typed till yet

def press(key): 
    global typing 
    new = ''
    try:
        if key != Key.backspace:  # If user presses the backspace, the last letter of the Typing is removed
            typing += key.char
            print(typing)
            accesing_matches(typing)

        else:  # If user typed a letter, then append the letter to Typing
            typing = typing[:-1]
            accesing_matches(typing)

        if key == Key.space:
            typing = ''
            print(typing)

    except AttributeError:  # If user pressed keys like Alt, Delete, Enter, Space etc, nothing should happen
        pass

def release(key):
    global typing
    if key == Key.space or key == Key.enter:  # Checking for space, so as to reset Typing
        typing = ''
        print(typing)

def accesing_matches(_input):  # To trigger the function in AI so it can send the data to view to view it on GUI 
    matches = ai.matching(_input)
    print(list(matches))
    

with Listener(on_press=press, on_release=release) as listener:
    listener.join()

# CodeGameFun's Autocomplete specially for IDLE users
