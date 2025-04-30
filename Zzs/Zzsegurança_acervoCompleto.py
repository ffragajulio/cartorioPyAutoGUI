import pyautogui as pa
import pyperclip as pc
import cv2
import numpy as np
import time

inicio = int(input('primeiro numero:'))


fim = int(input('ultimo numero:')) + 1
time.sleep(10)

template = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\zeroBarraZero.png', cv2.IMREAD_COLOR)
h, w = template.shape[:2]

# pesquisa ctrlfind
for i in range(inicio, fim):
    pa.press('f3')
    pa.write(str(i))
    pa.press('enter')
    
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # faz a comparação da imagem
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    limiar = 0.9  # Pode ajustar esse valor se estiver muito sensível
    
    if max_val >= limiar:
        print('achou 0/0:', str(i))
        pa.hotkey('ctrl', '1')
        continue
    else:
        print('achou diferente')
        
    pa.hotkey('ctrl', 'enter')
    pa.hotkey('ctrl', '2')
        
    time.sleep(1.5) #pausa------------------

    # clica no acervo
    pa.click(x=145, y=460)
    pa.hotkey('ctrl', 'a')
    pa.press('backspace')
    pa.press('1')
    pa.press('tab', presses=2)

    # copia mensagem
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')

    # pega o texto da área de transferência
    mensagem = pc.paste()
    if len(mensagem) >= 4:
        novo_valor = mensagem[:3]
        pa.typewrite(novo_valor)
        
    time.sleep(1.5) #pausa------------------

    # grava e converte
    pa.click(x=100, y=490)
    time.sleep(2)
    pa.click(x=200, y=490)
    time.sleep(2)
    
    # verifica indice
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')
    mensagem = pc.paste()
    if mensagem == 'Índice já convertido para registro':
        print('já convertido:', str(i))

    # volta para pesquisa
    pa.hotkey('ctrl', '1')