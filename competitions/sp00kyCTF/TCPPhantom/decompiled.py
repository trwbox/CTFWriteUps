# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.9.5 (default, May 11 2021, 08:20:37) 
# [GCC 10.3.0]
# Embedded file name: challenge.py
# Compiled at: 2021-10-25 18:57:14
# Size of source mod 2**32: 1546 bytes
import sys
try:
    if sys.version_info[1] != 6:
        print('It seems you are using a different version of python than this program was compiled into bytecode on (python 3.6). If you are experiencing issues, please try that version')
    try:
        import pyttsx3
    except ImportError as error:
        print('For this synthesiser to work you need to install pyttsx3 with "pip3.6 install pyttsx3"')
        exit()

    introString = 'Hello, welcome to the new text to speech engine'
    engine = pyttsx3.init()
    engine.say(introString)
    engine.runAndWait()
    continueCollecting = True
    while continueCollecting:
        stringToSpeak = input('What would you like said aloud? Type q or empty line to exit\n')
        if stringToSpeak == 'q':
            continueCollecting = False
        elif stringToSpeak == '\n':
            continueCollecting = False
        else:
            engine.say(stringToSpeak)
            engine.runAndWait()

except OSError as error:
    print('If you are seeing this the required os components are not installed for pyttsx3 if you are on linux try run "sudo apt update && sudo apt install espeak ffmpeg libespeak1"')
# okay decompiling speakspellCompiled.pyc
