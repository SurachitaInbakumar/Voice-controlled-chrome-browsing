import pyautogui
import time
import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()

def is_open():
    # To check if chrome is opened
    time.sleep(1)
    open = pyautogui.locateCenterOnScreen('Images/open.png')
    if (open):
        print('Chrome is opened')
        return True
    else:
        return False

def open_chrome():
    #To open run prompt
    if not is_open():
        pyautogui.keyDown('winleft')
        pyautogui.press('r')
        pyautogui.keyUp('winleft')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(1)
        #Application not found
        app_not_found = pyautogui.locateOnScreen('Images/app_not_found.png')
        if (app_not_found):
            return 'Application not found'
        else:
            print('Open success')

def close_chrome():
    #To close chrome
    time.sleep(1)
    close = pyautogui.locateCenterOnScreen('Images/close.png',confidence=0.8)
    if (close):
        pyautogui.click(close)
        print('Close success')

def minimize_chrome():
    #To minimize chrome
    minimize = pyautogui.locateCenterOnScreen('Images/minimize.png',confidence=0.8)
    if(minimize):
        pyautogui.click(minimize)
        print('Minimize success')
    else:
        print('Chrome is already minimized/closed')

def maximize_chrome():
    #To maximize chrome
    time.sleep(1)
    maximize_on_screen = pyautogui.locateCenterOnScreen('Images/maximize_on_screen.png',confidence=0.8)
    maximize = pyautogui.locateCenterOnScreen('Images/maximize.png',confidence=0.8)
    if(maximize_on_screen):
        pyautogui.click(maximize_on_screen)
        print('Maximize Success')
    elif (maximize):
        pyautogui.click(maximize)
        print('Maximize Success')
    else:
        print("Chrome is maximized/closed")

def browse_chrome(search_word):
    pyautogui.hotkey('ctrl', 'k')
    pyautogui.write(search_word)
    pyautogui.press('enter')

def back():
    time.sleep(1)
    previous_page = pyautogui.locateCenterOnScreen('Images/previouspage.png',confidence=0.8)
    print(previous_page)
    if (previous_page):
        pyautogui.click(previous_page)
        print('Moved to previous page')

def forward():
    time.sleep(1)
    next_page = pyautogui.locateCenterOnScreen('Images/nextpage.png',confidence=0.8)
    print(next_page)
    if (next_page):
        pyautogui.click(next_page)
        print('Moved to next page')

def reload():
    time.sleep(1)
    reload_page = pyautogui.locateCenterOnScreen('Images/reload.png',confidence=0.5)
    print(reload_page)
    if (reload_page):
        pyautogui.click(reload_page)
        print('Reloaded page')

def page_up():
    time.sleep(5)
    pyautogui.press('pgup')

def page_down():
    time.sleep(5)
    pyautogui.press('pgdn')

def scroll_up():
    time.sleep(5)
    pyautogui.press('up')

def scroll_down():
    time.sleep(5)
    pyautogui.press('down')

def click():
    time.sleep(5)
    pyautogui.click()

def down():
    text = 'run'
    os.startfile("C:\\Users\\sinbakum\\Desktop\\mouse_cursor.exe")
    while('stop' not in text):
        with pyautogui.hold('winleft'):
            pyautogui.press('o')
        text = speech_recognize()
    pyautogui.press('esc')

def up():
    text = 'run'
    os.startfile("C:\\Users\\sinbakum\\Desktop\\mouse_cursor.exe")
    while('stop' not in text):
        with pyautogui.hold('winleft'):
            pyautogui.press('i')
        text = speech_recognize()
    pyautogui.press('esc')

def right():
    text = 'run'
    os.startfile("C:\\Users\\sinbakum\\Desktop\\mouse_cursor.exe")
    while('stop' not in text):
        with pyautogui.hold('winleft'):
            pyautogui.press('y')
        text = speech_recognize()
    pyautogui.press('esc')

def left():
    text = 'run'
    os.startfile("C:\\Users\\sinbakum\\Desktop\\mouse_cursor.exe")
    while('stop' not in text):
        with pyautogui.hold('winleft'):
            pyautogui.press('j')
        text = speech_recognize()
    pyautogui.press('esc')

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def switch(text):
    if "open" in text:
        open_chrome()
    elif "minimize" in text:
        minimize_chrome()
    elif "maximize" in text:
        maximize_chrome()
    elif "wait" in text:
        time.sleep(10)
    elif "search" in text:
        SpeakText('What to search?')
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
            SpeakText("Recognizing your text.............")
            search_word = r.recognize_google(audio_data)
        browse_chrome(search_word)
    elif "back" in text:
        back()
    elif "next" in text:
        forward()
    elif "reload" in text:
        reload()
    elif "scroll" in text and "up" in text:
        scroll_up()
    elif "scroll" in text and "down" in text:
        scroll_down()
    elif "page" in text and "up" in text:
        page_up()
    elif "page" in text and "down" in text:
        page_down()
    elif "pointer" in text and "down" in text:
        down()
    elif "pointer" in text and "up" in text:
        up()
    elif "pointer" in text and "left" in text:
        left()
    elif "pointer" in text and "right" in text:
        right()
    elif "click" in text:
        click()
    elif "close" in text:
        close_chrome()
        exit(0)

def speech_recognize():
        text = 'None'
        try:
            SpeakText('What should I do now?')
            print("Listening....")
            with sr.Microphone() as source:
                audio_data = r.record(source, duration=5)
                SpeakText("Recognizing your text.............")
                text = r.recognize_google(audio_data)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
        return text

while(1):
    command = speech_recognize()
    print(command)
    switch(command)

