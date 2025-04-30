import pyautogui as pa, sys, time

try:
    time.sleep(3)
    for i in range(5,-1,-1):
        pa.write(str(i))
        time.sleep(1)
except KeyboardInterrupt:
    print('\n')