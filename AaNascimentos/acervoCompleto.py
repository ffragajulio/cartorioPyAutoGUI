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
        zz.append(str(i))
        pa.hotkey('ctrl', '1')
        continue
    else:
        print('achou diferente')
        
    pa.hotkey('ctrl', 'enter')
    pa.hotkey('ctrl', '2')
        
    time.sleep(1) #pausa------------------

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
    folha = pc.paste()
    if len(folha) >= 4:
        novo_valor = folha[:3]
        pa.typewrite(novo_valor)

    # grava e converte
    pa.click(x=100, y=490)
    time.sleep(0.25)
    pa.click(x=200, y=490)
    time.sleep(1.75)
    
    # verifica mensagem
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')
    mensagem = pc.paste()
    if mensagem == 'Índice já convertido para registro':
        jc.append(str(i))

    # volta para pesquisa
    pa.hotkey('ctrl', '1')

print('---------------------------')
print('ja convertidos:')
for i in jc:
    print(i)
print('---------------------------')
print('nao encontrados:')
for i in zz:
    print(i)