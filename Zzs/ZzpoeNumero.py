import pyautogui as pa
import time

pa.FAILSAFE = True

inicio = int(input('primeiro numero:'))
fim = int(input('ultimo numero:')) + 1


time.sleep(10)

for i in range(inicio, fim):

    with pa.hold('ctrl'):
        pa.press('a')
        pa.press('backspace')
        
    pa.write(str(i))
    pa.press('enter')
    time.sleep(3.5)
    pa.click(x=98, y=168)