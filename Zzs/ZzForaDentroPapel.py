listaNoPapel = []
numerosForaDoPapel = []

anomaliasJC = input('ja convertidas:').split()
anomaliasZZ = input('zero barra zero:').split()

inicio = int(input('primeiro da sequencia:'))
fim = int(input('ultimo da sequencia:'))

for i in range(inicio, fim):
    num = input(i, 'está no papel??? ("enter" para sim & "0" para não): ')
    if num == '':
        listaNoPapel.append(int(num))
        continue
    if num == 0:
        numerosForaDoPapel.append(int(num))

for i in anomaliasJC:
    if i in numerosForaDoPapel:
        anomaliasJC.remove(i)

for i in anomaliasZZ:
    if i in numerosForaDoPapel:
        anomaliasZZ.remove(i)
        
print('Ja convertidos:', anomaliasJC)
print('Zero / Zero:', anomaliasZZ)