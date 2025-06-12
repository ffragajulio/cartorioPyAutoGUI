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

livroCerto = str(input('qual o livro?'))

soma = int(input('quanto soma?'))

time.sleep(10)

jc = []
zz = []

template = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\zeroBarraZero.png', cv2.IMREAD_COLOR)
h, w = template.shape[:2]

# pesquisa ctrl + find
for i in lista:
    pa.press('f3')
    pa.write(str(i+soma) + ') o')
    
    time.sleep(0.3)
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # faz a comparação da imagem
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    limiar = 0.9  # Pode ajustar esse valor se estiver muito sensível
    
    if max_val >= limiar:
        zz.append(str(i))
        print(i, 'nao encontrou (0/0)')
        continue
        
    pa.hotkey('ctrl', 'enter')
    time.sleep(0.05)
    pa.click(x=380, y=15)
        
    # carregue botoes
    template_botoes = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\gravaConverte.png', 0)
    w, h = template_botoes.shape[::-1]

    limite_correspondencia = 0.8

    while True:
        # captura a tela inteira
        screenshot = pa.screenshot()
        tela_cinza = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # aplica o template matching
        resultado = cv2.matchTemplate(tela_cinza, template_botoes, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= limite_correspondencia:
            break
        time.sleep(0.25)

    # clica no acervo
    pa.click(x=145, y=460)
    pa.hotkey('ctrl', 'a')
    pa.press('1')
    pa.press('tab')
    
    # verifica livro
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')
    livro = pc.paste()
    if livro[2:] != livroCerto:
        print(i, 'com livro errado')
        pa.middleClick(x=380, y=15)
        continue
    
    pa.press('tab')

    # copia mensagem
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')

    # pega o texto da área de transferência e cola com len() = 3
    folha = pc.paste()
    if len(folha) >= 4:
        novo_valor = folha[:3]
        pa.typewrite(novo_valor)
        
    # escreve termo certo
    pa.press('tab')
    pa.write(str(i))

    # grava e converte
    pa.click(x=100, y=490)
    time.sleep(0.10)
    pa.click(x=200, y=490)
    time.sleep(2.1)
    
    # carrega foto guia obito
    template_obitoNav = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obitoNavegador.png', 0)
    w, h = template_obitoNav.shape[::-1]
    
    while True:
        # captura a tela inteira
        screenshot = pa.screenshot()
        obitoNav = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # aplica o template matching
        resultado = cv2.matchTemplate(obitoNav, template_obitoNav, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

        if max_val >= limite_correspondencia:
            break
        time.sleep(0.25)
        pa.click(x=200, y=490)
        time.sleep(2.1)
    
    # verifica mensagem
    pa.hotkey('ctrl', 'a')
    pa.hotkey('ctrl', 'c')
    mensagem = pc.paste()
    if mensagem == ('Índice já convertido para registro' or ''):
        jc.append(str(i))
        print(i, 'ja convertido')
    
    pa.click(x=190, y=120)

    # volta para pesquisa
    pa.middleClick(x=380, y=15)

print('---------------------------')
print('ja convertidos ou erro:')
for i in jc:
    print(i)
print('---------------------------')
print('nao encontrados:')
for i in zz:
    print(i)