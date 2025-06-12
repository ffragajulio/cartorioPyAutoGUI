import pyautogui as pa, time
# d1 = input('primeira data:')
# d2 = input('segunda data:')
d1 = '06111944'
d2 = '09071946'
t1 = int(input('primeiro termo:'))
t2 = int(input('segundo termo:'))
time.sleep(3)
for i in range(t1,t2):
    # clica no input
    pa.doubleClick(x=85, y=170)
    
    pa.write(i)

    # troca pesquisa para data
    pa.press('tab', presses=2)

    # escreve data, pula, e escreve novamente
    pa.write(d1)
    pa.press('tab')
    pa.write(d2)