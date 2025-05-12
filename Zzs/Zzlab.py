import pyautogui as pa
import pyperclip as pc
import cv2
import numpy as np
import time


a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
time.sleep(10)

for i in range(a, b + 1):
    template1 = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obito1.png', cv2.IMREAD_COLOR)
    template2 = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obito2.png', cv2.IMREAD_COLOR)
    h1, w1 = template1.shape[:2]
    h2, w2 = template2.shape[:2]
    # clica no input e escreve
    pa.doubleClick(x=85, y=170)
    pa.write(str(i))

    # troca pesquisa para data
    pa.press('tab', presses=2)

    # escreve data, pula, e escreve dnv
    pa.write('01/12/1959')
    pa.press('tab')
    pa.write('29/01/1960')

    # clica pesquisar
    pa.click(x=55, y=200)
    
    time.sleep(2)
    
    # verifica se existe obito registrado
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    result1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, max_loc1 = cv2.minMaxLoc(result1)
    _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
    limiar = 0.9  # ajustar esse valor se estiver muito sensível
    
    if max_val1 >= limiar or max_val2 >= limiar:
        print('existe obito')
    else:
        print('nao existe obito')
    
    # clica pesquisa nova
    pa.rightClick(x=1120, y=105)
    
    # apaga primeira guia
    pa.middleClick(x=150, y=15)