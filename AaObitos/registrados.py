import pyautogui as pa
import pyperclip as pc
import cv2
import numpy as np
import time

template = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obito.png', cv2.IMREAD_COLOR)
h, w = template.shape[:2]

a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
time.sleep(10)

for i in range(a, b + 1):
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
    
    # verifica se existe obito registrado
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    limiar = 0.9  # ajustar esse valor se estiver muito sensível
    
    if max_val >= limiar:
        # existe obito
        time.sleep(6)
        
        # clica em impressao
        pa.click(x=35, y=580)
        time.sleep(1.5)
        
        # folha
        pa.doubleClick(x=201, y=324)
        pa.hotkey('ctrl', 'c')
        # pega o texto da área de transferência
        folha = pc.paste()
        if len(folha) >= 4:
            novo_valor = folha[:3]
            pa.typewrite(novo_valor)
        
        # muda p termo e escreve
        pa.press('tab')
        pa.write(str(i))
        
        # muda p acervo e escreve
        pa.press('tab')
        pa.press('1')
        
        # grava
        pa.click(x=373, y=319)
        
        time.sleep(2)
    else:
        # nao eiste obito
        time.sleep(6)
        
        # clica no acervo
        pa.doubleClick(x=145, y=460)
        pa.press('1')
        
        # passa p folha e verifica
        pa.press('tab', presses=2)
        # folha
        pa.doubleClick(x=201, y=324)
        pa.hotkey('ctrl', 'c')
        folha = pc.paste()
        if len(folha) >= 4:
            novo_valor = folha[:3]
            pa.typewrite(novo_valor)
        
        # escreve o termo
        pa.press('tab')
        pa.write(str(i))
        
        # grava e converte
        pa.click(x=100, y=490)
        time.sleep(0.10)
        pa.click(x=200, y=490)
        time.sleep(2.1)
    
    # clica pesquisa nova
    pa.rightClick(x=1120, y=105)
    
    # apaga primeira guia
    pa.middleClick(x=150, y=15)