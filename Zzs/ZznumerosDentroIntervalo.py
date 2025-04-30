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
print(expandir_intervalos(entrada))