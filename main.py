from datetime import date, datetime
from threading import Thread

import requests
import time


def countdown(t):
    while t:
        minutes, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(10)
        print_massage("Status: ")
        t -= 1
    print('Fire in the hole!!')


def print_massage(massage):
    now = datetime.now()
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    t1 = now.strftime("%H:%M:%S")
    x = requests.get('https://google.com/')
    print(f' {d1} {t1} {massage} {x.status_code} ')  # Press Ctrl+F8 to toggle the breakpoint.


def func():
    thread = Thread(target=countdown(9))
    thread.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Here we start : ")
    func()


