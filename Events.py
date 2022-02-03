from platform import system as sys
from os import system
from time import sleep
from keyboard import is_pressed
from threading import Thread
import win10toast
from plyer import notification


def platform():
    need_stop = False
    title = 'Smoke Break' 
    message = 'An hour and half passed\nSee ya in same time' 
    plt = sys() 
    thread = Thread(target=push, args=(plt, title, message))
    thread.daemon = True
    thread.start()
    while True:
        if is_pressed('home'): 
            need_stop = True
        if thread.is_alive() and need_stop:
            break
        sleep(0.2)


def push(plt, title, message):
    while True:
        if plt == "Linux":
            command = f'''
            notify-send "{title}" "{message}"
            '''
            system(command)
        elif plt == "Windows":
            try: 
                win10toast.ToastNotifier().show_toast(title, message)
            except Exception:
                notification.notify(title, message)
        else:
            return
        sleep(5400)


if __name__ == '__main__':
    platform()
