import pyautogui as pa
import pyperclip as pc
import cv2
import numpy as np
import time

# Carregar templates
template1 = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obito1.png', cv2.IMREAD_COLOR)
template2 = cv2.imread(r'C:\Users\usuario\Desktop\codigos\automatizacao\assets\obito2.png', cv2.IMREAD_COLOR)
h1, w1 = template1.shape[:2]
h2, w2 = template2.shape[:2]

# Entradas do usuário
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
d1 = input('insira a data inicial: ')
d2 = input('insira a data final: ')
time.sleep(10)

# Função para verificar se a imagem existe na tela
def verificar_obito(screenshot):
    result1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
    _, max_val1, _, max_loc1 = cv2.minMaxLoc(result1)
    _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
    limiar = 0.9  # Ajustar esse valor se estiver muito sensível
    return max_val1 >= limiar or max_val2 >= limiar

# Função para localizar e clicar no centro da imagem template na tela
def clicar_na_imagem(template, limiar=0.9):
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= limiar:
        h, w = template.shape[:2]
        centro_x = max_loc[0] + w // 2
        centro_y = max_loc[1] + h // 2
        pa.click(centro_x, centro_y)
        print(f"Clique realizado na imagem em ({centro_x}, {centro_y}) com valor de confiança {max_val:.2f}")
        return True
    else:
        print(f"Imagem não encontrada para clique (threshold {limiar}), max_val {max_val:.2f}")
        return False

for i in range(a, b + 1):
    # Clica no input e escreve
    pa.doubleClick(x=85, y=170)
    pa.write(str(i))

    # Troca pesquisa para data
    pa.press('tab', presses=2)

    # Escreve data, pula, e escreve novamente
    pa.write(d1)
    pa.press('tab')
    pa.write(d2)

    # Clica pesquisar
    pa.click(x=55, y=200)
    
    time.sleep(2)
    
    # Verifica se existe óbito registrado
    screenshot = pa.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    if verificar_obito(screenshot):
        # Existe óbito
        time.sleep(6)

        # Clica na imagem1 (óbito1.png)
        clicou = clicar_na_imagem(template1)
        if not clicou:
            print("Clique na imagem1 falhou, realizando clique fixo como fallback.")
            pa.click(x=35, y=580)  # fallback para clicar em impressão se a imagem não for encontrada
        time.sleep(1.5)
        
        # Folha
        pa.doubleClick(x=201, y=324)
        pa.hotkey('ctrl', 'c')
        # Pega o texto da área de transferência
        folha = pc.paste()
        if len(folha) >= 4:
            novo_valor = folha[:3]
            pa.typewrite(novo_valor)
        
        # Muda para o termo e escreve
        pa.press('tab')
        pa.write(str(i + 1000))
        
        # Muda para acervo e escreve
        pa.press('tab')
        pa.press('1')
        
        # Grava
        pa.click(x=373, y=319)
        
        time.sleep(2)
    else:
        # Não existe óbito
        time.sleep(6)
        
        # Clica na imagem2 (óbito2.png)
        clicou = clicar_na_imagem(template2)
        if not clicou:
            print("Clique na imagem2 falhou, realizando clique fixo como fallback.")
            pa.doubleClick(x=145, y=460)  # fallback para clicar no acervo se a imagem não for encontrada
        pa.press('1')
        
        # Passa para folha e verifica
        pa.press('tab', presses=2)
        # Folha
        pa.doubleClick(x=201, y=324)
        pa.hotkey('ctrl', 'c')
        folha = pc.paste()
        if len(folha) >= 4:
            novo_valor = folha[:3]
            pa.typewrite(novo_valor)
        
        # Escreve o termo
        pa.press('tab')
        pa.write(str(i))
        
        # Grava e converte
        pa.click(x=100, y=490)
        time.sleep(0.10)
        pa.click(x=200, y=490)
        time.sleep(2.1)
    
    # Clica pesquisa nova
    pa.rightClick(x=1120, y=105)
    
    # Apaga primeira guia
    pa.middleClick(x=150, y=15)