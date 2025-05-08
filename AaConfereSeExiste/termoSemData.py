import pyautogui as pa
import pyperclip as pc
import cv2
import numpy as np
import time

# transforma string de "121 123 a 132 134 136" em lista
def expandir_intervalos(entrada):
    partes = entrada.split()
    resultado = []
    i = 0
    while i < len(partes):
        if len(partes[i]) < 4:  # assume que é o "a"
            inicio = int(partes[i - 1])
            fim = int(partes[i + 1])
            resultado.pop()
            resultado.extend(range(inicio, fim + 1))
            i += 2
        else:
            resultado.append(int(partes[i]))
            i += 1
    return resultado
entrada = input()

lista = expandir_intervalos(entrada)

time.sleep(10)

jc = []
zz = []

template = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\zeroBarraZero.png', cv2.IMREAD_COLOR)
h, w = template.shape[:2]

# pesquisa ctrl + find
for i in lista:
    
    # clica no campo, escreve, pesquisa
    pa.doubleClick(x=100, y=175)
    pa.write(str(i))
    pa.click(x=55, y=195)
    
    pa.press('f3')
    time.sleep(3.5)
    
    
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # faz a comparação da imagem
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    limiar = 0.9  # Pode ajustar esse valor se estiver muito sensível
    
    if max_val >= limiar:
        zz.append(str(i))
        continue
    else:
        jc.append(str(i))
        print('achou diferente')

print('---------------------------')
print('está no sistema:')
for i in jc:
    print(i)
print('---------------------------')
print('nao está no sistema:')
for i in zz:
    print(i)